import Vue from "vue";
import App from "./App.vue";
import axios from "axios";

axios.defaults.baseURL = "http://127.0.0.1:8000/translate";

Vue.config.productionTip = false;

new Vue({
  render: h => h(App)
}).$mount("#app");
