<template>
  <!-- ✅ Vue의 렌더링 대상이 되는 HTML 구조를 정의합니다 -->
  <div id="app">
    <!-- 
      📌 루트 요소 (Root Element)
      - <div id="app">: Vue 인스턴스가 마운트되는 최상위 요소입니다.
      - Vue 2에서는 반드시 하나의 루트 요소가 필요하며,
        Vue 3에서는 Fragment로 여러 요소를 사용할 수 있습니다.
    -->

    <!-- 
      🔗 WaitingRoom 컴포넌트 렌더링
      - <WaitingRoom />: components 폴더에 있는 WaitingRoom.vue를 현재 화면에 표시합니다.
      - 이 위치에 WaitingRoom 컴포넌트의 내용이 렌더링됩니다.
      - <div> </div> 안에 있는 애들은 자식 컴포넌트임.
    -->
    <WaitingRoom />
  </div>
</template>

<script>
import WaitingRoom from "./components/WaitingRoom.vue";

// export default는 한 파일에서 1개만 가능. 내보낸 거 쓸 때는, import App from './App.js'
// export는 여러 개의 값 내보내기 가능. 내보낸 거 쓸 때는, import { add } from './utils.js'

export default {
  // 객체를 'export'하면, 이 컴포넌트를 다른 파일에서 import해서 사용할 수 있음.
  name: "App", // 컴포넌트 이름 설정 (디버깅이나 개발 도구에서 유용)
  components: {
    // 현재 컴포넌트에서 사용할 컴포넌트 등록
    WaitingRoom, // 등록된 컴포넌트를 <WaitingRoom /> 태그로 사용할 수 있음
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif; /* 폰트 설정 (우선순위대로 적용) */
  text-align: center; /* 텍스트를 중앙 정렬 */
  margin-top: 60px; /* 상단 여백을 60px로 설정 */
}
</style>
