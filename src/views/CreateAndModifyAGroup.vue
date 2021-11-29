<template>
  <div class="container container-flex container-flex-column">
    <div class="container line-container">
      <p class="label">Group Name:</p>
      <input type="text" name="name" v-model="newParams.name" />
    </div>
    <div class="container area-container">
      <div class="container line-container">
        <p class="label">Group Members' emails:</p>
        <button class="button icon-button" @click="addNewMember">
          <mdicon name="plus" :size="20" />
        </button>
      </div>
      <div
        class="container container-useless-wrapper"
        v-for="(member, index) in newParams.members"
        :key="index"
      >
        <input
          type="email"
          :name="'member-' + index"
          v-model="newParams.members[index]"
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
      newParams: Object,
    };
  },
  props: {
    params: Object,
    isDone: Boolean,
  },
  watch: {
    isDone: function (oldValue, newValue) {
      if (newValue) {
        this.$emit("params", this.newParams);
      }
    },
    params: {
      handler: function () {
        this.newParams = this.params;
      },
      deep: true,
      immediate: true,
    },
    newParams: {
      handler: function () {
        this.$emit("params", this.newParams);
      },
      deep: true,
      immediate: true,
    },
  },
  computed: {},
  created() {},
  mounted() {},
  methods: {
    addNewMember: function () {
      this.newParams.members.push("");
    },
    deleteMember: function (index) {
      this.newParams.members.splice(index, 1);
    },
  },
};
</script>
