<template>
  <div class="hello">
    <div class="form-group">
      <label for="languageIn">Language input:&nbsp;</label>
      <select id="languageIn" class="form-control" v-model="userData.langIn">
        <option v-for="language in languages" :key="language">{{ language }}</option>
      </select>

      <br />

      <label for="languageOut">Language output:&nbsp;</label>
      <select id="languageOut" class="form-control" v-model="userData.langOut">
        <option v-for="language in languages" :key="language">{{ language }}</option>
      </select>

      <br />
      <br />

      <label for="text">Type text to be translated</label>
      <br />
      <br />
      <label>
        File
        <input type="file" id="file" ref="file" v-on:change="handleFileUpload()" />
      </label>
      <br />
      <br />
      <textarea id="text" rows="5" class="form-control" v-model="userData.text"></textarea>
      <br />
      <br />
      <button class="btn btn-primary" @click.prevent="submitted">Translate</button>
    </div>
    <br />
    <div class="response">
      <span v-if="loading">Translating...</span>
      {{translation}}
    </div>
  </div>
</template>

<script>
import LanguageService from "@/services/Language";

export default {
  name: "HelloWorld",
  data() {
    return {
      userData: {
        text: "",
        json: {},
        langIn: "en",
        langOut: "nl"
      },
      languages: ["en", "nl"],
      isSubmitted: false,
      translation: "",
      loading: false,

      file: "",
      translateJson: false
    };
  },
  methods: {
    handleFileUpload() {
      this.file = this.$refs.file.files[0];
      console.log(this.file["type"]);

      if (this.file["type"] === "text/plain") {
        const reader = new FileReader();
        reader.onload = e => (this.userData.text = e.target.result);

        reader.readAsText(this.file);
      } else if (this.file["type"] === "application/json") {
        const reader = new FileReader();
        reader.onload = e => {
          let json;
          try {
            json = JSON.parse(e.target.result);
            this.translateJson = true;

            this.userData.json = JSON.stringify(json);
          } catch (ex) {
            alert("ex when trying to parse json = " + ex);
          }
        };
        reader.readAsText(this.file);
      }
    },
    downloadJson(json) {
      const data = JSON.stringify(json);
      const blob = new Blob([data], { type: "text/plain" });
      const e = document.createEvent("MouseEvents");
      const a = document.createElement("a");
      a.download = "test.json";
      a.href = window.URL.createObjectURL(blob);
      a.dataset.downloadurl = ["text/json", a.download, a.href].join(":");
      e.initEvent(
        "click",
        true,
        false,
        window,
        0,
        0,
        0,
        0,
        0,
        false,
        false,
        false,
        false,
        0,
        null
      );
      a.dispatchEvent(e);
    },
    submitted() {
      this.isSubmitted = true;
      this.loading = true;
      this.translation = "";

      if (this.translateJson) {
        LanguageService.translateJson(this.userData).then(translation => {
          console.log(translation);
          this.translation = translation;
          this.loading = false;
          this.translateJson = false;
          this.downloadJson(translation);
        });
      } else {
        console.log(this.userData);
        LanguageService.translate(this.userData).then(
          translation => (
            (this.translation = translation), (this.loading = false)
          )
        );
      }
    }
  },
  props: {
    msg: String
  },
  mounted() {
    LanguageService.getLanguages().then(langs => (this.languages = langs));
  }
};
</script>

<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
