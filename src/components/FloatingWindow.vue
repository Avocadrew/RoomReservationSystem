<template>
  <div class="container floating-container" v-if="isShown">
    <div class="floating-container-header">
      <h3>{{ window.title }}</h3>
      <button class="button icon-button" @click="closeWindow">X</button>
    </div>
    <router-view />
    <div class="floating-container-footer">
      <div></div>
      <div>
        <button
          class="button primary-button button-fixed-width-medium"
          @click="done"
        >
          DONE
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "FloatingWindow",
  data() {
    return {
      isShown: false,
    };
  },
  props: {
    window: Object,
  },
  methods: {
    openWindow: function () {
      this.isShown = true;
    },
    closeWindow: function () {
      this.isShown = false;
    },
    done: function () {
      this.$router.push(this.window.nextPath);
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss"></style>
