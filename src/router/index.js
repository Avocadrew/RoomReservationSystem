import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import Main from "../views/Main.vue";
import DateAndRoom from "../views/DateAndRoom.vue";
import MeetingInfo from "../views/MeetingInfo.vue";
import CreateAccount from "../views/CreateAccount.vue";

const routes = [
  {
    path: "/main",
    name: "Main",
    component: Main,
    children: [
      {
        path: "",
        name: "Home",
        component: Home,
      },
      {
        path: "dateandroom",
        name: "DateAndRoom",
        component: DateAndRoom,
      },
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
