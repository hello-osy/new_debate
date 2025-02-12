<template>
  <div v-if="status === 'waiting'">
    <h2>매칭 대기 중...</h2>
    <p>상대방을 기다리고 있습니다.</p>
  </div>
  <OneToOneChat
    v-else-if="status === 'matched'"
    :room="roomId"
    :partner="partnerId"
  />
  <button v-if="status === 'idle'" @click="requestMatch">1:1 채팅 신청</button>
</template>

<script>
import io from "socket.io-client";
import OneToOneChat from "./OneToOneChat.vue";

export default {
  components: { OneToOneChat },
  data() {
    return {
      socket: null,
      status: "idle", // idle → waiting → matched
      roomId: "",
      partnerId: "",
      userId: "user_" + Math.floor(Math.random() * 10000), // 임시 사용자 ID
    };
  },
  created() {
    this.socket = io("http://localhost:5000");

    this.socket.on("matched", (data) => {
      this.status = "matched";
      this.roomId = data.room_id;
      this.partnerId = data.partner_id;
    });
  },
  methods: {
    requestMatch() {
      this.status = "waiting";
      this.socket.emit("join", { user_id: this.userId, username: this.userId });

      fetch("http://localhost:5000/match", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_id: this.userId }),
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.status === "matched") {
            this.status = "matched";
            this.roomId = data.room_id;
            this.partnerId = data.partner_id;
          }
        });
    },
  },
};
</script>
