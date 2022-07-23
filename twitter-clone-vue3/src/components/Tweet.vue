<template>
  <div
    class="flex px-3 py-3 border-b border-color hover:bg-gray-50 cursor-pointer"
  >
    <img
      src="http://picsum.photos/200"
      class="w-10 h-10 rounded-full hover:opacity-80 cursor-pointer"
    />

    <div class="ml-3 flex-1 flex flex-col space-y-1">
      <!-- tweet title -->
      <div class="text-sm space-x-1">
        <span class="font-bold">T1 LoL</span>
        <span class="text-gray text-xs">@T1LoL</span>
        <span class="">·</span>
        <span class="text-gray text-xs">1시간</span>
      </div>

      <!-- tweet body -->
      <div class="">
        [2022 #LCK Summer R2 M10 vs. DRX] 서머의 전환점, 2라운드의 시작! 이번
        라운드도 T1 다운 모습 보여드리겠습니다. The second Round starts NOW! We
        will show everyone what T1 is made of. ⏰8 PM KST #T1WIN #T1Fighting
      </div>

      <!-- tweet actions -->
      <div class="flex justify-between">
        <div class="text-gray hover:text-primary">
          <i class="far fa-comment hover:bg-blue-50 rounded-full p-2"></i>
          <span class="ml-1 text-sm">1</span>
        </div>

        <div class="text-gray hover:text-green-500">
          <i class="fas fa-retweet hover:bg-green-50 rounded-full p-2"></i>
          <span class="ml-1 text-sm">2</span>
        </div>

        <div class="text-gray hover:text-red-500">
          <i class="far fa-heart hover:bg-red-50 rounded-full p-2"></i>
          <span class="ml-1 text-sm">3</span>
        </div>

        <div class="text-gray hover:text-primary">
          <i class="far fa-share-square hover:bg-blue-50 rounded-full p-2"></i>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style></style>
