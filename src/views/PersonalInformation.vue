<template>
  <div class="container container-flex container-flex-column">
    <h3>Personal Information</h3>

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
        class="button primary-button button-fixed-width-medium"
        @click="goToEditPersonalInformation"
      >
        EDIT
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "PersonalInformation",
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
  components: {},
  computed: {},
  created() {},
  mounted() {
    //this.useDefaultValue();
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
        } else {
          console.log("getDetailedUserInformation failed");
        }
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
  },
};
</script>
