<template>
  <div>
    <!-- v-bind:프롭스 속성 이름="상위 컴포넌트의 데이터 이름" -->
    <app-header v-bind:propsdata="str"></app-header>
  </div>
</template>

<script>
import AppHeader from "./components/AppHeader.vue";

// var AppHeader = {
//   template: "<header><h1>Header</h1></header>",
// };

// new Vue({
//   data: {
//     str: "hi",
//   },
// });

export default {
  data: function () {
    return {
      str: "Header",
    };
  },
  components: {
    "app-header": AppHeader,
  },
};
</script>

<style></style>
