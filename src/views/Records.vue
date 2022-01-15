<template>
  <div class="container container-flex container-flex-column">
    <h2>Records</h2>
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
      <div
        class="container container-tab-body"
        v-if="presentedMeetings.length != 0"
      >
        <div
          class="container container-useless-wrapper"
          v-for="(meeting, index) in presentedMeetings"
          :key="index"
        >
          <div class="container line-container">
            <div
              class="
                container container-useless-wrapper container-fixed-width-small
              "
            >
              <p>{{ meeting.name }}</p>
            </div>
            <div
              class="
                container
                container-flex
                container-useless-wrapper
                container-fixed-width-tiny
              "
            >
              <button
                class="button icon-button"
                @click="modifyMeeting(index)"
                v-if="currentTab == 'future'"
              >
                <mdicon name="pencil" :size="20" />
              </button>
              <button
                class="button icon-button"
                @click="inspectMeeting(index)"
                v-else
              >
                <mdicon name="magnify" :size="20" />
              </button>
              <button class="button icon-button" @click="deleteMeeting(index)">
                <mdicon name="delete" :size="20" />
              </button>
            </div>
          </div>
          <hr v-show="index != presentedMeetings.length - 1" />
        </div>
      </div>
      <div class="container container-tab-body" v-else>
        <div class="container line-container">
          <div
            class="
              container container-useless-wrapper container-fixed-width-small
            "
          >
            <p>None</p>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="container container-flex container-flex-row">
    <button
      class="button secondary-button button-fixed-width-medium"
      @click="back()"
    >
      BACK
    </button>
  </div>
  <LoadingAnimation ref="loadingAnimation" />
</template>

<script>
import LoadingAnimation from "@/components/LoadingAnimation.vue";

export default {
  name: "Records",
  components: {
    LoadingAnimation,
  },
  data() {
    return {
      tempMeeting: {},
      presentedMeetings: [],
      futureMeetings: [],
      pastMeetings: [],
      currentTab: "future",
    };
  },
  computed: {},
  created() {},
  mounted() {
    // Fetch future and past meetings.
    this.$refs.loadingAnimation.start();
    console.log(this.$cookies.get("userID"));
    this.axios
      .post("https://ntustsers.xyz/api/getAllReservations", {
        user_ID: this.$cookies.get("userID"),
      })
      .then((response) => {
        console.log(response);
        let success = response.data.success;
        if (success) {
          let reservations = response.data.allReservations;
          let futureReservations = reservations.reservation_future;
          let pastReservations = reservations.reservation_past;
          for (let i = 0; i < futureReservations.length; i++) {
            let meeting = {};
            meeting.id = futureReservations[i][0];
            meeting.name = futureReservations[i][1];
            meeting.description = futureReservations[i][2];
            this.futureMeetings.push(meeting);
          }
          for (let i = 0; i < pastReservations.length; i++) {
            let meeting = {};
            meeting.id = pastReservations[i][0];
            meeting.name = pastReservations[i][1];
            meeting.description = pastReservations[i][2];
            this.pastMeetings.push(meeting);
          }
          this.$refs.loadingAnimation.stop();
        } else {
          console.log("getAllReservations failed");
        }
      })
      .catch((err) => {
        this.$refs.loadingAnimation.stop();
        window.alert(err + ". Please try again later. ");
        this.$router.go(-1);
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
        params: { meetingID: this.presentedMeetings[index].id, mode: "edit" },
      });
    },
    inspectMeeting: function (index) {
      this.$router.push({
        name: "FillOutMeetingInfo",
        params: {
          meetingID: this.presentedMeetings[index].id,
          mode: "inspect",
        },
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
      this.$refs.loadingAnimation.start();
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
            this.$refs.loadingAnimation.stop();
          } else {
            console.log("cancelReservation failed");
            console.log("Error: ", response.data.error);
          }
        })
        .catch((err) => {
          this.$refs.loadingAnimation.stop();
          window.alert(err + ". Please try again later. ");
        });
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
    back: function () {
      this.$router.go(-1);
    },
  },
};
</script>
