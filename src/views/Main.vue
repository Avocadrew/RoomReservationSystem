<template>
  <div>
    <TopBar />
    <div class="post-top-bar">
      <router-view />
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
  data() {
    return {};
  },
  methods: {},
};
</script>
