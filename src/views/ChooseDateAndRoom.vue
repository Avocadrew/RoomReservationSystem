<template>
  <div class="container container-flex container-flex-column">
    <v-select v-model="room" label="Room" :options="$ROOMS" />
    <Calendar @dayclick="chooseDate" :min-date="new Date()" />
  </div>
  <FloatingWindow
    :window="window"
    :params="paramsForChooseTime"
    ref="floatingWindow"
    :showDoneButton="!viewingMode"
    @done="done"
    @updateInfo="updateInfo"
  />
</template>

<script>
import FloatingWindow from "@/components/FloatingWindow.vue";

export default {
  name: "ChooseDateAndRoom",
  components: {
    FloatingWindow,
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
  mounted() {},
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
      if (day.day < new Date().getDate()) {
        return;
      }
      this.chosenDate = day;
      // Get one day reservation information.
      //this.generateTestData();
      //this.$refs.floatingWindow.openWindow();
			console.log("HI");
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
            this.$refs.floatingWindow.openWindow();
          } else {
            console.log("getDailyReservation failed");
          }
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
  },
};
</script>
