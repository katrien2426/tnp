---
layout: default
---

<div class="bg-white bg-opacity-80 p-6 pb-4 rounded-lg mx-auto my-4 w-9/10">
  <div class="flex items-center justify-center mb-3">
    <h1 class="text-2xl font-bold text-gray-600">模型构建：全连接神经网络</h1>
  </div>

  <div class="w-full bg-gradient-to-br from-gray-50 to-white rounded-lg p-4 pb-3">
    <div class="flex items-center mb-3">
      <div class="w-6 h-6 rounded-full bg-blue-100 flex items-center justify-center mr-2">
        <span class="text-blue-500 font-medium">6</span>
      </div>
      <div class="text-lg font-medium text-gray-700">预测结果分析</div>
    </div>
    <div class="grid grid-cols-2 gap-6">
      <!-- 左侧：预测结果图 -->
      <div class="bg-gradient-to-br from-gray-50 to-white p-3 rounded-lg shadow-sm">
        <div class="flex items-center justify-center">
          <img src="/img/result.png" class="w-full rounded-lg shadow-sm" alt="Prediction Results">
        </div>
        <div class="text-sm text-gray-500 mt-2 px-1">
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;上图展示了模型预测值（蓝色）与真实值（橙色）的对比，可以看出预测曲线与实际数据走势基本吻合。
        </div>
      </div>
      <!-- 右侧：详细分析 -->
      <div class="bg-gradient-to-br from-gray-50 to-white p-3 rounded-lg shadow-sm space-y-3">
        <!-- MSE分析 -->
        <div class="bg-gradient-to-r from-gray-50 to-white rounded-lg p-3">
          <div class="flex items-center mb-1">
            <div class="w-2 h-2 rounded-full bg-pink-400 mr-2"></div>
            <span class="text-pink-400 font-medium">均方误差 (MSE)</span>
            <span class="ml-auto text-lg font-semibold text-pink-400">0.3388</span>
          </div>
          <div class="text-sm text-gray-600 ml-4">
            预测值与实际值的平均偏差较小，说明模型预测准确度高。
          </div>
        </div>
        <!-- R²分析 -->
        <div class="bg-gradient-to-r from-gray-50 to-white rounded-lg p-3">
          <div class="flex items-center mb-1">
            <div class="w-2 h-2 rounded-full bg-blue-400 mr-2"></div>
            <span class="text-blue-400 font-medium">决定系数 (R²)</span>
            <span class="ml-auto text-lg font-semibold text-blue-400">0.9148</span>
          </div>
          <div class="text-sm text-gray-600 ml-4">
            表明模型解释了数据中91.48%的变化，具有很强的预测能力。
          </div>
        </div>
      </div>
    </div>
  </div>
</div>