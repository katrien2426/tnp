---
layout: default
---

<div class="bg-white bg-opacity-80 p-6 rounded-lg mx-auto my-4 w-9/10 h-9/10">
  <div class="flex items-center justify-center mb-2">
    <h1 class="text-2xl font-bold text-gray-600">特征选择</h1>
  </div>

  <div class="w-full bg-gradient-to-br from-gray-50 to-white rounded-lg p-4">
    <div class="flex items-center mb-3">
      <div class="w-6 h-6 rounded-full bg-blue-100 flex items-center justify-center mr-2">
        <span class="text-blue-500 font-medium">6</span>
      </div>
      <div class="text-lg font-medium text-gray-700">特征间相关性分析</div>
    </div>
    <div class="text-base text-gray-600 mb-4 leading-relaxed" style="text-indent: 2em;">
      通过<span class="text-blue-400 font-medium">相关性分析</span>模型对特征相关性进行分析，我们发现：
      <span class="text-pink-400 font-medium">residential_den</span>和<span class="text-pink-400 font-medium">freq_tran</span>、
      <span class="text-pink-400 font-medium">TripMiles_mean</span>和<span class="text-pink-400 font-medium">TripsSeconds_mean</span>是高度相关的特征对。
    </div>
    <div class="grid grid-cols-2 gap-8">
      <div class="flex justify-center items-start h-[180px] group">
        <img src="/img/heatmaps_2.png?url" alt="优化后的特征相关性热力图" 
          class="h-full w-auto object-contain rounded-lg shadow-md 
          transition-all duration-300 ease-in-out transform 
          group-hover:scale-200 group-hover:shadow-xl"/>
      </div>
      <div class="bg-gradient-to-br from-gray-50 to-white p-2 rounded-lg shadow-sm hover:shadow-md transition-all">
        <ul class="list-disc list-inside space-y-1 text-gray-600">
          <li>相关系数 > 0.8 的特征对：</li>
          <ul class="list-inside ml-6 space-y-0.5 text-gray-500">
            <li>residential_den - <span class="text-pink-400">freq_tran</span></li>
            <li>TripMiles_mean - <span class="text-pink-400">TripsSeconds_mean</span></li>
          </ul>
          <li class="mt-2">根据具体情况<span class="text-blue-400">删除</span>其中一个特征</li>
        </ul>
      </div>
    </div>
  </div>
</div>
