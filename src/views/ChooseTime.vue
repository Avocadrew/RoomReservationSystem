<template>
  <div class="container container-flex container-flex-row container-wrap">
    <button
      class="button chooseTime-button"
      v-for="(time, index) in times"
      :key="index"
      :disabled="viewingMode"
      @click="testEvent"
    >
      {{ ("0" + time.startingTime.hours).slice(-2) }} :
      {{ ("0" + time.startingTime.minutes).slice(-2) }} ~
      {{ ("0" + time.endingTime.hours).slice(-2) }} :
      {{ ("0" + time.endingTime.minutes).slice(-2) }}
    </button>
  </div>
</template>

<script>
export default {
  name: "ChooseTime",
  data() {
    return {};
  },
  props: {
    params: Object,
  },
  computed: {
    times: function () {
      let t = [];
      let startingTime = {
        hours: this.$AVAILABLE_TIME.STARTING_HOURS,
        minutes: this.$AVAILABLE_TIME.STARTING_MINUTES,
      };
      let endingTime = {
        hours: this.$AVAILABLE_TIME.STARTING_HOURS,
        minutes: this.$AVAILABLE_TIME.STARTING_MINUTES,
      };
      let maxTime = {
        hours: this.$AVAILABLE_TIME.ENDING_HOURS,
        minutes: this.$AVAILABLE_TIME.ENDING_MINUTES,
      };
      let interval = this.$AVAILABLE_TIME.INTERVAL;

      endingTime.minutes += interval;
      while (endingTime.minutes >= 60) {
        endingTime.minutes -= 60;
        endingTime.hours++;
      }

      function isOutOfBound(time, maxTime) {
        if (time.hours == maxTime.hours) {
          if (time.minutes > maxTime.minutes) {
            return true;
          } else if (time.hours > maxTime.hours) {
            return true;
          }
        }
        return false;
      }

      while (!isOutOfBound(endingTime, maxTime)) {
        t.push({
          startingTime: { ...startingTime },
          endingTime: { ...endingTime },
        });

        startingTime.minutes += interval;
        while (startingTime.minutes >= 60) {
          startingTime.minutes -= 60;
          startingTime.hours++;
        }

        endingTime.minutes += interval;
        while (endingTime.minutes >= 60) {
          endingTime.minutes -= 60;
          endingTime.hours++;
        }
      }

      return t;
    },
    viewingMode: function () {
      return this.params.viewingMode;
    },
  },
  created() {},
  mounted() {
    for (let i = 0; i < this.times.length; i++) {
      console.log(i, this.times[i]);
    }
  },
  methods: {
    testEvent: function () {
      window.alert("HI");
    },
  },
};
</script>
