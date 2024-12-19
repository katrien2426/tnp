---
layout: default
---

<div class="bg-white bg-opacity-80 p-6 rounded-lg mx-auto my-4 w-9/10 h-9/10">
  <div class="flex items-center justify-center mb-2">
    <h1 class="text-2xl font-bold text-gray-600">目标变量分析</h1>
  </div>

  <div class="w-full bg-gradient-to-br from-gray-50 to-white rounded-lg p-4">
    <div class="flex items-center mb-3">
      <div class="w-6 h-6 rounded-full bg-blue-100 flex items-center justify-center mr-2">
        <span class="text-blue-500 font-medium">1</span>
      </div>
      <div class="text-lg font-medium text-gray-700">原始分析</div>
    </div>
    <div class="grid grid-cols-2 gap-6">
      <!-- 左侧：分布图 -->
      <div class="bg-gradient-to-br from-gray-50 to-white p-4 rounded-lg shadow-sm flex justify-center items-center">
        <img src="/img/TripCount_1.png" 
          class="w-11/12 h-auto object-contain rounded-lg" 
          alt="Original Distribution"/>
      </div>
      <!-- 右侧：分析内容 -->
      <div class="bg-gradient-to-br from-gray-50 to-white p-3 rounded-lg shadow-sm">
        <div class="text-base text-gray-600">
          <div class="flex items-center mb-1">
            <div class="w-2 h-2 rounded-full bg-pink-400 mr-2"></div>
            <span class="text-pink-400 font-medium">分布特点</span>
          </div>
          <ul class="list-disc ml-5 mt-1 mb-4 space-y-1 text-base">
            <li>呈现明显的<span class="text-pink-400">长尾分布</span>，存在较长的右尾</li>
            <li>大量数据集中在低值区域，少数样本出现极大值</li>
          </ul>
          <div class="flex items-center mb-1">
            <div class="w-2 h-2 rounded-full bg-blue-400 mr-2"></div>
            <span class="text-blue-400 font-medium">处理方案</span>
          </div>
          <ul class="list-disc ml-5 mt-1 space-y-1 text-base">
            <li>采用<span class="text-blue-400">对数变换</span>y = log(x + 1)处理数据</li>
            <li>减弱异常值影响，保留数据的相对关系</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>
