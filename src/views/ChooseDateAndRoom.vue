<template>
  <div class="container container-flex container-flex-column">
    <v-select v-model="room" label="Room" :options="$ROOMS" />
    <Calendar @dayclick="chooseDate" />
  </div>
  <FloatingWindow
    :window="window"
    :params="paramsForChooseTime"
    ref="floatingWindow"
    :showDoneButton="!viewingMode"
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
      chosenDate: "",
			dailyReservation: {}, 
    };
  },
  computed: {
    window: function () {
      return {
				title: this.room + " on " + this.chosenDate,
        nextPath: "filloutmeetinginfo",
      };
    },
    paramsForChooseTime: function () {
      return {
        viewingMode: this.viewingMode,
				dailyReservation: this.dailyReservation, 
      };
    },
    account: function () {
      return this.$cookies.get("account");
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
		generateTestData: function() {
			this.dailyReservation = {
				"9:00": true, 
				"9:30": false, 
				"10:00": true, 
				"14:00": true, 
				"15:00": true, 
			};
		}, 
    chooseDate: function (param) {
      console.log(param);
      this.chosenDate = param.ariaLabel;
			// Get one day reservation information. 
			this.generateTestData();
      this.$refs.floatingWindow.openWindow();
    },
  },
};
</script>
