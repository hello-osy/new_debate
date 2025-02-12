<template>
  <div id="app">
    <h1>Vue + Flask + MySQL</h1>
    <button @click="fetchData">데이터 가져오기</button>
    <ul v-if="data.length">
      <li v-for="(item, index) in data" :key="index">{{ item }}</li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      data: [],
    };
  },
  methods: {
    fetchData() {
      fetch("http://localhost:5000/data")
        .then((response) => response.json())
        .then((data) => {
          this.data = data;
        });
    },
  },
};
</script>
