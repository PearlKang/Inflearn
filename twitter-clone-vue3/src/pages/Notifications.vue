<template>
  <div class="flex-1 border-r border-gray-100 flex flex-col overflow-y-auto">
    <!-- title -->
    <div class="p-3 font-bold text-lg border-b border-gray-100">알림</div>

    <!-- notifications -->
    <div
      class="flex flex-col hover:bg-gray-50 p-3 space-y-2 border-b border-gray-100 cursor-pointer"
      v-for="notification in 10"
      :key="notification"
    >
      <div class="flex justify-between">
        <img
          src="http://picsum.photos/120"
          class="w-10 h-10 rounded-full hover:opacity-80"
        />

        <i
          class="fas fa-ellipsis-h text-gray-500 hover:bg-blue-50 hover:text-primary p-2 rounded-full w-10 h-10 flex items-center justify-center"
        ></i>
      </div>

      <div class=""><span class="font-bold">DRX</span> 님의 최근 트윗</div>
      <div class="text-gray-500">
        Presents from fans at LoL PARK and D’IVE last week!🎁 Thank you for your
        sincere support. (Presents for DRX Pyosik were also delivered.😢) 지난
        주 롤파크와 D’IVE에서 팬분들이 전해주신 선물!🎁 팬분들의 정성에
        감사드립니다. (표식 선수에게는 따로 전달했습니다.😢)
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style></style>
