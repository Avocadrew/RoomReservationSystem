<template>
	<div class="container container-flex container-flex-column">
		<h3>{{ meeting.name }}</h3>
		<div class="container line-container">
			<p class="label">Date: </p>
			<p>{{ meeting.date }}</p>
		</div>
		<div class="container line-container">
			<p class="label">Time: </p>
			<p>{{ meeting.time }}</p>
		</div>
		<div class="container line-container">
			<p class="label">Room: </p>
			<p>{{ meeting.room }}</p>
		</div>
		<div class="container line-container">
			<p class="label">Group: </p>
			<p>{{ meetingGroup.name }}</p>
			<button class="button icon-button">
				<mdicon name="magnify" />
			</button>
		</div>
		<div class="container area-container">
			<p class="label">Description: </p>
			<p class="textBox">{{ meeting.description }}</p>
		</div>
		<div class="container container-flex container-flex-row">
			<button class="button secondary-button button-fixed-width-medium" @click="testEvent">
				DELETE
			</button>
			<button class="button primary-button button-fixed-width-medium" @click="testEvent">
				EDIT
			</button>
		</div>
	</div>
</template>

<script>
export default {
	name: "MeetingInfo",
	data() {
		return {
			meeting: {
				name: "", 
				date: "", 
				time: "", 
				room: "", 
				description: "", 
				groupID: "", 
			}, 
		}
	}, 
	components: {
	}, 
	computed: {
		meetingGroup: function() {
			let group = {};
			if (this.meeting.groupID) {
				// Get group information
				group.name = "Group1";
				group.participants = ["A", "B"];
			}
			return group;
		}
	}, 
	created() {
	}, 
	mounted() {
		this.useDefaultValue();
		console.log(this.meeting.name);
	},
	methods: {
		useDefaultValue: function() {
			this.meeting.name = "Financial Meeting";
			this.meeting.date = "Nov 7th, 2021";
			this.meeting.time = "13:00 ~ 14:30";
			this.meeting.room = "Room1";
			this.meeting.description = "Group 06 will discuss for the system of the game. ";
			this.meeting.groupID = "abcd";
		}, 
		testEvent: function() {
			window.alert("HI");
		}, 
	}, 
};
</script>


