<template>
  <div>
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
          <router-view />
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
  computed: {},
  created() {},
  mounted() {
    eruda.init();
  },
  updated() {
    console.log(this.$route.fullPath);
  },
  data() {
    return {};
  },
  methods: {},
};
</script>
