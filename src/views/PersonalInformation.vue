<template>
  <div class="container container-flex container-flex-column">
    <h2>Personal Information</h2>

    <div class="container line-container">
      <p class="label">Name:</p>
      <p>{{ profile.name }}</p>
    </div>

    <div class="container line-container">
      <p class="label">Gender:</p>
      <p>{{ profile.gender }}</p>
    </div>

    <div class="container line-container">
      <p class="label">Email:</p>
      <p>{{ profile.email }}</p>
    </div>

    <div class="container line-container">
      <p class="label">Occupation:</p>
      <p>{{ profile.occupation }}</p>
    </div>

    <div class="container line-container">
      <p class="label">Phone Number:</p>
      <p>{{ profile.phoneNumber }}</p>
    </div>

    <div class="container container-flex container-flex-row">
      <button
        class="button secondary-button button-fixed-width-medium"
        @click="back"
      >
        BACK
      </button>
      <button
        class="button primary-button button-fixed-width-medium"
        @click="goToEditPersonalInformation"
      >
        EDIT
      </button>
    </div>
  </div>
  <LoadingAnimation ref="loadingAnimation" />
</template>

<script>
import LoadingAnimation from "@/components/LoadingAnimation.vue";

export default {
  name: "PersonalInformation",
  components: {
    LoadingAnimation,
  },
  data() {
    return {
      profile: {
        name: "",
        gender: "",
        email: "",
        occupation: "",
        phoneNumber: "",
      },
    };
  },
  computed: {},
  created() {},
  mounted() {
    if (
      !this.$cookies.get("userID") ||
      this.$cookies.get("userID").length == 0
    ) {
      this.$router.push({ path: "landingpage" });
      return;
    }

    //this.useDefaultValue();
    this.$refs.loadingAnimation.start();
    this.axios
      .post("https://ntustsers.xyz/api/getDetailedUserInformation", {
        UserID: this.$cookies.get("userID"),
      })
      .then((response) => {
        let success = response.data.success;
        if (success) {
          let profile = response.data.detailedUserInformation;
          this.profile.email = profile[0];
          this.profile.gender = profile[1];
          this.profile.name = profile[2];
          this.profile.occupation = profile[3];
          this.profile.phoneNumber = profile[4];
          this.$refs.loadingAnimation.stop();
        } else {
          console.log("getDetailedUserInformation failed");
        }
      })
      .catch((err) => {
        this.$refs.loadingAnimation.stop();
        window.alert("Error: " + err + ". Please try again later. ");
        this.$router.go(-1);
      });
  },
  methods: {
    useDefaultValue: function () {
      this.profile.name = "Wei Chen";
      this.profile.gender = "Male";
      this.profile.email = "willy123456@gmail.com";
      this.profile.occupation = "Student";
      this.profile.phoneNumber = "0912-345678";
    },
    goToEditPersonalInformation: function () {
      this.$router.push({ path: "editpersonalinformation" });
    },
    back: function () {
      this.$router.go(-1);
    },
  },
};
</script>
