<template>
  <div class="flex-1 flex">
    <!-- chat list -->
    <div class="w-2/5 border-r border-color overflow-y-auto">
      <div class="flex flex-col">
        <!-- title -->
        <div class="p-3 font-bold text-lg border-b border-color h-14">쪽지</div>

        <!-- selected -->
        <div
          class="flex px-3 py-4 hover:bg-gray-50 border-b border-color bg-gray-200"
        >
          <img
            src="http://picsum.photos/200"
            class="w-10 h-10 rounded-full cursor-pointer mr-2"
          />

          <div class="">
            <div class="flex space-x-1">
              <div class="font-bold">benkang.com</div>
              <div class="text-gray">@benkang</div>
              <div class="text-gray">7월 20일</div>
            </div>
            <div class="text-gray">123123</div>
          </div>
        </div>

        <!-- a chat list -->
        <div
          class="flex px-3 py-4 hover:bg-gray-50 border-b border-color"
          v-for="message in 30"
          :key="message"
        >
          <img
            src="http://picsum.photos/200"
            class="w-10 h-10 rounded-full cursor-pointer mr-2"
          />

          <div class="">
            <div class="flex space-x-1">
              <div class="font-bold">benkang.com</div>
              <div class="text-gray">@benkang</div>
              <div class="text-gray">7월 20일</div>
            </div>
            <div class="text-gray">메세지</div>
          </div>
        </div>
      </div>
    </div>

    <!-- chatting -->
    <div class="w-3/5 border-r border-color">
      <div class="flex flex-col h-screen">
        <!-- title -->
        <div class="flex px-3 h-14 items-center border-b border-color">
          <img
            src="http://picsum.photos/100"
            class="w-8 h-8 rounded-full mr-2 cursor-pointer"
          />

          <div class="">
            <div class="font-bold text-lg">benkang.com</div>
            <div class="text-sm text-gray">@benkang</div>
          </div>
        </div>

        <!-- user info -->
        <div
          class="flex flex-col justify-center items-center border-b border-color hover:bg-gray-50 py-6"
        >
          <div class="">
            <span class="font-bold mr-1">benkang.com</span>
            <span class="text-gray">@benkang</span>
          </div>
          <div class="">
            <span class="font-bold mr-1">28</span>
            <span class="text-gray">팔로우 중</span>
            <span class="font-bold ml-3 mr-1">7</span>
            <span class="text-gray">팔로워</span>
          </div>
          <div class="">
            <span class="text-gray mr-1">가입일:</span>
            <span class="text-gray">2022년 07월</span>
          </div>
        </div>

        <!-- chat bubble -->
        <div class="flex-1 overflow-y-auto">
          <!-- chat bubble : my chat-->
          <div class="text-right px-3 py-3">
            <span class="bg-primary text-white px-4 py-2 rounded-full">
              메세지
            </span>
            <div class="mt-2 text-xs text-gray">2022년 7월 21일 오전 1:11</div>
          </div>

          <!-- chat bubble : opponent chat -->
          <div class="text-left px-3 py-3" v-for="chat in 30" :key="chat">
            <span class="bg-gray-100 px-4 py-2 rounded-full"> 메세지 </span>
            <div class="mt-2 text-xs text-gray">2022년 7월 21일 오전 1:11</div>
          </div>
        </div>

        <!-- chat input -->
        <div class="flex items-center bg-white border-t border-color sticky">
          <input
            type="text"
            class="m-2 py-1 px-4 rounded-full bg-gray-100 resize-none outline-none flex-1"
            placeholder="새 쪽지 작성하기"
          />
          <button class="text-center">
            <i
              class="far fa-paper-plane text-primary text-lg hover:bg-blue-50 p-2 rounded-full w-10 h-10"
            ></i>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style></style>
