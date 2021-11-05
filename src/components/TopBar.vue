<template>
	<div class="top-bar">
		<div>
			<button class="button" @click="testEvent">
				<h2>
					hi
				</h2>
			</button>
		</div>
		<div>
			<button class="button" @click="testEvent">
				HI
			</button>
		</div>
	</div>
</template>

<script>
export default {
	name: "TopBar",
	props: {
		msg: String,
	},
	methods: {
		testEvent: function() {
			window.alert("HI");
		}, 
	}, 
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
</style>

