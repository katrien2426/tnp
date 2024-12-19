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
    <div class="grid grid-cols-2 gap-6">
      <div class="flex justify-center items-start h-[260px] group">
        <img src="/img/heatmaps_3.png?url" alt="最终特征相关性热力图" 
          class="h-full w-auto object-contain rounded-lg shadow-md 
          transition-all duration-300 ease-in-out transform 
          group-hover:scale-180 group-hover:shadow-xl"/>
      </div>
      <div class="bg-gradient-to-br from-gray-50 to-white p-1 rounded-lg shadow-sm hover:shadow-md transition-all">
        <div class="grid grid-cols-2 gap-1">
          <div class="bg-gray-50 p-1.5 rounded-lg text-sm text-gray-600">work_commute_mean</div>
          <div class="bg-gray-50 p-1.5 rounded-lg text-sm text-gray-600">white</div>
          <div class="bg-gray-50 p-1.5 rounded-lg text-sm text-gray-600">pct_18to34</div>
          <div class="bg-gray-50 p-1.5 rounded-lg text-sm text-gray-600">25&over_bachelor...</div>
          <div class="bg-gray-50 p-1.5 rounded-lg text-sm text-gray-600">pct_bachelorORhigher</div>
          <div class="bg-gray-50 p-1.5 rounded-lg text-sm text-gray-600">household_size_mean</div>
          <div class="bg-gray-50 p-1.5 rounded-lg text-sm text-gray-600">median_household_in...</div>
          <div class="bg-gray-50 p-1.5 rounded-lg text-sm text-gray-600">household_zero_vehicle</div>
          <div class="bg-gray-50 p-1.5 rounded-lg text-sm text-gray-600">residential_den</div>
          <div class="bg-gray-50 p-1.5 rounded-lg text-sm text-gray-600">empoloyment_den</div>
          <div class="bg-gray-50 p-1.5 rounded-lg text-sm text-gray-600">network_den</div>
          <div class="bg-gray-50 p-1.5 rounded-lg text-sm text-gray-600">TripMiles_mean</div>
          <div class="bg-gray-50 p-1.5 rounded-lg text-sm text-gray-600">PCA_Population_Factor</div>
          <div class="bg-gray-50 p-1.5 rounded-lg text-sm text-gray-600">TripCount</div>
        </div>
      </div>
    </div>
  </div>
</div>
