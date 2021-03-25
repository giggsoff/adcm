# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ansible.errors import AnsibleError
from ansible.plugins.action import ActionBase
from ansible.utils.vars import merge_hash
import cm


MSG_NO_CONFIG = (
    "There are no job related vars in inventory. It's mandatory for that module to have some"
    " info from context. During normal execution it runs with inventory and config.yaml generated"
    " by ADCM. Did you forget to pass them during debug? Bad Dobby!"
)
MSG_NO_CONTEXT = (
    "There are no context variable in job related vars in inventory. It's mandatory for that "
    "module to have some info from context. During normal execution it runs with inventory and "
    "config.yaml generated by ADCM. Did you forget to pass them during debug? Bad Dobby!"
)
MSG_WRONG_CONTEXT = 'Wrong context. Should be "{}", not "{}"'
MSG_WRONG_CONTEXT_ID = 'Wrong context. There are no "{}" in context'
MSG_NO_CLUSTER_CONTEXT = (
    "You are trying to change cluster state outside of cluster context. Cluster state can be "
    "changed in cluster's or service's actions only. Bad Dobby!"
)
MSG_NO_CLUSTER_CONTEXT2 = (
    "You are trying to change service state outside of cluster context. Service state can be"
    " changed by service_name in cluster's actions only. Bad Dobby!"
)
MSG_NO_SERVICE_CONTEXT = (
    "You are trying to change unnamed service's state outside of service context."
    " Service state can be changed in service's actions only or in cluster's actions but"
    " with using service_name arg. Bad Dobby!"
)
MSG_MANDATORY_ARGS = "Arguments {} are mandatory. Bad Dobby!"
MSG_NO_ROUTE = "Incorrect combination of args. Bad Dobby!"
MSG_WRONG_SERVICE = "Do not try to change one service from another."


def check_context_type(task_vars, *context_type, err_msg=None):
    """
    Check context type. Check if inventory.json and config.json were passed
    and check if `context` exists in task variables, сheck if a context is of a given type.
    """
    if not task_vars:
        raise AnsibleError(MSG_NO_CONFIG)
    if 'context' not in task_vars:
        raise AnsibleError(MSG_NO_CONTEXT)
    if not isinstance(task_vars['context'], dict):
        raise AnsibleError(MSG_NO_CONTEXT)
    context = task_vars['context']
    if context['type'] not in context_type:
        if err_msg is None:
            err_msg = MSG_WRONG_CONTEXT.format(', '.join(context_type), context['type'])
        raise AnsibleError(err_msg)


def get_object_id_from_context(task_vars, id_type, *context_type, err_msg=None):
    """
    Get object id from context.
    """
    check_context_type(task_vars, *context_type, err_msg=err_msg)
    context = task_vars['context']
    if id_type not in context:
        raise AnsibleError(MSG_WRONG_CONTEXT_ID.format(id_type))
    return context[id_type]


class ContextActionModule(ActionBase):

    TRANSFERS_FILES = False
    _VALID_ARGS = None
    _MANDATORY_ARGS = None

    def _wrap_call(self, func, *args):
        try:
            func(*args)
        except cm.errors.AdcmEx as e:
            return {'failed': True, 'msg': e.msg}
        return {'changed': True}

    def _check_mandatory(self):
        for arg in self._MANDATORY_ARGS:
            if arg not in self._task.args:
                raise AnsibleError(MSG_MANDATORY_ARGS.format(self._MANDATORY_ARGS))

    def _get_job_var(self, task_vars, name):
        try:
            return task_vars["job"][name]
        except KeyError as error:
            raise AnsibleError(MSG_NO_CLUSTER_CONTEXT) from error

    def _do_cluster(self, task_vars, context):
        raise NotImplementedError

    def _do_service_by_name(self, task_vars, context):
        raise NotImplementedError

    def _do_service(self, task_vars, context):
        raise NotImplementedError

    def _do_host(self, task_vars, context):
        raise NotImplementedError

    def run(self, tmp=None, task_vars=None):
        self._check_mandatory()
        obj_type = self._task.args["type"]

        if obj_type == 'cluster':
            check_context_type(task_vars, 'cluster', 'service')
            res = self._do_cluster(
                task_vars,
                {'cluster_id': self._get_job_var(task_vars, 'cluster_id')}
            )
        elif obj_type == "service" and "service_name" in self._task.args:
            check_context_type(task_vars, 'cluster', 'service')
            context = task_vars['context']
            if context['type'] == 'service':
                service = cm.models.ClusterObject.objects.get(pk=context["service_id"])
                service_name = service.prototype.name
                if service_name != self._task.args["service_name"]:
                    # It is forbiden to change one service from another one.
                    # But due to usage pattern it is common case when developers
                    # use service_name in service playbooks to make them general
                    # use (for cluster context and for service context)
                    raise AnsibleError(MSG_WRONG_SERVICE)
            res = self._do_service_by_name(
                task_vars,
                {'cluster_id': self._get_job_var(task_vars, 'cluster_id')}
            )
        elif obj_type == "service":
            check_context_type(task_vars, 'service')
            res = self._do_service(
                task_vars,
                {
                    'cluster_id': self._get_job_var(task_vars, 'cluster_id'),
                    'service_id': self._get_job_var(task_vars, 'service_id')
                }
            )
        elif obj_type == "host" and "host_id" in self._task.args:
            check_context_type(task_vars, 'provider')
            res = self._do_host_from_provider(
                task_vars,
                {}
            )
        elif obj_type == "host":
            check_context_type(task_vars, 'host')
            res = self._do_host(
                task_vars,
                {'host_id': self._get_job_var(task_vars, 'host_id')}
            )
        elif obj_type == "provider":
            check_context_type(task_vars, 'provider')
            res = self._do_provider(
                task_vars,
                {'provider_id': self._get_job_var(task_vars, 'provider_id')}
            )
        elif obj_type == "component":
            check_context_type(task_vars, 'component')
            res = self._do_component(
                task_vars,
                {'component_id': self._get_job_var(task_vars, 'component_id')}
            )
        else:
            raise AnsibleError(MSG_NO_ROUTE)

        result = super().run(tmp, task_vars)
        return merge_hash(result, res)
