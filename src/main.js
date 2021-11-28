import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
//import i18n from "./common/plugins/vue-i18n";

import { SetupCalendar, Calendar, DatePicker } from "v-calendar";
import vSelect from "vue-select";
import mdiVue from "mdi-vue/v3";
import * as mdijs from "@mdi/js";

const app = createApp(App);
app
  .use(router)
  .use(SetupCalendar, {})
  .use(mdiVue, { icons: mdijs })
  .component("Calendar", Calendar)
  .component("DatePicker", DatePicker)
  .component("v-select", vSelect)
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
