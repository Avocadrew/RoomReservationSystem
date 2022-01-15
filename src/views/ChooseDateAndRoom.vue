<template>
  <div class="container container-flex container-flex-column">
    <v-select v-model="room" label="Room" :options="$ROOMS" />
    <Calendar @dayclick="chooseDate" :min-date="new Date()" />
  </div>
  <div class="container container-flex container-flex-row">
    <button
      class="button secondary-button button-fixed-width-medium"
      @click="back()"
    >
      BACK
    </button>
  </div>
  <FloatingWindow
    :window="window"
    :params="paramsForChooseTime"
    ref="floatingWindow"
    :showDoneButton="!viewingMode"
    @done="done"
    @updateInfo="updateInfo"
  />
  <LoadingAnimation ref="loadingAnimation" />
</template>

<script>
import FloatingWindow from "@/components/FloatingWindow.vue";
import LoadingAnimation from "@/components/LoadingAnimation.vue";

export default {
  name: "ChooseDateAndRoom",
  components: {
    FloatingWindow,
    LoadingAnimation,
  },
  data() {
    return {
      room: "Room1",
      chosenDate: {},
      dailyReservation: {},
      selectedTime: [],
    };
  },
  computed: {
    window: function () {
      return {
        title: this.room + " on " + this.chosenDate.id,
        nextPath: "", // filloutmeetinginfo
      };
    },
    paramsForChooseTime: function () {
      return {
        viewingMode: this.viewingMode,
        dailyReservation: this.dailyReservation,
      };
    },
    account: function () {
      return this.$cookies.get("userID");
    },
    viewingMode: function () {
      if (this.account == undefined || this.account == "") {
        return true;
      } else {
        return false;
      }
    },
  },
  watch: {},
  created() {},
  mounted() {
    if (
      !this.$cookies.get("userID") ||
      this.$cookies.get("userID").length == 0
    ) {
      this.$router.push({ path: "landingpage" });
      return;
    }
  },
  methods: {
    generateTestData: function () {
      this.dailyReservation = {
        "9:00": true,
        "9:30": false,
        "10:00": true,
        "14:00": true,
        "15:00": true,
      };
    },
    chooseDate: function (day) {
      console.log(day.year, day.month, day.day);
      console.log(
        new Date().getYear(),
        new Date().getMonth() + 1,
        new Date().getDate()
      );
      if (day.year < new Date().getYear() + 1900) {
        return;
      } else if (day.year == new Date().getYear() + 1900) {
        if (day.month < new Date().getMonth() + 1) {
          return;
        } else if (day.month == new Date().getMonth() + 1) {
          if (day.day < new Date().getDate()) {
            return;
          }
        }
      }
      this.chosenDate = day;
      // Get one day reservation information.
      //this.generateTestData();
      //this.$refs.floatingWindow.openWindow();
      this.$refs.loadingAnimation.start();
      this.axios
        .post("https://ntustsers.xyz/api/getDailyReservation", {
          room_number: this.room,
          date:
            this.chosenDate.year +
            "-" +
            ("0" + this.chosenDate.month).slice(-2) +
            "-" +
            ("0" + this.chosenDate.day).slice(-2),
        })
        .then((response) => {
          if (response.data.success) {
            this.dailyReservation = response.data.dailyReservation;
            console.log(response.data);
            this.$refs.loadingAnimation.stop();
            this.$refs.floatingWindow.openWindow();
          } else {
            console.log("getDailyReservation failed");
          }
        })
        .catch((err) => {
          this.$refs.loadingAnimation.stop();
          window.alert(err + ". Please try again later. ");
        });
    },
    done: function () {
      //let roomString = this.room;
      //let chosenDateString = this.chosenDate.id;
      //let selectedTimeString = "";
      //for (let i = 0; i < this.selectedTime.length - 1; i++) {
      //	selectedTimeString += this.selectedTime[i] + "-";
      //}
      //if (this.selectedTime.length != 0) {
      //	selectedTimeString += this.selectedTime[this.selectedTime.length - 1];
      //}
      this.$router.push({
        name: "FillOutMeetingInfo",
        params: {
          room: this.room,
          chosenDate: this.chosenDate.id,
          selectedTime: this.selectedTime,
        },
      });
    },
    updateInfo: function (value) {
      this.selectedTime = value;
    },
    back: function () {
      this.$router.go(-1);
    },
  },
};
</script>
