<template>
  <div class="container-overflow-hidden">
    <TopBar />
    <div class="post-top-bar">
      <img class="background" src="@/assets/background.jpg" alt="background" />
      <div
        class="
          container
          container-flex
          container-useless-wrapper
          container-router-view
        "
      >
        <div class="card">
          <div class="card-label">
            <div class="card-label-text">
              <p>{{ currentPage }}</p>
            </div>
          </div>
          <div class="card-body">
            <router-view />
          </div>
        </div>
      </div>
      <!--
      <a href="http://www.freepik.com">Background designed by Freepik</a>
			-->
    </div>
  </div>
</template>

<script>
import TopBar from "@/components/TopBar.vue";
import eruda from "../../node_modules/eruda/eruda.js";

export default {
  name: "Main",
  components: {
    TopBar,
  },
  data() {
    return {
      currentPage: "Reservation System",
      pathToLabel: {
        landingpage: "Reservation System",
        chooseactions: "Menu",
        single: "Date and Room",
        filloutmeetinginfo: "Meeting Info",
        records: "Records",
        personalinformation: "Personal Information",
        editpersonalinformation: "Personal Information",
        createaccount: "Create Account",
      },
    };
  },
  computed: {},
  created() {},
  mounted() {
    eruda.init();
  },
  updated() {
    console.log(this.$route.fullPath);
  },
  watch: {
    $router: {
      handler: function () {
        let path = this.$route.path;
        path = path.split("/")[path.split("/").length - 1];
        this.currentPage = this.pathToLabel[path];
      },
      deep: true,
      immediate: true,
    },
  },
  methods: {},
};
</script>
