<template>
  <div
    class="loading-animation"
    v-bind:class="{
      'loading-animation-enabled': state == 'enabled',
      'loading-animation-disabled': state == 'disabled',
    }"
  >
    <div class="loading-animation-background"></div>
    <div class="loading-animation-outer-circle">
      <div class="loading-animation-icon"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoadingAnimation",
  data: function () {
    return {
      state: "disabled",
    };
  },
  props: {},
  watch: {},
  methods: {
    start: function () {
      this.state = "enabled";
    },
    stop: function () {
      this.state = "disabled";
    },
  },
  mounted() {},
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss"></style>
