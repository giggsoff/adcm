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


from selenium.webdriver.common.by import By

from tests.ui_tests.app.helpers.locator import Locator


class ClusterMenuLocators:
    """Cluster menu elements locators"""

    main_tab = Locator(By.XPATH, "//a[@adcm_test='tab_main']", "Tab main")
    services_tab = Locator(By.XPATH, "//a[@adcm_test='tab_service']", "Tab services")
    hosts_tab = Locator(By.XPATH, "//a[@adcm_test='tab_host']", "Tab hosts")
    components_tab = Locator(By.XPATH, "//a[@adcm_test='tab_host_component']", "Tab components")
    config_tab = Locator(By.XPATH, "//a[@adcm_test='tab_config']", "Tab config")
    status_tab = Locator(By.XPATH, "//a[@adcm_test='tab_status']", "Tab status")
    import_tab = Locator(By.XPATH, "//a[@adcm_test='tab_import']", "Tab import")
    actions_tab = Locator(By.XPATH, "//a[@adcm_test='tab_action']", "Tab actions")


class ClusterMainLocators:
    """Cluster main page elements locators"""

    text = Locator(By.XPATH, "//mat-card-content", "Cluster main page text")


class ClusterServicesLocators:
    """Cluster main page elements locators"""

    add_services_btn = Locator(By.XPATH, "//button[@adcm_test='create-btn']", "Add services button")


class ClusterImportLocators:
    """Cluster import page elements locators"""

    import_item_block = Locator(By.XPATH, "//div[@class='items']/div", "Import item block")
