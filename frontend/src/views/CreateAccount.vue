<template>
  <div class="container container-flex container-flex-column">
    <h2>Personal Information</h2>

    <div class="container line-container">
      <p class="label">Name:</p>
      <input type="text" name="name" v-model="profile.name" />
    </div>

    <div class="container line-container">
      <p class="label">Gender:</p>
      <input
        type="radio"
        id="male"
        name="gender"
        value="Male"
        checked
        v-model="profile.gender"
      />
      <label for="male">Male</label>
      <input
        type="radio"
        id="female"
        name="gender"
        value="Female"
        v-model="profile.gender"
      />
      <label for="female">Female</label>
    </div>

    <div class="container line-container">
      <p class="label">Email:</p>
      <p>{{ profile.email }}</p>
    </div>

    <div class="container line-container">
      <p class="label">Occupation:</p>
      <input type="text" name="occupation" v-model="profile.occupation" />
    </div>

    <div class="container line-container">
      <p class="label">Phone Number:</p>
      <input
        type="tel"
        name="phone"
        pattern="09[0-9]{8}"
        v-model="profile.phoneNumber"
      />
    </div>

    <div>
      <button
        class="button primary-button button-fixed-width-medium"
        @click="createAccount"
      >
        CREATE
      </button>
    </div>
  </div>
  <LoadingAnimation ref="loadingAnimation" />
</template>

<script>
import LoadingAnimation from "@/components/LoadingAnimation.vue";

export default {
  name: "CreateAccount",
  components: {
    LoadingAnimation,
  },
  data() {
    return {
      profile: {
        name: "",
        gender: "Male",
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
    this.profile.email = this.$cookies.get("userID");
  },
  methods: {
    checkPersonalInformationValidation: function () {
      if (!this.profile.name || this.profile.name.length == 0) {
        let message = "Your name can't be emtpy. Please fill in your name. ";
        return { success: false, message: message };
      }
      if (!this.profile.occupation || this.profile.occupation.length == 0) {
        let message =
          "Your occupation can't be emtpy. Please fill in your occupation. ";
        return { success: false, message: message };
      }
      if (!this.profile.gender) {
        let message = "Please select a gender. ";
        return { success: false, message: message };
      }
      if (!this.profile.phoneNumber || this.profile.phoneNumber.length == 0) {
        let message =
          "Your phone number can't be emtpy. Please fill in your phone number. ";
        return { success: false, message: message };
      }
      return { success: true, message: "" };
    },
    createAccount: function () {
      this.$refs.loadingAnimation.start();
      let validation = this.checkPersonalInformationValidation();
      if (!validation.success) {
        this.$refs.loadingAnimation.stop();
        window.alert(validation.message);
        return;
      }
      this.axios
        .post("https://ntustsers.xyz/api/saveDetailedUserInformation", {
          UserID: this.profile.email,
          gender: this.profile.gender,
          name: this.profile.name,
          jobTitle: this.profile.occupation,
          phone: this.profile.phoneNumber,
        })
        .then((response) => {
          let success = response.data.success;
          if (success) {
            this.$refs.loadingAnimation.stop();
            this.$router.push({ path: "chooseactions" });
          } else {
            console.log("saveDetailedUserInformation failed");
          }
        })
        .catch((err) => {
          this.$refs.loadingAnimation.stop();
          window.alert(err + ". Please try again later. ");
        });
    },
  },
};
</script>
