import Vue from "vue";

Vue.component("sample-component", {
  template: "#sample-component",
  props: {},
  data: function () {
    return {
      name: "Amit",
    };
  },
  mounted: async function () {
    console.log("THis was mounted..");
  },
  methods: {},
  delimiters: ["[[", "]]"],
});
