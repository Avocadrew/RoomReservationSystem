<template>
  <div class="container container-flex container-flex-column">
    <h3>Personal Information</h3>
    <div class="container line-container">
      <p class="label">Name:</p>
      <input type="text" name="name" />
    </div>
    <div class="container line-container">
      <p class="label">Gender:</p>
      <input type="radio" id="male" name="gender" value="Male" checked />
      <label for="male">Male</label>
      <input type="radio" id="female" name="gender" value="Female" />
      <label for="female">Female</label>
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
        CREATE
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "CreateAccount",
  data() {
    return {};
  },
  components: {},
  computed: {},
  created() {},
  mounted() {},
  methods: {
    testEvent: function () {
      window.alert("HI");
    },
  },
};
</script>
