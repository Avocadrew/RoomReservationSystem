<template>
  <div class="container container-flex container-flex-column">
    <h2>Personal Information</h2>

    <div class="container line-container">
      <p class="label">Name:</p>
      <input type="text" name="name" v-model="profile.name" />
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

    <div class="container container-flex container-flex-row">
      <button
        class="button secondary-button button-fixed-width-medium"
        @click="cancel"
      >
        CANCEL
      </button>
      <button
        class="button primary-button button-fixed-width-medium"
        @click="confirm"
      >
        CONFIRM
      </button>
    </div>
  </div>
  <LoadingAnimation ref="loadingAnimation" />
</template>

<script>
import LoadingAnimation from "@/components/LoadingAnimation.vue";

export default {
  name: "EditPersonalInformation",
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
      });
    console.log(this.profile.name);
  },
  methods: {
    useDefaultValue: function () {
      this.profile.name = "";
      this.profile.gender = "Male";
      this.profile.email = "willy123456@gmail.com";
      this.profile.occupation = "";
      this.profile.phoneNumber = "";
    },
    cancel: function () {
      this.$router.go(-1);
    },
    confirm: function () {
      this.$refs.loadingAnimation.start();
      this.axios
        .post("https://ntustsers.xyz/api/saveDetailedUserInformation", {
          UserID: this.$cookies.get("userID"),
          gender: this.profile.gender,
          name: this.profile.name,
          jobTitle: this.profile.occupation,
          phone: this.profile.phoneNumber,
        })
        .then((response) => {
          let success = response.data.success;
          if (success) {
            this.$router.go(-1);
            this.$refs.loadingAnimation.stop();
          } else {
            console.log("saveDetailedUserInformation failed");
          }
        });
    },
  },
};
</script>
