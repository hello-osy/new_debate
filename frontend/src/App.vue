<template>
  <div id="app">
    <WaitingRoom />
  </div>
</template>

<script>
import WaitingRoom from "./components/WaitingRoom.vue";

export default {
  name: "App",
  components: {
    WaitingRoom,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  margin-top: 60px;
}
</style>
