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

export default {
  name: "Main",
  components: {
    TopBar,
  },
  computed: {},
  created() {},
  mounted() {},
  data() {
    return {};
  },
  methods: {},
};
</script>
