import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
//import i18n from "./common/plugins/vue-i18n";

import { SetupCalendar, Calendar, DatePicker } from "v-calendar";
import vSelect from "vue-select";
import mdiVue from "mdi-vue/v3";
import Datepicker from "vue3-date-time-picker";
import "vue3-date-time-picker/dist/main.css";
import * as mdijs from "@mdi/js";
import VueCookies from "vue3-cookies";

const app = createApp(App);
app
  .use(router)
  .use(SetupCalendar, {})
  .use(mdiVue, { icons: mdijs })
  .use(VueCookies, {
    expireTimes: "30d",
    secure: true,
  })
  .component("Calendar", Calendar)
  .component("DatePicker", DatePicker)
  .component("v-select", vSelect)
  .component("Datepicker", Datepicker)
  .mount("#app");

app.config.globalProperties.$MONTHS = [
  "January",
  "February",
  "March",
  "April",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December",
];
app.config.globalProperties.$ROOMS = [
  "Room1",
  "Room2",
  "Room3",
  "Room4",
  "Room5",
  "Room6",
];
app.config.globalProperties.$AVAILABLE_TIME = {
  STARTING_HOURS: 9,
  STARTING_MINUTES: 0,
  ENDING_HOURS: 17,
  ENDING_MINUTES: 0,
  INTERVAL: 30,
};
app.config.globalProperties.$REPEAT_UNITS = ["day", "week", "month"];
