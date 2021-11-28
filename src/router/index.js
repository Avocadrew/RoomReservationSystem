import { createRouter, createWebHistory } from "vue-router";
import Main from "../views/Main.vue";
import ChooseDateAndRoom from "../views/DateAndRoom.vue";
import MeetingInfo from "../views/MeetingInfo.vue";
import CreateAccount from "../views/CreateAccount.vue";
import ChooseActions from "../views/ChooseActions.vue";
import ChooseTypes from "../views/ChooseTypes.vue";
import ChooseTime from "../views/ChooseTime.vue";
import FillOutMeetingInfo from "../views/FillOutMeetingInfo.vue";

const routes = [
  {
    path: "/main",
    name: "Main",
    component: Main,
		redirect: "/main/chooseactions", 
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
				path: "reservation/choosetypes", 
				name: "ChooseTypes", 
				component: ChooseTypes, 
			}, 
			{
				path: "reservation/multiple", 
        name: "ChooseDateAndRoom",
        component: ChooseDateAndRoom,
				children: [
					{
						path: "chooseTime", 
						name: "ChooseTime", 
						component: ChooseTime, 
					}, 
				], 
			}, 
			{
				path: "reservation/filloutmeetinginfo", 
				name: "FillOutMeetingInfo", 
				component: FillOutMeetingInfo, 
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
