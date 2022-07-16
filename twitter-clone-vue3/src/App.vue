<template>
  <div class="flex h-screen">
    <!-- left side bar section -->
    <div
      class="w-1/4 pt-5 ml-10 flex flex-col justify-between border-r border-gray-100"
    >
      <div class="flex flex-col items-center lg:items-start">
        <!-- twitter logo -->
        <i class="fa-brands fa-twitter text-3xl text-primary lg:ml-4 mb-3"></i>

        <!-- left side menu icons -->
        <div class="flex flex-col items-start">
          <div
            class="hover:text-primary hover:bg-blue-50 px-4 py-2 rounded-full"
          >
            <i class="fas fa-home fa-fw text-2xl"></i>
            <span class="ml-5 text-lg hidden lg:inline-block">홈</span>
          </div>

          <div
            class="hover:text-primary hover:bg-blue-50 px-4 py-2 rounded-full"
          >
            <i class="fas fa-hashtag fa-fw text-2xl"></i>
            <span class="ml-5 text-lg hidden lg:inline-block">탐색하기</span>
          </div>

          <div
            class="hover:text-primary hover:bg-blue-50 px-4 py-2 rounded-full"
          >
            <i class="far fa-bell fa-fw text-2xl"></i>
            <span class="ml-5 text-lg hidden lg:inline-block">알림</span>
          </div>

          <div
            class="hover:text-primary hover:bg-blue-50 px-4 py-2 rounded-full"
          >
            <i class="far fa-envelope fa-fw text-2xl"></i>
            <span class="ml-5 text-lg hidden lg:inline-block">쪽지</span>
          </div>

          <div
            class="hover:text-primary hover:bg-blue-50 px-4 py-2 rounded-full"
          >
            <i class="far fa-bookmark fa-fw text-2xl"></i>
            <span class="ml-5 text-lg hidden lg:inline-block">북마크</span>
          </div>

          <div
            class="hover:text-primary hover:bg-blue-50 px-4 py-2 rounded-full"
          >
            <i class="far fa-list-alt fa-fw text-2xl"></i>
            <span class="ml-5 text-lg hidden lg:inline-block">리스트</span>
          </div>

          <div
            class="hover:text-primary hover:bg-blue-50 px-4 py-2 rounded-full"
          >
            <i class="far fa-user fa-fw text-2xl"></i>
            <span class="ml-5 text-lg hidden lg:inline-block">프로필</span>
          </div>

          <div
            class="hover:text-primary hover:bg-blue-50 px-4 py-2 rounded-full"
          >
            <i class="fas fa-ellipsis-h fa-fw text-2xl"></i>
            <span class="ml-5 text-lg hidden lg:inline-block">더보기</span>
          </div>
        </div>

        <!-- tweet button -->
        <div class="w-full lg:pr-3 flex justify-center">
          <button
            class="mt-3 bg-primary text-white lg:w-full w-12 h-12 rounded-full hover:bg-dark"
          >
            <span class="hidden lg:block">트윗</span>
            <i class="fas fa-plus lg:hidden"></i>
          </button>
        </div>
      </div>

      <!-- profile button -->
      <div class="lg:pr-3 mb-3">
        <button
          class="hidden lg:flex mt-3 px-2 py-1 w-full h-12 rounded-full hover:bg-blue-50 items-center"
        >
          <img src="https://picsum.photos/100" class="w-10 h-10 rounded-full" />

          <div class="lg:ml-2 hidden lg:block">
            <div class="text-sm font-bold">benkang.com</div>
            <div class="text-xs text-gray-500 text-left">@benkang</div>
          </div>

          <i
            class="ml-auto fas fa-ellipsis-h fa-fw text-xs hidden lg:block"
          ></i>
        </button>

        <div class="lg:hidden flex justify-center">
          <img
            src="https://picsum.photos/100"
            class="w-10 h-10 rounded-full cursor-pointer hover:opacity-80"
          />
        </div>
      </div>
    </div>

    <!-- right main screen -->
    <div class="flex-1">
      <div class="flex h-screen">
        <!-- main section -->
        <div class="flex-1 border-r border-gray-100 overflow-y-auto">
          <div class="flex flex-col">
            <!-- page title -->
            <div class="border-b border-gray-100 px-3 py-2 font-bold text-lg">
              홈
            </div>

            <!-- tweeting section -->
            <div class="flex px-3 py-3 border-b-8 border-gray-100">
              <img
                src="http://picsum.photos/200"
                class="w-10 h-10 rounded-full hover:opacity-80 cursor-pointer"
              />

              <div class="ml-2 flex-1 flex flex-col">
                <textarea
                  placeholder="무슨 일이 일어나고 있나요?"
                  class="w-full text-lg font-bold focus:outline-none mb-3 resize-none"
                ></textarea>

                <div class="text-right">
                  <button
                    class="bg-primary hover:bg-dark text-sm font-bold text-white px-4 py-1 rounded-full"
                  >
                    트윗
                  </button>
                </div>
              </div>
            </div>

            <!-- tweets section -->
            <div
              class="flex px-3 py-3 border-b border-gray-100"
              v-for="tweet in 10"
              :key="tweet"
            >
              <img
                src="http://picsum.photos/200"
                class="w-10 h-10 rounded-full hover:opacity-80 cursor-pointer"
              />

              <div class="ml-3 flex-1 flex flex-col space-y-1">
                <!-- tweet title -->
                <div class="text-sm space-x-1">
                  <span class="font-bold">T1 LoL</span>
                  <span class="text-gray-500 text-xs">@T1LoL</span>
                  <span class="">·</span>
                  <span class="text-gray-500 text-xs">1시간</span>
                </div>

                <!-- tweet body -->
                <div class="">
                  [2022 #LCK Summer R2 M10 vs. DRX] 서머의 전환점, 2라운드의
                  시작! 이번 라운드도 T1 다운 모습 보여드리겠습니다. The second
                  Round starts NOW! We will show everyone what T1 is made of.
                  ⏰8 PM KST #T1WIN #T1Fighting
                </div>

                <!-- tweet actions -->
                <div class="flex justify-between">
                  <div class="text-gray-500 hover:text-primary">
                    <i
                      class="far fa-comment hover:bg-blue-50 rounded-full p-2"
                    ></i>
                    <span class="ml-1 text-sm">1</span>
                  </div>

                  <div class="text-gray-500 hover:text-green-500">
                    <i
                      class="fas fa-retweet hover:bg-green-50 rounded-full p-2"
                    ></i>
                    <span class="ml-1 text-sm">2</span>
                  </div>

                  <div class="text-gray-500 hover:text-red-500">
                    <i
                      class="far fa-heart hover:bg-red-50 rounded-full p-2"
                    ></i>
                    <span class="ml-1 text-sm">3</span>
                  </div>

                  <div class="text-gray-500 hover:text-primary">
                    <i
                      class="far fa-share-square hover:bg-blue-50 rounded-full p-2"
                    ></i>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- trend section -->
        <!-- <div class="hidden lg:block lg:w-2/5 px-4 py-2"> -->
        <div class="w-2/5 px-4 py-2">
          <!-- tweet search input section -->
          <div class="relative mb-5">
            <input
              placeholder="트위터 검색"
              type="text"
              class="pl-10 rounded-full w-full p-2 bg-gray-100 text-sm focus:ring-1 focus:ring-primary focus:bg-white focus:outline-none"
            />

            <i
              class="fas fa-search absolute left-0 mt-2 ml-3 text-sm text-light"
            ></i>
          </div>

          <!-- trend for me -->
          <div class="w-full rounded-xl bg-gray-50 flex flex-col">
            <!-- for me setting nav title -->
            <div
              class="flex items-center justify-between px-3 py-1 border-b border-gray-100"
            >
              <span class="text-lg font-bold">나를 위한 트렌드</span>
              <i
                class="text-center fas fa-cog text-lg text-primary hover:bg-blue-50 p-2 rounded-full w-10 h-10"
              ></i>
            </div>

            <!-- recommend trend lists -->
            <div
              class="border-b border-gray-100 hover:bg-gray-100 px-4 py-2 cursor-pointer"
              v-for="trend in 3"
              :key="trend"
            >
              <div class="flex">
                <div class="flex-1 flex flex-col">
                  <div class="text-gray-500">대한민국에서 트렌드 중</div>
                  <div class="font-bold text-lg">러블리즈</div>
                  <div class="text-gray-500">3,564 트윗</div>
                </div>
                <i class="fas fa-ellipsis-h text-gray-500"></i>
              </div>
            </div>

            <!-- more -->
            <div class="px-4 py-2 hover:bg-gray-100">
              <span class="text-primary text-lg rounded-xl">더 보기</span>
            </div>
          </div>

          <!-- recommend follows -->
          <div class="mt-5 w-full rounded-xl bg-gray-50 flex flex-col">
            <!-- for me setting -->
            <div class="px-3 py-3 border-b border-gray-100">
              <span class="text-lg font-bold">팔로우 추천</span>
            </div>

            <!-- recommend follow lists -->
            <div
              class="border-b border-gray-100 hover:bg-gray-100 px-4 py-2 cursor-pointer"
              v-for="follow in 3"
              :key="follow"
            >
              <div class="flex items-center">
                <div class="">
                  <img
                    src="http://picsum.photos/200"
                    class="w-12 h-12 rounded-full mr-2"
                  />
                </div>

                <div class="flex-1 flex flex-col">
                  <div class="font-bold text-lg">윤석열</div>
                  <div class="text-gray-500">@president_of_korea</div>
                </div>
                <div class="">
                  <button
                    class="border-2 border-primary hover:bg-blue-100 px-4 py-1 rounded-full text-primary"
                  >
                    팔로우
                  </button>
                </div>
              </div>
            </div>

            <!-- more -->
            <div class="px-4 py-2 hover:bg-gray-100">
              <span class="text-primary text-lg rounded-xl">더 보기</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style></style>
