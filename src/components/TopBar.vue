<template>
  <div class="top-bar">
    <div>
      <button class="button button-title" @click="testEvent">
        Reservation System
      </button>
    </div>
    <div></div>
  </div>
</template>

<script>
export default {
  name: "TopBar",
  props: {
    msg: String,
  },
  methods: {
    testEvent: function () {
      window.alert("HI");
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss"></style>
