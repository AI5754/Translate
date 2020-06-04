import axios from "axios";

export default {
  getLanguages() {
    return axios.get("/languages/").then(response => response.data);
  },

  translate(payload) {
    let paramsUrl =
      "?text=" +
      payload.text +
      "&langIn=" +
      payload.langIn +
      "&langOut=" +
      payload.langOut;

    return axios.get(paramsUrl).then(response => response.data);
  },

  translateJson(payload) {
    let paramsUrl =
      "/json/?json=" +
      payload.json +
      "&langIn=" +
      payload.langIn +
      "&langOut=" +
      payload.langOut;

    return axios.get(paramsUrl).then(response => response.data);
  }
};
