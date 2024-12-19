---
layout: default
---

<div class="bg-white bg-opacity-80 p-6 rounded-lg mx-auto my-4 w-9/10 h-9/10">
  <div class="flex items-center justify-center mb-1">
    <h1 class="text-2xl font-bold text-gray-600">特征选择</h1>
  </div>

  <div class="w-full bg-gradient-to-br from-gray-50 to-white rounded-lg shadow-sm p-2">
    <div class="flex items-center mb-1">
      <div class="w-5 h-5 rounded-full bg-blue-100 flex items-center justify-center mr-2">
        <span class="text-blue-500 font-medium text-sm">3</span>
      </div>
      <div class="text-lg font-medium text-gray-700">计算各特征值贡献度</div>
    </div>
    <div class="grid grid-cols-3 gap-2">
      <div class="col-span-2 relative bg-white rounded-lg">
        <img class="w-full h-full object-contain" src="/img/feature_importance_process.gif" alt="Feature Importance Process">
      </div>
      <div class="flex flex-col gap-3">
        <div class="bg-gradient-to-r from-blue-50 to-blue-100 p-1.5 rounded-lg transform hover:scale-102 transition-all duration-200">
          <div class="font-bold text-blue-600 mb-1 text-sm">1. 树结构构建</div>
          <div class="text-sm text-gray-600">通过节点分裂来拟合数据</div>
        </div>
        <div class="bg-gradient-to-r from-green-50 to-green-100 p-1.5 rounded-lg transform hover:scale-102 transition-all duration-200">
          <div class="font-bold text-green-600 mb-1 text-sm">2. 特征置换</div>
          <div class="text-sm text-gray-600">随机打乱特征值，观察变化</div>
        </div>
        <div class="bg-gradient-to-r from-purple-50 to-purple-100 p-1.5 rounded-lg transform hover:scale-102 transition-all duration-200">
          <div class="font-bold text-purple-600 mb-1 text-sm">3. 重要性评估</div>
          <div class="text-sm text-gray-600">计算置换前后预测差异</div>
        </div>
        <div class="bg-gradient-to-r from-pink-50 to-pink-100 p-1.5 rounded-lg transform hover:scale-102 transition-all duration-200">
          <div class="font-bold text-pink-600 mb-1 text-sm">4. 贡献度排序</div>
          <div class="text-sm text-gray-600">根据重要性得分排序</div>
        </div>
      </div>
    </div>
  </div>
</div>