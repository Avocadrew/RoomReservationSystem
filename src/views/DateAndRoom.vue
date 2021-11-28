<template>
  <div class="container container-flex container-flex-column">
    <v-select v-model="room" label="Room" :options="$ROOMS" />
    <Calendar @dayclick="chooseDate" />
  </div>
	<FloatingWindow :window="window" ref="floatingWindow"/>
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
			floatingContainerOpened: false, 
			chosenDate: "", 
    };
  },
	computed: {
		window: function() {
			return {
				title: this.chosenDate, 
				nextPath: "../filloutmeetinginfo", 
			};
		}, 
	},
  created() {},
  mounted() {},
  methods: {
    chooseDate: function (param) {
      console.log(param);
			this.chosenDate = param.ariaLabel;
			this.$refs.floatingWindow.openWindow();
    },
  },
};
</script>
