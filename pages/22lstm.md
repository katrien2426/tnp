---
layout: default
---

<div class="bg-white bg-opacity-80 p-6 rounded-lg mx-auto my-4 w-9/10 h-9/10">
  <div class="flex items-center justify-center mb-2">
    <h1 class="text-2xl font-bold text-gray-600">模型假设：LSTM</h1>
  </div>

  <div class="w-full bg-gradient-to-br from-gray-50 to-white rounded-lg p-4">
    <div class="grid grid-cols-2 gap-6">
      <!-- 左侧：结果图 -->
      <div class="bg-gradient-to-br from-gray-50 to-white p-4 rounded-lg shadow-sm flex justify-center items-center">
        <img src="/img/LSTM_result.png" 
          class="w-11/12 h-auto object-contain rounded-lg" 
          alt="LSTM Results"/>
      </div>
      <!-- 右侧：分析内容 -->
      <div class="bg-gradient-to-br from-gray-50 to-white p-4 rounded-lg shadow-sm">
        <div class="space-y-4">
          <!-- 初始考虑 -->
          <div class="flex items-start">
            <div class="w-2 h-2 rounded-full bg-pink-400 mt-2 mr-2 flex-shrink-0"></div>
            <div>
              <span class="text-pink-400 font-medium">初始考虑原因</span>
              <div class="text-base text-gray-600 mt-1">
                需要处理<span class="text-pink-400">节假日</span>、<span class="text-pink-400">天气</span>等时间相关因素
              </div>
            </div>
          </div>
          <!-- 遇到的问题 -->
          <div class="flex items-start">
            <div class="w-2 h-2 rounded-full bg-blue-400 mt-2 mr-2 flex-shrink-0"></div>
            <div>
              <span class="text-blue-400 font-medium">遇到的问题</span>
              <div class="text-base text-gray-600 mt-1">
                数据集按照<span class="text-blue-400">地理位置</span>排序而非时间顺序
              </div>
            </div>
          </div>
          <!-- 最终结果 -->
          <div class="flex items-start">
            <div class="w-2 h-2 rounded-full bg-purple-400 mt-2 mr-2 flex-shrink-0"></div>
            <div>
              <span class="text-purple-400 font-medium">最终结果</span>
              <div class="text-base text-gray-600 mt-1">
                无法正确捕捉<span class="text-purple-400">时间变化规律</span>，效果很差
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
