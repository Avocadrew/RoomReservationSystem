import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
//import i18n from "./common/plugins/vue-i18n";

createApp(App).use(router).mount("#app");
