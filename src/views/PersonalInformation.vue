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
      <p>{{ profile.phonenumber }}</p>
    </div>

    <div class="container container-flex container-flex-row">
      <button
        class="button primary-button button-fixed-width-medium"
        @click="testEvent"
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
      this.profile.name = "Wei Chen";
      this.profile.gender = "Male";
      this.profile.email = "willy123456@gmail.com";
      this.profile.occupation = "Student";
      this.profile.phonenumber ="0912-345678";
    },
    testEvent: function () {
      window.alert("HI");
    },
  },
};
</script>
