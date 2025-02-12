<template>
  <!-- 
    ✅ Vue의 렌더링 대상이 되는 HTML 구조를 정의합니다.

    📦 Virtual DOM 구조 (Vue 3의 Fragment 개념):
    Virtual DOM
    └── Fragment (가상의 루트 요소)
        ├── <div> 매칭 대기 중...</div>          → 매칭 대기 상태일 때 표시
        ├── <OneToOneChat>...</OneToOneChat>    → 매칭 완료 시 표시되는 채팅 컴포넌트
        └── <button>1:1 채팅 신청</button>       → 대기 중이 아닐 때 표시되는 채팅 신청 버튼

    Vue 3에서는 Fragment를 통해 불필요한 <div> 태그 없이도 여러 요소를 렌더링할 수 있습니다.
  -->

  <!-- 매칭 대기 상태일 때 표시되는 메시지 -->
  <div v-if="status === 'waiting'">
    <h2>매칭 대기 중...</h2>
    <p>상대방을 기다리고 있습니다.</p>
  </div>

  <!-- 매칭이 완료되면 OneToOneChat 컴포넌트를 렌더링 -->
  <!-- OneToOneChat이라는 이름의 커스텀 컴포넌트를 사용하려면, 반드시 script에서 import하고 등록해야 합니다. -->
  <OneToOneChat
    v-else-if="status === 'matched'"
    :room="roomId"          <!-- 방 ID를 전달 -->
    :partner="partnerId"    <!-- 상대방 ID를 전달 -->
  />

  <!-- 기본 상태(idle)일 때는 1:1 채팅 신청 버튼을 표시 -->
  <!-- button 컴포넌트는 기본 컨포넌트여서 import 안 해도 사용 가능 -->
  <button v-if="status === 'idle'" @click="requestMatch">
    1:1 채팅 신청
  </button>
</template>


<script>
import io from "socket.io-client";
import OneToOneChat from "./OneToOneChat.vue";

export default {
  components: { OneToOneChat }, // 현재 컴포넌트에서 사용할 컴포넌트 등록
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
  methods: { // methods 안에 있는 함수들은 Vue의 반응형 시스템과 연결됨(이벤트 처리, 데이터 변경, UI 업데이트 가능능). 밖에 있는 다른 애들은 그냥 일반 js 함수임.
    requestMatch() {
      this.status = "waiting"; // 1️⃣ 매칭 요청 상태로 변경

      // 2️⃣ 소켓 서버로 'join' 이벤트 전송
      this.socket.emit("join", { user_id: this.userId, username: this.userId });

      // 3️⃣ REST API 호출 (매칭 요청)
      fetch("http://localhost:5000/match", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_id: this.userId }),
      })
        .then((response) => response.json()) // 4️⃣ 서버 응답 처리
        .then((data) => {
          if (data.status === "matched") {
            // 5️⃣ 매칭 성공 시 상태 및 정보 업데이트
            this.status = "matched";
            this.roomId = data.room_id;
            this.partnerId = data.partner_id;
          }
        });
    },
  },
};
</script>
