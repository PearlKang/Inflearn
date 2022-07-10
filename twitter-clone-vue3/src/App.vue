<template>
  <div class="flex h-screen">
    <!-- left side bar -->
    <div class="w-1/4 mt-5 ml-10">
      <!-- twitter logo -->
      <i class="fa-brands fa-twitter text-2xl text-primary ml-4"></i>
      <!-- left side menu icons -->
      <div class="flex flex-col items-start">
        <div class="hover:text-primary hover:bg-blue-50 px-4 py-2 rounded-full">
          <i class="fas fa-home fa-fw text-2xl"></i>
          <span class="ml-5 text-lg">홈</span>
        </div>
        <div class="hover:text-primary hover:bg-blue-50 px-4 py-2 rounded-full">
          <i class="fas fa-hashtag fa-fw text-2xl"></i>
          <span class="ml-5 text-lg">탐색하기</span>
        </div>
        <div class="hover:text-primary hover:bg-blue-50 px-4 py-2 rounded-full">
          <i class="far fa-bell fa-fw text-2xl"></i>
          <span class="ml-5 text-lg">알림</span>
        </div>
        <div class="hover:text-primary hover:bg-blue-50 px-4 py-2 rounded-full">
          <i class="far fa-envelope fa-fw text-2xl"></i>
          <span class="ml-5 text-lg">쪽지</span>
        </div>
        <div class="hover:text-primary hover:bg-blue-50 px-4 py-2 rounded-full">
          <i class="far fa-bookmark fa-fw text-2xl"></i>
          <span class="ml-5 text-lg">북마크</span>
        </div>
        <div class="hover:text-primary hover:bg-blue-50 px-4 py-2 rounded-full">
          <i class="far fa-list-alt fa-fw text-2xl"></i>
          <span class="ml-5 text-lg">리스트</span>
        </div>
        <div class="hover:text-primary hover:bg-blue-50 px-4 py-2 rounded-full">
          <i class="far fa-user fa-fw text-2xl"></i>
          <span class="ml-5 text-lg">프로필</span>
        </div>
        <div class="hover:text-primary hover:bg-blue-50 px-4 py-2 rounded-full">
          <i class="fas fa-ellipsis-h fa-fw text-2xl"></i>
          <span class="ml-5 text-lg">더보기</span>
        </div>
      </div>
      <!-- tweet button -->
      <button
        class="mt-3 bg-primary text-white w-full h-12 rounded-full hover:bg-dark"
      >
        트윗
      </button>
    </div>
    <!-- right main screen -->
    <div class="flex-1 bg-red-200"></div>
  </div>
</template>

<script>
export default {};
</script>

<style></style>
