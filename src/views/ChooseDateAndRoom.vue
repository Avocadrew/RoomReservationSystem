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
    };
  },
  computed: {
    window: function () {
      return {
        title: this.chosenDate,
        nextPath: "filloutmeetinginfo",
      };
    },
    paramsForChooseTime: function () {
      return {
        viewingMode: this.viewingMode,
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
    chooseDate: function (param) {
      console.log(param);
      this.chosenDate = param.ariaLabel;
      this.$refs.floatingWindow.openWindow();
    },
  },
};
</script>
