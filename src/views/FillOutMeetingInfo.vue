<template>
  <div class="container container-flex container-flex-column">
    <div class="container line-container">
      <p class="label">Meeting Name:</p>
      <input type="text" name="name" v-model="meeting.name" />
    </div>
    <div class="container line-container">
      <p class="label">Date:</p>
      <p>{{ meeting.date }}</p>
    </div>
    <div class="container line-container">
      <p class="label">Time:</p>
      <p>{{ meeting.time }}</p>
    </div>
    <div class="container line-container">
      <p class="label">Room:</p>
      <p>{{ meeting.room }}</p>
    </div>
    <div class="container area-container">
      <div class="container line-container">
        <p class="label">Group:</p>
        <button class="button primary-button sub-button" @click="createAGroup">
          Create a Group
        </button>
      </div>
      <div class="container container-useless-wrapper">
        <div v-for="(group, index) in groups" :key="index">
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
    </div>
    <div class="container area-container">
      <p class="label">Description:</p>
      <textarea name="description" v-model="meeting.description" />
    </div>
    <div class="container container-flex container-flex-row">
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
    @params="tempGroup"
    ref="floatingWindow"
    @done="saveGroup"
  />
</template>

<script>
import FloatingWindow from "@/components/FloatingWindow.vue";

export default {
  name: "FillOutMeetingInfo",
  components: {
    FloatingWindow,
  },
  data() {
    return {
      mode: "reserve",
      meeting: {
        name: "",
        date: "",
        time: "",
        room: "",
        description: "",
        groupID: "",
      },
      groups: [
        {
          id: "id1",
          name: "Group1",
          members: ["abc@gmail.com", "haha@gmail.com"],
        },
        {
          id: "id2",
          name: "Group2",
          members: ["def@gmail.com", "hello@gmail.com"],
        },
      ],
      window: {
        title: "Create a Group",
      },
      tempGroup: {
        id: "",
        name: "testGroup",
        members: ["hello@gmail.com", "hi@gmail.com"],
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
    if (this.$route.query.meetingid) {
      // Fetch the meeting.
      this.mode = "edit";
      this.useDefaultValue();
    } else {
      this.mode = "reserve";
    }
    // Fetch groups and after success:
    if (this.groups.length != 0) {
      this.meeting.groupID = this.groups[0].id;
    }
  },
  methods: {
    useDefaultValue: function () {
      this.meeting.name = "Financial Meeting";
      this.meeting.date = "Nov 7th, 2021";
      this.meeting.time = "13:00 ~ 14:30";
      this.meeting.room = "Room1";
      this.meeting.description =
        "Group 06 will discuss for the system of the game. ";
      this.meeting.groupID = "id1";
    },
    testEvent: function () {
      console.log(this.meetingGroup);
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
    modifyGroup: function (index) {
      this.tempGroup = this.groups[index];
      this.window.title = "Modify a Group";
      this.$refs.floatingWindow.openWindow();
    },
    saveGroup: function () {
      console.log(this.tempGroup);
      // Call api to create a new group using tempGroup.
      window.alert("Save group");
    },
    deleteGroup: function (index) {
      // Call api to delete a group, and then refetch groups.
      window.alert("Delete group " + index.toString());
    },
    reserve: function () {
      window.alert("Reserve");
    },
    cancel: function () {
      this.$router.go(-1);
    },
    save: function () {
      window.alert("Save");
    },
  },
};
</script>
