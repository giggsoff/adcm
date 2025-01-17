// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';

import { ActionsComponent, CrumbsComponent, UpgradeComponent } from './components';
import { ActionListComponent } from './components/actions/action-list/action-list.component';
import { ActionsDirective } from './components/actions/actions.directive';
import { UpgradesDirective } from './components/upgrades/upgrade.directive';
import { TooltipDirective } from '@app/shared/components/tooltip';
import { PopoverDirective } from '@app/directives/popover.directive';
import {
  BaseDirective,
  ForTestDirective,
  InfinityScrollDirective,
  MTextareaDirective,
  ScrollDirective,
  SocketListenerDirective
} from './directives';
import { MaterialModule } from './material.module';
import { MenuItemComponent } from './components/actions/action-list/menu-item/menu-item.component';
import { PopoverComponent } from '@app/components/popover/popover.component';
import { KeysPipe } from '@app/pipes/keys.pipe';
import { IsArrayPipe } from '@app/pipes/is-array.pipe';
import { IssuePathPipe } from '@app/pipes/issue-path.pipe';
import { ConcernComponent } from '@app/components/concern/concern.component';
import { ConcernService } from '@app/services/concern.service';
import { ConcernItemComponent } from '@app/components/concern/concern-item/concern-item.component';
import { IssueMessagePlaceholderPipe } from '@app/pipes/issue-message-placeholder.pipe';
import { ConcernListComponent } from '@app/components/concern/concern-list/concern-list.component';
import { ConcernListRefComponent } from '@app/components/concern/concern-list-ref/concern-list-ref.component';
import { TooltipModule } from '@app/shared/components/tooltip/tooltip.module';
import { HasSelectedPipe } from '@app/pipes/has-selected.pipe';
import { ActionsButtonComponent } from "@app/components/actions-button/actions-button.component";

@NgModule({
  declarations: [
    ForTestDirective,
    MTextareaDirective,
    BaseDirective,
    SocketListenerDirective,
    CrumbsComponent,
    UpgradeComponent,
    ScrollDirective,
    InfinityScrollDirective,
    ActionsComponent,
    ActionsDirective,
    UpgradesDirective,
    ActionListComponent,
    MenuItemComponent,
    PopoverDirective,
    PopoverComponent,
    ConcernComponent,
    ConcernItemComponent,
    IssueMessagePlaceholderPipe,
    ConcernListComponent,
    ConcernListRefComponent,
    KeysPipe,
    IsArrayPipe,
    HasSelectedPipe,
    IssuePathPipe,
    ActionsButtonComponent,
  ],
  imports: [
    CommonModule,
    MaterialModule,
    RouterModule,
    TooltipModule
  ],
  exports: [
    ForTestDirective,
    TooltipDirective,
    MTextareaDirective,
    BaseDirective,
    SocketListenerDirective,
    CrumbsComponent,
    UpgradeComponent,
    ScrollDirective,
    InfinityScrollDirective,
    ActionsComponent,
    ActionsDirective,
    UpgradesDirective,
    ActionListComponent,
    MenuItemComponent,
    PopoverDirective,
    PopoverComponent,
    ConcernComponent,
    ConcernItemComponent,
    IssueMessagePlaceholderPipe,
    ConcernListComponent,
    KeysPipe,
    IsArrayPipe,
    HasSelectedPipe,
    IssuePathPipe,
    ConcernListRefComponent,
    TooltipModule,
    ActionsButtonComponent
  ],
  providers: [
    ConcernService,
  ],
})
export class StuffModule {}
