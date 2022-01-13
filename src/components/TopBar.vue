<template>
  <div class="top-bar">
    <div
      class="
        container container-flex container-flex-row container-no-left-margin
      "
    >
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
      <img
        class="img-icon img-icon-google"
        :src="googleLogo"
        alt="Google-Logo"
      />
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
  <LoadingAnimation ref="loadingAnimation" />
</template>

<script>
import googleLogo from "@/assets/Google-icon-logo.svg";
import LoadingAnimation from "@/components/LoadingAnimation.vue";

export default {
  name: "TopBar",
  components: {
    LoadingAnimation,
  },
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
          path != "/main/chooseactions" &&
          path != "/main/landingpage" &&
          path != "/main/createaccount";
        let userID = this.$cookies.get("userID");
        this.haveLoggedIn = userID != undefined && userID != "";
      },
      immediate: true,
      deep: true,
    },
  },
  methods: {
    goToLandingPage: function () {
      this.$router.push({ path: "/main/landingpage" });
    },
    logIn: async function () {
      try {
        //const googleUser = await this.$gAuth.signIn();
        //if (!googleUser) {
        //  return null;
        //}
        //console.log("googleUser", googleUser);
        //this.user = googleUser.getBasicProfile().getEmail();
        //console.log("getId", this.user);
        //console.log("getBasicProfile", googleUser.getBasicProfile());
        //console.log("getAuthResponse", googleUser.getAuthResponse());
        //console.log(
        //  "getAuthResponse",
        //  this.$gAuth.instance.currentUser.get().getAuthResponse()
        //);

        const authCode = await this.$gAuth.getAuthCode();
        this.$refs.loadingAnimation.start();
        this.axios
          .post("https://ntustsers.xyz/api/signIn", {
            token: authCode,
          })
          .then((response) => {
            let success = response.data.success;
            if (success) {
              this.$cookies.set("userID", response.data.userInfo.user_ID);
              this.haveLoggedIn = true;
              this.$refs.loadingAnimation.stop();
              if (response.data.userInfo.is_registered == false) {
                this.$router.push({ path: "createaccount" });
              } else {
                this.$router.push({ path: "chooseactions" });
              }
            } else {
              console.log("signIn failed");
            }
          });

        // For testing
        //let account = "aabb9052@gmail.com";
        //console.log(account);
        //this.$cookies.set("userID", account);
        //this.haveLoggedIn = true;
        //this.$router.push({ path: "chooseactions" });
      } catch (error) {
        //on fail do something
        console.error(error);
        return null;
      }
    },
    logOut: async function () {
      try {
        //await this.$gAuth.signOut();
        this.$cookies.remove("userID");
        this.haveLoggedIn = false;
        this.$router.push({ path: "landingPage" });
      } catch (error) {
        console.error(error);
      }
    },
    goBack: function () {
      this.$router.go(-1);
    },
  },
  mounted() {
    this.haveLoggedIn =
      this.$cookies.get("userID") != undefined &&
      this.$cookies.get("userID") != "";
  },
  setup() {
    return {
      googleLogo,
    };
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
