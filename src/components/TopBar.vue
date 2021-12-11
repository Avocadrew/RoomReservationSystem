<template>
  <div class="top-bar">
    <div class="container container-flex-row container-no-left-margin">
      <button
        class="button icon-button"
        @click="goBack"
        v-show="showBackButton"
      >
        <mdicon class="mdicon-white" name="arrow-left" />
      </button>
      <button class="button button-title" @click="goToLandingPage">
        Reservation System
      </button>
    </div>
    <button
      class="button primary-button button-fixed-width-medium"
      @click="logIn"
      v-if="!haveLoggedIn"
    >
      LOG IN
    </button>
    <button
      class="button primary-button button-fixed-width-medium"
      @click="logOut"
      v-else
    >
      LOG OUT
    </button>
  </div>
</template>

<script>
export default {
  name: "TopBar",
  data: function () {
    return {
      showBackButton: Boolean,
      haveLoggedIn: false,
    };
  },
  props: {
    msg: String,
  },
  watch: {
    $router: {
      handler: function (newValue) {
        let path = newValue.currentRoute._rawValue.path.toLowerCase();
        this.showBackButton =
          path != "/main/chooseactions" && path != "/main/landingpage";
      },
      immediate: true,
      deep: true,
    },
  },
  methods: {
    goToLandingPage: function () {
      this.$router.push({ path: "/main/landingpage" });
    },
    logIn: function () {
      this.$cookies.set("account", "testAccount");
      this.haveLoggedIn = true;
      this.$router.push({ path: "chooseactions" });
    },
    logOut: function () {
      this.$cookies.remove("account");
      this.haveLoggedIn = false;
      this.$router.push({ path: "landingPage" });
    },
    goBack: function () {
      this.$router.go(-1);
    },
  },
  mounted() {
    this.haveLoggedIn =
      this.$cookies.get("account") != undefined &&
      this.$cookies.get("account") != "";
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
//.fade-enter-active, .fade-leave-active {
//	transition: opacity .5s;
//}
//.fade-enter-from, .fade-leave-to {
//	opacity: 0;
//}
//.fade-enter-to, .fade-leave-from {
//	opacity: 1;
//}
//.fade-move {
//	transition: all 0.8s ease;
//}
</style>
