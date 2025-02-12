<template>
  <div>
    <h2>채팅방 (상대방: {{ partner }})</h2>
    <div v-for="(msg, index) in messages" :key="index">
      <strong>{{ msg.sender }}:</strong> {{ msg.msg }}
    </div>
    <input
      v-model="message"
      @keyup.enter="sendMessage"
      placeholder="메시지를 입력하세요"
    />
    <button @click="sendMessage">전송</button>
  </div>
</template>

<script>
export default {
  props: ["room", "partner"],
  data() {
    return {
      socket: null,
      messages: [],
      message: "",
      username: "user_" + Math.floor(Math.random() * 10000),
    };
  },
  created() {
    this.socket = this.$root.socket; // 부모 컴포넌트의 소켓 재사용
    this.socket.emit("join", { room: this.room, username: this.username });

    this.socket.on("message", (data) => {
      this.messages.push(data);
    });
  },
  methods: {
    sendMessage() {
      if (this.message.trim()) {
        this.socket.emit("message", {
          room: this.room,
          msg: this.message,
          username: this.username,
        });
        this.message = "";
      }
    },
  },
};
</script>
