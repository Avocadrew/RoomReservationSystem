import { createRouter, createWebHistory } from "vue-router";
import Main from "../views/Main.vue";
import ChooseDateAndRoom from "../views/ChooseDateAndRoom.vue";
import ChooseMultiDateAndRoom from "../views/ChooseMultiDateAndRoom.vue";
import MeetingInfo from "../views/MeetingInfo.vue";
import CreateAccount from "../views/CreateAccount.vue";
import ChooseActions from "../views/ChooseActions.vue";
import ChooseTypes from "../views/ChooseTypes.vue";
import ChooseTime from "../views/ChooseTime.vue";
import FillOutMeetingInfo from "../views/FillOutMeetingInfo.vue";
import LandingPage from "../views/LandingPage.vue";
import PersonalInformation from "../views/PersonalInformation.vue";
import EditPersonalInformation from "../views/EditPersonalInformation.vue";
import CreateAndModifyAGroup from "../views/CreateAndModifyAGroup.vue";
import Records from "../views/Records.vue";

const routes = [
  {
    path: "",
    name: "Root",
    redirect: "/main",
  },
  {
    path: "/main",
    name: "Main",
    component: Main,
    redirect: "/main/landingpage",
    children: [
      {
        path: "meetinginfo",
        name: "MeetingInfo",
        component: MeetingInfo,
      },
      {
        path: "createaccount",
        name: "CreateAccount",
        component: CreateAccount,
      },
      {
        path: "chooseactions",
        name: "ChooseActions",
        component: ChooseActions,
      },
      {
        path: "choosetypes",
        name: "ChooseTypes",
        component: ChooseTypes,
      },
      {
        path: "single",
        name: "ChooseDateAndRoom",
        component: ChooseDateAndRoom,
        children: [
          {
            path: "",
            name: "ChooseTime",
            component: ChooseTime,
          },
        ],
      },
      {
        path: "multiple",
        name: "ChooseMultiDateAndRoom",
        component: ChooseMultiDateAndRoom,
      },
      {
        path: "filloutmeetinginfo",
        name: "",
        component: FillOutMeetingInfo,
        children: [
          {
            path: "",
            name: "FillOutMeetingInfo",
            component: CreateAndModifyAGroup,
          },
        ],
      },
      {
        path: "personalinformation",
        name: "PersonalInformation",
        component: PersonalInformation,
      },
      {
        path: "editpersonalinformation",
        name: "EditPersonalInformation",
        component: EditPersonalInformation,
      },
      {
        path: "landingpage",
        name: "LandingPage",
        component: LandingPage,
      },
      {
        path: "records",
        name: "Records",
        component: Records,
      },
    ],
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
