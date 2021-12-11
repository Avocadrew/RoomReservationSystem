<template>
  <div class="container floating-container" v-if="isShown">
    <div class="floating-container-header">
      <h3>{{ window.title }}</h3>
      <button class="button icon-button" @click="closeWindow">X</button>
    </div>
    <router-view :params="params" :isDone="isDone" @params="emitNewParams" />
    <div class="floating-container-footer">
      <div></div>
      <div>
        <button
          class="button primary-button button-fixed-width-medium"
          @click="done"
          v-show="showDoneButton"
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
      isDone: false,
    };
  },
  props: {
    window: Object,
    params: Object,
    showDoneButton: {
      type: Boolean,
      default: true,
    },
  },
  methods: {
    openWindow: function () {
      this.isShown = true;
    },
    closeWindow: function () {
      this.isShown = false;
    },
    done: function () {
      this.closeWindow();
      if (this.window.nextPath && this.window.nextPath.length != 0) {
        this.$router.push(this.window.nextPath);
      }
      this.isDone = true;
      this.$emit("done", true);
    },
    emitNewParams: function (value) {
      this.$emit("params", value);
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss"></style>
