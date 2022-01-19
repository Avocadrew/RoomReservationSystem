<template>
  <div class="container container-flex container-flex-column">
    <div class="container line-container">
      <p class="label">Repeats every:</p>
      <input type="number" name="name" />
      <v-select v-model="repeatUnit" label="Room" :options="$REPEAT_UNITS" />
    </div>
    <div class="container line-container">
      <p class="label">Date range:</p>
      <Datepicker v-model="date" range :enableTimePicker="false" />
    </div>
  </div>
</template>

<script>
export default {
  name: "ChooseMultiDateAndRoom",
  data() {
    return {
      repeatUnit: this.$REPEAT_UNITS[0],
      date: {},
    };
  },
  components: {},
  computed: {},
  created() {},
  mounted() {
    this.useDefaultValue();
  },
  watch: {},
  methods: {
    useDefaultValue: function () {
      const startDate = new Date();
      const endDate = new Date(new Date().setDate(startDate.getDate() + 7));
      this.date.value = [startDate, endDate];
    },
  },
};
</script>
