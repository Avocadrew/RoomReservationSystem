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
				<img class="img-icon img-icon-google" :src="googleLogo" alt="Google-Logo" /> LOG IN 
      </button>
    </div>
  </div>
</template>

<script>
import googleLogo from "@/assets/Google-icon-logo.svg";

export default {
  name: "LandingPage",
  data() {
    return {};
  },
  components: {},
  computed: {},
  created() {
    let account = this.$cookies.get("userId");
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
    goToChooseTypes: function () {
      this.$router.push({ path: "reservation/choosetypes" });
    },
    goToGuest: function () {
			this.$cookies.set("userId", "testAccount");
			window.alert(this.$cookies.get("userId"));
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
