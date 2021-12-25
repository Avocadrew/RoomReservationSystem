<template>
  <div class="container container-flex container-flex-column">
    <div class="container line-container">
      <p class="label">Group Name:</p>
      <input type="text" name="name" v-model="newGroup.name" />
    </div>
    <div class="container area-container">
      <div class="container line-container">
        <p class="label">Group Members' emails:</p>
        <button class="button icon-button" @click="addNewMember">
          <mdicon name="plus" :size="20" />
        </button>
      </div>
      <div
        class="container line-container container-useless-wrapper"
        v-for="(member, index) in newGroup.members"
        :key="index"
      >
        <input
          type="email"
          :name="'member-' + index"
          v-model="newGroup.members[index]"
        />
        <button class="button icon-button" @click="deleteMember(index)">
          <mdicon name="delete" :size="20" />
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CreateAndModifyAGroup",
  components: {},
  data() {
    return {
      newGroup: Object,
    };
  },
  props: {
    params: Object,
    isDone: Boolean,
  },
  watch: {
    isDone: function (newValue) {
      if (newValue) {
        this.$emit("updateInfo", this.newGroup);
      }
    },
    newGroup: {
      handler: function (newValue) {
        this.$emit("updateInfo", newValue);
      },
      deep: true,
    },
  },
  computed: {},
  created() {},
  mounted() {
    this.newGroup = this.params;
  },
  methods: {
    addNewMember: function () {
      this.newGroup.members.push("");
    },
    deleteMember: function (index) {
      this.newGroup.members.splice(index, 1);
    },
  },
};
</script>
