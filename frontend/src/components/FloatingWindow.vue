<template>
  <transition name="pop-up">
    <div class="container floating-container" v-if="isShown">
      <div class="floating-container-header">
        <h3>{{ window.title }}</h3>
        <button class="button icon-button" @click="closeWindow">X</button>
      </div>
      <div class="floating-container-body">
        <router-view
          :params="params"
          :isDone="isDone"
          @updateInfo="emitNewInfo"
        />
      </div>
      <div class="floating-container-footer">
        <button
          class="button primary-button button-fixed-width-medium"
          @click="done"
          v-show="showDoneButton"
        >
          DONE
        </button>
        <button
          class="button primary-button button-fixed-width-medium"
          @click="close"
          v-show="!showDoneButton"
        >
          CLOSE
        </button>
      </div>
    </div>
  </transition>
  <transition name="fade">
    <div
      class="container container-useless-wrapper container-gray-background"
      v-if="isShown"
      @click="closeWindow"
    ></div>
  </transition>
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
  mounted() {},
  methods: {
    openWindow: function () {
      this.isShown = true;
    },
    closeWindow: function () {
      this.isShown = false;
    },
    done: function () {
      this.closeWindow();
      this.isDone = true;
      this.$emit("done");
      if (this.window.nextPath && this.window.nextPath.length != 0) {
        this.$router.push(this.window.nextPath);
      }
    },
    emitNewInfo: function (value) {
      this.$emit("updateInfo", value);
    },
    close: function () {
      this.closeWindow();
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss"></style>
