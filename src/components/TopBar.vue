<template>
  <div class="top-bar">
    <div class="container container-flex container-flex-row container-no-left-margin">
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
			<img class="img-icon img-icon-google" :src="googleLogo" alt="Google-Logo" /> LOG IN 
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
import googleLogo from "@/assets/Google-icon-logo.svg";

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
				let userId = this.$cookies.get("userId");
				this.haveLoggedIn = (userId != undefined) && (userId != "");
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
				this.axios.post("https://ntustsers.xyz/api/signIn", {
					token: authCode, 
				})
				.then((response) => {
					console.log(response.data.id_token.email);
					this.$cookies.set("userId", response.data.id_token.email);
					this.haveLoggedIn = true;
					this.$router.push({ path: "chooseactions" });
				});

      } catch (error) {
        //on fail do something
        console.error(error);
        return null;
      }
    },
    logOut: async function () {
			try {
				//await this.$gAuth.signOut();
				this.$cookies.remove("userId");
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
      this.$cookies.get("userId") != undefined &&
      this.$cookies.get("userId") != "";
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
