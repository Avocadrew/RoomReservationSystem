<template>
  <div class="container container-flex container-flex-column">
    <h3>Records</h3>
    <div class="container container-flex container-flex-column">
      <div class="container container-tab-buttons">
        <button
          class="button button-tab secondary-button"
          v-bind:class="{ 'button-disabled': currentTab == 'past' }"
          @click="switchTab('future')"
        >
          FUTURE
        </button>
        <button
          class="button button-tab secondary-button"
          v-bind:class="{ 'button-disabled': currentTab == 'future' }"
          @click="switchTab('past')"
        >
          PAST
        </button>
      </div>
      <div class="container container-tab-body">
        <div
          class="container line-container"
          v-for="(meeting, index) in presentedMeetings"
          :key="index"
        >
          <div
            class="
              container container-useless-wrapper container-fixed-width-small
            "
          >
            <p class="p-fixed-width">{{ meeting.name }}</p>
          </div>
          <button class="button icon-button" @click="modifyMeeting(index)">
            <mdicon name="pencil" :size="20" />
          </button>
          <button class="button icon-button" @click="deleteMeeting(index)">
            <mdicon name="delete" :size="20" />
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Records",
  data() {
    return {
      tempMeeting: {},
      presentedMeetings: [],
      futureMeetings: [],
      pastMeetings: [],
      currentTab: "future",
    };
  },
  components: {},
  computed: {},
  created() {},
  mounted() {
    // Fetch future and past meetings.
    this.axios
      .post("https://ntustsers.xyz/api/getAllReservations", {
        user_ID: this.$cookies.get("userID"),
      })
      .then((response) => {
        let success = response.data.success;
        console.log(response.data);
        if (success) {
          let reservations = response.data.allReservations;
          for (let i = 0; i < reservations.length; i++) {
            let meeting = {};
            meeting.id = reservations[i][0];
            meeting.name = reservations[i][1];
            meeting.description = reservations[i][2];
            this.futureMeetings.push(meeting);
          }
        } else {
          console.log("getAllReservations failed");
        }
      });
    //this.useDefaultValue();
    this.currentTab = "future";
  },
  watch: {
    currentTab: {
      handler: function (newValue) {
        if (newValue == "future") {
          this.presentedMeetings = this.futureMeetings;
        } else if (newValue == "past") {
          this.presentedMeetings = this.pastMeetings;
        } else {
          console.log("Error: Invalid tab " + newValue);
        }
      },
      immediate: true,
    },
  },
  methods: {
    testEvent: function () {
      window.alert("HI");
    },
    modifyMeeting: function (index) {
      this.$router.push({
        name: "FillOutMeetingInfo",
        params: { meetingID: this.presentedMeetings[index].id },
      });
    },
    deleteMeeting: function (index) {
      // Call api to delete a meeting.
      let meetingID = "";
      if (this.currentTab == "future") {
        meetingID = this.futureMeetings[index].id;
      } else {
        meetingID = this.pastMeetings[index].id;
      }
      this.axios
        .post("https://ntustsers.xyz/api/cancelReservation", {
          meeting_ID: meetingID,
        })
        .then((response) => {
          let success = response.data.success;
          if (success) {
            if (this.currentTab == "future") {
              this.futureMeetings.splice(index, 1);
            } else {
              this.pastMeetings.spice(index, 1);
            }
          } else {
            console.log("cancelReservation failed");
          }
        });
      window.alert("Delete meeting " + index.toString());
    },
    switchTab: function (tab) {
      this.currentTab = tab;
    },
    useDefaultValue: function () {
      let meeting = {};
      meeting.id = "meeting1";
      meeting.name = "Financial Meeting";
      meeting.date = "Nov 7th, 2021";
      meeting.time = "13:00 ~ 14:30";
      meeting.room = "Room1";
      meeting.description =
        "Group 06 will discuss for the system of the game. ";
      meeting.groupID = "id1";
      this.futureMeetings.push({ ...meeting });
      meeting.id = "meeting2";
      meeting.name = "Project Meeting";
      meeting.date = "Nov 7th, 2021";
      meeting.time = "13:00 ~ 14:30";
      meeting.room = "Room1";
      meeting.description =
        "Group 06 will discuss for the system of the game. ";
      meeting.groupID = "id1";
      this.futureMeetings.push({ ...meeting });
      meeting.id = "meeting3";
      meeting.name = "New Meeting";
      meeting.date = "Nov 7th, 2021";
      meeting.time = "13:00 ~ 14:30";
      meeting.room = "Room1";
      meeting.description =
        "Group 06 will discuss for the system of the game. ";
      meeting.groupID = "id2";
      this.pastMeetings.push({ ...meeting });
    },
  },
};
</script>
