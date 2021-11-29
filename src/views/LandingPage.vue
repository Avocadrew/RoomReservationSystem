<template>

  <div class="container container-flex container-flex-column">
    <h1>Easier, Quickier, Better</h1>
    <h4>Simplest Meeting Room Reservation System Ever</h4>

     <div class="container container-flex container-flex-row">
      <button
        class="button secondary-button button-fixed-width-medium"
        @click="testEvent"
      >
        GUEST
      </button>

      <button
        class="button primary-button button-fixed-width-medium"
        @click="testEvent"
      >
        LOGIN
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "LandingPage",
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
