<template>
  <div class="container container-flex container-flex-column">
    <h1>Easier, Quickier, Better</h1>
    <h4>Simplest Meeting Room Reservation System Ever</h4>

    <div class="container container-flex container-flex-row">
      <button
        class="button secondary-button button-fixed-width-medium"
        @click="goToGuest"
      >
        GUEST
      </button>

      <button
        class="button primary-button button-fixed-width-medium"
        @click="logIn"
      >
        LOG IN
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
  created() {
    let account = this.$cookies.get("account");
    if (account != undefined && account != "") {
      this.$router.push("chooseactions");
    }
  },
  mounted() {},
  methods: {
    logIn: function () {
      this.$cookies.set("account", "testAccount");
      this.$router.push({ path: "chooseactions" });
      this.$router.go(); // Refreshing the page to make the TopBar refresh, so the button in it can refreshes.
    },
    goToChooseTypes: function () {
      this.$router.push({ path: "reservation/choosetypes" });
    },
    goToGuest: function () {
      this.$router.push({ path: "single" });
    },
  },
};
</script>
