<template>
	<div class="container container-flex container-flex-column">
		<v-select v-model="room" label="Room" :options="$ROOMS" />
		<Calendar @dayclick="testEvent" />
	</div>
</template>

<script>
export default {
	name: "DateAndRoom",
	data() {
		return {
			room: "Room1", 
		}
	}, 
	components: {
	}, 
	computed: {
	}, 
	created() {
	}, 
	mounted() {
	},
	methods: {
		testEvent: function() {
			window.alert("HI");
		}, 
	}, 
};
</script>

