const { createApp, ref, onMounted } = Vue;

createApp({
  delimiters: ["[[", "]]"], // Change the default delimiters to [[ and ]]
  setup() {
    onMounted(() => {
      console.log("mounted");
    });
    const message = ref("Hello vue!");
    const myName = ref("Daniel Supernault");
    return {
      message,
      myName,
    };
  },
}).mount("#app");
