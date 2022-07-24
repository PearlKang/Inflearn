<template>
  <div class="flex h-screen container mx-auto">
    <!-- left side bar section -->
    <div
      class="w-20 xl:w-1/4 pt-5 xl:ml-10 flex flex-col justify-between border-r border-color"
    >
      <!-- left menu -->
      <div class="flex flex-col items-center xl:items-start">
        <!-- twitter logo -->
        <i class="fa-brands fa-twitter text-3xl text-primary xl:ml-4 mb-3"></i>

        <!-- left side menu icons -->
        <div class="flex flex-col items-start">
          <router-link
            to="/"
            class="hover:text-primary hover:bg-blue-50 px-4 py-2 rounded-full cursor-pointer"
          >
            <i class="fas fa-home fa-fw text-2xl"></i>
            <span class="ml-5 text-xl hidden xl:inline-block">홈</span>
          </router-link>

          <router-link
            to="/"
            class="hover:text-primary hover:bg-blue-50 px-4 py-2 rounded-full cursor-pointer"
          >
            <i class="fas fa-hashtag fa-fw text-2xl"></i>
            <span class="ml-5 text-xl hidden xl:inline-block">탐색하기</span>
          </router-link>

          <router-link
            to="/notifications"
            class="hover:text-primary hover:bg-blue-50 px-4 py-2 rounded-full cursor-pointer"
          >
            <i class="far fa-bell fa-fw text-2xl"></i>
            <span class="ml-5 text-xl hidden xl:inline-block">알림</span>
          </router-link>

          <router-link
            to="/messages"
            class="hover:text-primary hover:bg-blue-50 px-4 py-2 rounded-full cursor-pointer"
          >
            <i class="far fa-envelope fa-fw text-2xl"></i>
            <span class="ml-5 text-xl hidden xl:inline-block">쪽지</span>
          </router-link>

          <router-link
            to="/"
            class="hover:text-primary hover:bg-blue-50 px-4 py-2 rounded-full cursor-pointer"
          >
            <i class="far fa-bookmark fa-fw text-2xl"></i>
            <span class="ml-5 text-xl hidden xl:inline-block">북마크</span>
          </router-link>

          <router-link
            to="/"
            class="hover:text-primary hover:bg-blue-50 px-4 py-2 rounded-full cursor-pointer"
          >
            <i class="far fa-list-alt fa-fw text-2xl"></i>
            <span class="ml-5 text-xl hidden xl:inline-block">리스트</span>
          </router-link>

          <router-link
            to="/profile"
            class="hover:text-primary hover:bg-blue-50 px-4 py-2 rounded-full cursor-pointer"
          >
            <i class="far fa-user fa-fw text-2xl"></i>
            <span class="ml-5 text-xl hidden xl:inline-block">프로필</span>
          </router-link>

          <router-link
            to="/"
            class="hover:text-primary hover:bg-blue-50 px-4 py-2 rounded-full cursor-pointer"
          >
            <i class="fas fa-ellipsis-h fa-fw text-2xl"></i>
            <span class="ml-5 text-xl hidden xl:inline-block">더보기</span>
          </router-link>
        </div>

        <!-- tweet button -->
        <div class="w-full xl:pr-3 flex justify-center">
          <button
            class="mt-3 bg-primary text-white xl:w-full w-12 h-12 rounded-full hover:bg-dark"
          >
            <span class="hidden xl:block">트윗</span>
            <i class="fas fa-plus xl:hidden"></i>
          </button>
        </div>
      </div>

      <!-- profile button -->
      <div class="xl:pr-3 mb-3">
        <button
          class="hidden xl:flex mt-3 px-2 py-1 w-full h-12 rounded-full hover:bg-blue-50 items-center"
        >
          <img src="https://picsum.photos/100" class="w-10 h-10 rounded-full" />

          <div class="xl:ml-2 hidden xl:block">
            <div class="text-sm font-bold">benkang.com</div>
            <div class="text-xs text-gray text-left">@benkang</div>
          </div>

          <i
            class="ml-auto fas fa-ellipsis-h fa-fw text-xs hidden xl:block"
          ></i>
        </button>

        <div class="xl:hidden flex justify-center">
          <img
            src="https://picsum.photos/100"
            class="w-10 h-10 rounded-full cursor-pointer hover:opacity-80"
          />
        </div>
      </div>
    </div>

    <!-- right main section -->
    <div class="flex-1 flex h-screen">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style></style>
