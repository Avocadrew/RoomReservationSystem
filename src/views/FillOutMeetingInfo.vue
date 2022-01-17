<template>
  <div class="container container-flex container-flex-column">
    <div class="container line-container" v-if="mode != 'inspect'">
      <p class="label">Meeting Name:</p>
      <input type="text" name="name" v-model="meeting.name" />
    </div>
    <div class="container line-container" v-else>
      <p class="label">Meeting Name:</p>
      <p>{{ meeting.name }}</p>
    </div>
    <div class="container line-container">
      <p class="label">Date:</p>
      <p>{{ meeting.date }}</p>
    </div>
    <div class="container line-container">
      <p class="label">Time:</p>
      <p>{{ meeting.timeString }}</p>
    </div>
    <div class="container line-container">
      <p class="label">Room:</p>
      <p>{{ meeting.room }}</p>
    </div>
    <div class="container area-container" v-if="mode != 'inspect'">
      <div class="container line-container">
        <p class="label">Group:</p>
        <button class="button primary-button sub-button" @click="createAGroup">
          Create a Group
        </button>
      </div>
      <div
        class="container container-useless-wrapper"
        v-if="groups.length != 0"
      >
        <div
          class="container line-container"
          v-for="(group, index) in groups"
          :key="index"
        >
          <input
            type="radio"
            name="group"
            :value="group.id"
            v-model="meeting.groupID"
          />
          <label :for="index">{{ group.name }}</label>
          <button class="button icon-button" @click="modifyGroup(index)">
            <mdicon name="pencil" :size="20" />
          </button>
          <button class="button icon-button" @click="deleteGroup(index)">
            <mdicon name="delete" :size="20" />
          </button>
        </div>
      </div>
      <div class="container line-container" v-else>
        <p>You don't have any group yet, please create a new group.</p>
      </div>
    </div>
    <div class="container line-container" v-else>
      <p class="label">Group:</p>
      <p>{{ meeting.groupName }}</p>
      <button
        class="button icon-button"
        @click="inspectGroup()"
        v-show="!theGroupIsDeleted"
      >
        <mdicon name="magnify" :size="20" />
      </button>
    </div>
    <div class="container area-container" v-if="mode != 'inspect'">
      <p class="label">Description:</p>
      <textarea name="description" v-model="meeting.description" />
    </div>
    <div class="container area-container" v-else>
      <p class="label">Description:</p>
      <textarea name="description" v-model="meeting.description" readonly />
    </div>
    <div class="container container-flex container-flex-row">
      <button
        class="button secondary-button button-fixed-width-medium"
        @click="back()"
        v-show="mode != 'edit'"
      >
        BACK
      </button>
      <button
        class="button primary-button button-fixed-width-medium"
        @click="reserve()"
        v-show="mode == 'reserve'"
      >
        RESERVE
      </button>
      <button
        class="button secondary-button button-fixed-width-medium"
        @click="cancel()"
        v-show="mode == 'edit'"
      >
        CANCEL
      </button>
      <button
        class="button primary-button button-fixed-width-medium"
        @click="save()"
        v-show="mode == 'edit'"
      >
        SAVE
      </button>
    </div>
  </div>
  <FloatingWindow
    :window="window"
    :params="tempGroup"
    ref="floatingWindow"
    @done="saveGroup"
    @updateInfo="updateTempGroup"
  />
  <LoadingAnimation ref="loadingAnimation" />
</template>

<script>
import FloatingWindow from "@/components/FloatingWindow.vue";
import LoadingAnimation from "@/components/LoadingAnimation.vue";

