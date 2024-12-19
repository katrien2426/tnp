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
      通过对特征之间的相关性分析，我们发现部分<span class="text-pink-400 font-medium">人口相关特征</span>之间存在较强的相关性，
      包括年龄、人口总数、家庭数量等指标。为了降低特征间的冗余性，我们采用了<span class="text-blue-400 font-medium">PCA</span>
      降维处理方法。
    </div>
    <div class="grid grid-cols-2 gap-8">
      <div class="flex justify-center items-start h-[180px] group">
        <img src="/img/heatmaps_1.png?url" alt="特征相关性热力图" 
          class="h-full w-auto object-contain rounded-lg shadow-md 
          transition-all duration-300 ease-in-out transform 
          group-hover:scale-200 group-hover:shadow-xl"/>
      </div>
      <div class="bg-gradient-to-br from-gray-50 to-white p-4 rounded-lg shadow-sm hover:shadow-md transition-all">
        <ul class="list-disc list-inside space-y-1 text-gray-600">
          <ul class="list-inside ml-6 space-y-0.5 text-gray-500">
            <li>age_18to34</li>
            <li>population_25&over</li>
            <li>total_population</li>
            <li>total_household</li>
          </ul>
        </ul>
      </div>
    </div>
  </div>
</div>
