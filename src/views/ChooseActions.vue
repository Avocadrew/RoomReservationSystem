<template>
  <div class="container container-flex container-flex-column">
    <h3>Menu</h3>
    <div class="container container-flex container-flex-column">
      <button
        class="button primary-button button-fixed-width-big"
        @click="goToChooseTypes"
      >
        RESERVATION
      </button>
      <button
        class="button primary-button button-fixed-width-big"
        @click="testEvent"
      >
        RECORDS
      </button>
      <button
        class="button primary-button button-fixed-width-big"
        @click="testEvent"
      >
        PROFILE
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "ChooseActions",
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
    goToChooseTypes: function () {
      this.$router.push({ path: "reservation/choosetypes" });
    },
  },
};
</script>
