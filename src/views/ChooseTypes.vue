<template>
  <div class="container container-flex container-flex-column">
    <h3>Menu</h3>
    <div class="container container-flex container-flex-column">
      <button
        class="button primary-button button-fixed-width-big"
        @click="testEvent"
      >
        SINGLE
      </button>
      <button
        class="button primary-button button-fixed-width-big"
        @click="goToChooseDateAndRoom"
      >
        MULTIPLE
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "ChooseTypes",
  data() {
    return {};
  },
  components: {},
  computed: {},
  created() {},
  mounted() {},
  methods: {
    testEvent: function () {
      window.alert("HI");
    },
    goToChooseDateAndRoom: function () {
      this.$router.push({ path: "multiple" });
    },
  },
};
</script>