export default {
  name: "FillOutMeetingInfo",
  components: {
    FloatingWindow,
    LoadingAnimation,
  },
  data() {
    return {
      mode: "reserve",
      theGroupIsDeleted: false,
      meeting: {
        name: "",
        date: "",
        time: "",
        room: "",
        description: "",
        groupID: "",
        groupName: "",
      },
      groups: [
        //{
        //  id: "id1",
        //  name: "Group1",
        //  members: ["abc@gmail.com", "haha@gmail.com"],
        //},
        //{
        //  id: "id2",
        //  name: "Group2",
        //  members: ["def@gmail.com", "hello@gmail.com"],
        //},
      ],
      window: {
        title: "Create a Group",
      },
      tempGroup: {
        id: "",
        name: "testGroup",
        members: ["hello@gmail.com", "hi@gmail.com"],
        readonly: false,
      },
    };
  },
  computed: {
    meetingGroup: function () {
      let group = {};
      if (this.meeting.groupID) {
        // Get group information
        group.name = "Group1";
        group.members = ["A", "B"];
      }
      return group;
    },
  },
  created() {},
  mounted() {
    if (
      !this.$cookies.get("userID") ||
      this.$cookies.get("userID").length == 0
    ) {
      this.$router.push({ path: "landingpage" });
      return;
    }
    let times = this.getTimesString();
    if (this.$route.params.meetingID) {
      // Fetch the meeting.
      this.$refs.loadingAnimation.start();
      this.axios
        .post("https://ntustsers.xyz/api/checkReservation", {
          meeting_ID: this.$route.params.meetingID,
        })
        .then((response) => {
          let success = response.data.success;
          if (success) {
            let reservation = response.data.reservation;
            this.meeting.id = this.$route.params.meetingID;
            this.meeting.name = reservation.title;
            let startingTimeIndex = -1;
            let endingTimeIndex = -1;
            for (let i = 0; i < times.length; i++) {
              for (let j = 0; j < reservation.time.length; j++) {
                if (times[i].startingTime == reservation.time[j]) {
                  startingTimeIndex = i;
                  break;
                }
              }
              if (startingTimeIndex != -1) {
                break;
              }
            }
            for (let i = times.length - 1; i >= 0; i--) {
              for (let j = 0; j < reservation.time.length; j++) {
                if (times[i].startingTime == reservation.time[j]) {
                  endingTimeIndex = i;
                  break;
                }
              }
              if (endingTimeIndex != -1) {
                break;
              }
            }
            this.meeting.time = reservation.time;
            this.meeting.timeString =
              times[startingTimeIndex].startingTime +
              " ~ " +
              times[endingTimeIndex].endingTime;
            this.meeting.date = reservation.date;
            this.meeting.description = reservation.description;
            this.meeting.room = reservation["room number"];
            this.meeting.groupID = reservation.group_ID;
            this.meeting.groupName = "<deleted>";

            // Fetch groups
            this.axios
              .post("https://ntustsers.xyz/api/getGroupList", {
                userID: this.$cookies.get("userID"),
              })
              .then((response) => {
                let success = response.data.success;
                if (success) {
                  let groups = response.data.groupList;
                  if (groups) {
                    this.theGroupIsDeleted = true;
                    for (let i = 0; i < groups.length; i++) {
                      this.groups.push({
                        id: groups[i].groupID,
                        name: groups[i].GroupName,
                        members: groups[i].emails,
                      });
                      console.log(groups[i].groupID, this.meeting.groupID);
                      if (groups[i].groupID == this.meeting.groupID) {
                        this.meeting.groupName = groups[i].GroupName;
                        this.meeting.groupID = groups[i].groupID;
                        this.theGroupIsDeleted = false;
                      }
                    }
                  }
                  this.$refs.loadingAnimation.stop();
                } else {
                  console.log("getGroupList failed");
                }
              })
              .catch((err) => {
                this.$refs.loadingAnimation.stop();
                window.alert(err + ". Please try again later. ");
                this.$router.go(-1);
              });
          } else {
            console.log("checkReservation failed");
          }
        })
        .catch((err) => {
          this.$refs.loadingAnimation.stop();
          window.alert(err + ". Please try again later. ");
          this.$router.go(-1);
        });
      this.mode = this.$route.params.mode;
      //this.useDefaultValue();
    } else {
      if (!this.$route.params.room || this.$route.params.room.length == 0) {
        this.$router.push({ path: "landingpage" });
        return;
      }
      this.meeting.room = this.$route.params.room;
      this.meeting.date = this.$route.params.chosenDate;
      let startingTimeIndex = -1;
      let endingTimeIndex = -1;
      for (let i = 0; i < times.length; i++) {
        for (let j = 0; j < this.$route.params.selectedTime.length; j++) {
          if (times[i].startingTime == this.$route.params.selectedTime[j]) {
            startingTimeIndex = i;
            break;
          }
        }
        if (startingTimeIndex != -1) {
          break;
        }
      }
      for (let i = times.length - 1; i >= 0; i--) {
        for (let j = 0; j < this.$route.params.selectedTime.length; j++) {
          if (times[i].startingTime == this.$route.params.selectedTime[j]) {
            endingTimeIndex = i;
            break;
          }
        }
        if (endingTimeIndex != -1) {
          break;
        }
      }
      this.meeting.time = this.$route.params.selectedTime;
      this.meeting.timeString =
        times[startingTimeIndex].startingTime +
        " ~ " +
        times[endingTimeIndex].endingTime;
      this.mode = "reserve";

      this.$refs.loadingAnimation.start();
      // Fetch groups
      this.axios
        .post("https://ntustsers.xyz/api/getGroupList", {
          userID: this.$cookies.get("userID"),
        })
        .then((response) => {
          let groups = response.data.groupList;
          if (groups) {
            for (let i = 0; i < groups.length; i++) {
              this.groups.push({
                id: groups[i].groupID,
                name: groups[i].GroupName,
                members: groups[i].emails,
              });
            }
            if (groups.length > 0) {
              this.meeting.groupID = this.groups[0].id;
            }
          }
          this.$refs.loadingAnimation.stop();
        })
        .catch((err) => {
          this.$refs.loadingAnimation.stop();
          window.alert(err + ". Please try again later. ");
          this.$router.go(-1);
        });
    }
  },
  methods: {
    useDefaultValue: function () {
      //this.meeting.name = "";
      this.meeting.date = "2021-12-23";
      this.meeting.time = '[ "15:30", "16:00", "16:30" ]';
      this.meeting.room = "Room1";
      //this.meeting.description =
      //  "Group 06 will discuss for the system of the game. ";
      //this.meeting.groupID = "id1";
    },
    createAGroup: function () {
      this.tempGroup = {
        id: "",
        name: "",
        members: [],
      };
      this.window.title = "Create a Group";
      this.$refs.floatingWindow.openWindow();
    },
    checkGroupValidation: function () {
      if (!this.tempGroup.name || this.tempGroup.name.length == 0) {
        let message =
          "Please fill in the group name. \nCreating a group failed. ";
        return { success: false, message: message };
      }
      if (!this.tempGroup.members || this.tempGroup.members.length == 0) {
        let message =
          "Please fill in members' emails. \nCreating a group failed. ";
        return { success: false, message: message };
      }
      return { success: true, message: "" };
    },
    modifyGroup: function (index) {
      this.window.title = "Modify a Group";
      this.tempGroup = this.groups[index];
      this.$refs.floatingWindow.openWindow();
    },
    saveGroup: function () {
      if (!this.tempGroup.id) {
        // Call api to create a new group using this.tempGroup.
        this.$refs.loadingAnimation.start();
        let validation = this.checkGroupValidation();
        if (!validation.success) {
          window.alert(validation.message);
          this.$refs.loadingAnimation.stop();
          return;
        }
        this.axios
          .post("https://ntustsers.xyz/api/addGroup", {
            groupName: this.tempGroup.name,
            emails: this.tempGroup.members,
            userID: this.$cookies.get("userID"),
            description: "",
          })
          .then((response) => {
            let success = response.data.success;
            if (success) {
              this.tempGroup.id = response.data.groupID;
              this.groups.push(this.tempGroup);
              this.meeting.groupID = response.data.groupID;
            } else {
              console.log("addGroup failed");
            }
            this.$refs.loadingAnimation.stop();
          })
          .catch((err) => {
            this.$refs.loadingAnimation.stop();
            window.alert(err + ". Please try again later. ");
          });
      } else {
        // Call api to save a group using this.tempGroup.
        this.$refs.loadingAnimation.start();
        this.axios
          .post("https://ntustsers.xyz/api/saveGroup", {
            groupID: this.tempGroup.id,
            groupName: this.tempGroup.name,
            emails: this.tempGroup.members,
            userID: this.$cookies.get("userID"),
            description: "",
          })
          .then((response) => {
            let success = response.data.success;
            console.log(response.data);
            if (success) {
              window.alert("Save group successfully. ");
            } else {
              console.log("saveGroup failed");
            }
            this.$refs.loadingAnimation.stop();
          })
          .catch((err) => {
            this.$refs.loadingAnimation.stop();
            window.alert(err + ". Please try again later. ");
          });
      }
    },
    deleteGroup: function (index) {
      // Call api to delete a group.
      this.$refs.loadingAnimation.start();
      this.axios
        .post("https://ntustsers.xyz/api/deleteGroup", {
          userID: this.$cookies.get("userID"),
          groupID: this.groups[index].id,
        })
        .then((response) => {
          let success = response.data.success;
          if (success) {
            if (this.meeting.groupID == this.groups[index].id) {
              this.meeting.groupID = "";
            }
            this.groups.splice(index, 1);
          } else {
            console.log("deleteGroup failed");
          }
          this.$refs.loadingAnimation.stop();
        })
        .catch((err) => {
          this.$refs.loadingAnimation.stop();
          window.alert(err + ". Please try again later. ");
        });
    },
    inspectGroup: function () {
      for (let i = 0; i < this.groups.length; i++) {
        if (this.meeting.groupID == this.groups[i].id) {
          this.tempGroup = this.groups[i];
          break;
        }
      }
      this.tempGroup.readonly = true;
      this.$refs.floatingWindow.openWindow();
    },
    checkMeetingValidation: function () {
      if (!this.meeting.name || this.meeting.name.length == 0) {
        let message = "Please fill in the meeting name. ";
        return { success: false, message: message };
      }
      if (!this.meeting.groupID || this.meeting.groupID.length == 0) {
        let message =
          "Please select a group. \nIf you don't have any group, please create one. ";
        return { success: false, message: message };
      }
      return { success: true, message: "" };
    },
    reserve: function () {
      this.$refs.loadingAnimation.start();
      let validation = this.checkMeetingValidation();
      if (!validation.success) {
        window.alert(validation.message);
        this.$refs.loadingAnimation.stop();
        return;
      }
      this.axios
        .post("https://ntustsers.xyz/api/reserveOneTime", {
          user_ID: this.$cookies.get("userID"),
          group_ID: this.meeting.groupID,
          title: this.meeting.name,
          date: this.meeting.date,
          time: this.meeting.time,
          description: this.meeting.description,
          room: this.meeting.room,
        })
        .then((response) => {
          let success = response.data.success;
          if (success) {
            this.$router.push({ path: "chooseactions" });
          } else {
            console.log("reserveOneTime failed");
          }
          window.alert("Reservation complete!");
          this.$refs.loadingAnimation.stop();
        })
        .catch((err) => {
          this.$refs.loadingAnimation.stop();
          window.alert(err + ". Please try again later. ");
        });
    },
    cancel: function () {
      this.$router.go(-1);
    },
    save: function () {
      this.$refs.loadingAnimation.start();
      let validation = this.checkMeetingValidation();
      if (!validation.success) {
        window.alert(validation.message);
        this.$refs.loadingAnimation.stop();
        return;
      }
      this.axios
        .post("https://ntustsers.xyz/api/cancelReservation", {
          meeting_ID: this.meeting.id,
        })
        .then((response) => {
          let success = response.data.success;
          if (success) {
            this.axios
              .post("https://ntustsers.xyz/api/reserveOneTime", {
                user_ID: this.$cookies.get("userID"),
                group_ID: this.meeting.groupID,
                title: this.meeting.name,
                date: this.meeting.date,
                time: this.meeting.time,
                description: this.meeting.description,
                room: this.meeting.room,
              })
              .then((response) => {
                let success = response.data.success;
                if (success) {
                  this.$router.push({ path: "chooseactions" });
                } else {
                  console.log("reserveOneTime failed");
                }
                this.$refs.loadingAnimation.stop();
              })
              .catch((err) => {
                this.$refs.loadingAnimation.stop();
                window.alert(err + ". Please try again later. ");
              });
          } else {
            console.log("cancelReservation failed");
          }
        })
        .catch((err) => {
          this.$refs.loadingAnimation.stop();
          window.alert(err + ". Please try again later. ");
        });
    },
    back: function () {
      this.$router.go(-1);
    },
    updateTempGroup(newGroup) {
      this.tempGroup = newGroup;
    },
    getTimesString: function () {
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
          startingTime:
            startingTime.hours.toString() +
            ":" +
            ("0" + startingTime.minutes.toString()).slice(-2),
          endingTime:
            endingTime.hours.toString() +
            ":" +
            ("0" + endingTime.minutes.toString()).slice(-2),
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
  },
};
</script>
