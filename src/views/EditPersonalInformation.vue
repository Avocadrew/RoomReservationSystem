<template>
    <div class="container container-flex container-flex-column">
      <h3>Edit Personal Information</h3>
      
      <div class="container line-container">
        <p class="label">Name:</p>
        <input type="text" name="name" />
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
        <input type="text" name="occupation" />
      </div>

      <div class="container line-container">
        <p class="label">Phone Number:</p>
        <input type="tel" name="phone" pattern="09[0-9]{8}" />
      </div>

      <div class="container container-flex container-flex-row">
        <button
          class="button secondary-button button-fixed-width-medium"
          @click="testEvent"
        >
          CANCEL
        </button>
        <button
          class="button primary-button button-fixed-width-medium"
          @click="testEvent"
        >
          CONFIRM
        </button>
      </div>
    </div>
  </template>
  
  <script>
 export default {
  name: "EditPersonalInformation",
  data() {
    return {
      profile: {
        name: "",
        gender: "",
        email: "",
        occupation: "",
        phonenumber: "",
      },
    };
  },
  components: {},
  computed: {
  },
  created() {},
  mounted() {
    this.useDefaultValue();
    console.log(this.profile.name);
  },
  methods: {
    useDefaultValue: function () {
      this.profile.name = "";
      this.profile.gender = "Male";
      this.profile.email = "willy123456@gmail.com";
      this.profile.occupation = "";
      this.profile.phonenumber ="";
    },
    testEvent: function () {
      window.alert("HI");
    },
  },
};
  </script>
  