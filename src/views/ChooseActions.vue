<template>
  <div class="container container-flex container-flex-column">
    <h2>Menu</h2>
    <div class="container container-flex container-flex-column">
      <button
        class="button primary-button button-fixed-width-big"
        @click="goToSingle"
      >
        RESERVATION
      </button>
      <button
        class="button primary-button button-fixed-width-big"
        @click="goToRecords"
      >
        RECORDS
      </button>
      <button
        class="button primary-button button-fixed-width-big"
        @click="goToPersonalInformation"
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
    // goToChooseTypes is useless now.
    goToChooseTypes: function () {
      this.$router.push({ path: "choosetypes" });
    },
    goToSingle: function () {
      this.$router.push({ path: "single" });
    },
    goToRecords: function () {
      this.$router.push({ path: "records" });
    },
    goToPersonalInformation: function () {
      this.$router.push({ path: "personalinformation" });
    },
  },
};
</script>
