<template>
  <div class="container container-flex container-flex-row container-wrap">
    <button
      class="button chooseTime-button"
      v-bind:class="{
        'chooseTime-button-occupied':
          params.dailyReservation[
            time.startingTime.hours +
              ':' +
              ('0' + time.startingTime.minutes).slice(-2)
          ],
        'chooseTime-button-empty':
          !params.dailyReservation[
            time.startingTime.hours +
              ':' +
              ('0' + time.startingTime.minutes).slice(-2)
          ],
        'chooseTime-button-selected':
          selectedTime.indexOf(
            time.startingTime.hours +
              ':' +
              ('0' + time.startingTime.minutes).slice(-2)
          ) > -1,
      }"
      v-for="(time, index) in times"
      :key="index"
      :disabled="viewingMode"
      @click="select(time)"
    >
      {{ time.startingTime.hours }} :
      {{ ("0" + time.startingTime.minutes).slice(-2) }} ~
      {{ time.endingTime.hours }} :
      {{ ("0" + time.endingTime.minutes).slice(-2) }}
    </button>
  </div>
</template>

<script>
export default {
  name: "ChooseTime",
  data() {
    return {
      selectedTime: [],
    };
  },
  props: {
    params: Object,
    isDone: Boolean,
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
  watch: {
    isDone: function (newValue) {
      if (newValue == true) {
        this.emit("updateInfo", this.selectedTime);
      }
    },
  },
  created() {},
  mounted() {},
  methods: {
    select: function (time) {
      let timeString =
        time.startingTime.hours +
        ":" +
        ("0" + time.startingTime.minutes).slice(-2);
      let index = this.selectedTime.indexOf(timeString);
      if (this.params.dailyReservation[timeString]) {
        window.alert("This time is reserved, please choose another time. ");
      } else if (index > -1) {
        this.selectedTime.splice(index, 1);
      } else {
        this.selectedTime.push(timeString);
      }
      this.$emit("updateInfo", this.selectedTime);
    },
  },
};
</script>
