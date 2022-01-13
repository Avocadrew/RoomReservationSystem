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
        <img
          class="img-icon img-icon-google"
          :src="googleLogo"
          alt="Google-Logo"
        />
        LOG IN
      </button>
    </div>
  </div>
  <LoadingAnimation ref="loadingAnimation" />
</template>

<script>
import googleLogo from "@/assets/Google-icon-logo.svg";
import LoadingAnimation from "@/components/LoadingAnimation.vue";

export default {
  name: "LandingPage",
  components: {
    LoadingAnimation,
  },
  data() {
    return {};
  },
  computed: {},
  created() {
    let account = this.$cookies.get("userID");
    if (account != undefined && account != "") {
      this.$router.push("chooseactions");
    }
  },
  mounted() {},
  methods: {
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
              window.alert("SignIn failed, please try again later. ");
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
    goToChooseTypes: function () {
      this.$router.push({ path: "reservation/choosetypes" });
    },
    goToGuest: function () {
      this.$router.push({ path: "single" });
    },
  },
  setup() {
    return {
      googleLogo,
    };
  },
};
</script>
