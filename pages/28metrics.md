---
layout: default
---

<div class="bg-white bg-opacity-80 p-6 pb-4 rounded-lg mx-auto my-4 w-9/10">
  <div class="flex items-center justify-center mb-2">
    <h1 class="text-2xl font-bold text-gray-600">模型构建：全连接神经网络</h1>
  </div>

  <div class="w-full bg-gradient-to-br from-gray-50 to-white rounded-lg p-3 pb-2">
    <div class="grid grid-cols-2 gap-4">
      <!-- 左侧：训练数据表格 -->
      <div class="bg-gradient-to-br from-gray-50 to-white p-2 rounded-lg shadow-sm">
        <div class="flex items-center mb-2">
          <div class="w-6 h-6 rounded-full bg-blue-100 flex items-center justify-center mr-2">
            <span class="text-blue-500 font-medium">4</span>
          </div>
          <div class="text-lg font-medium text-gray-700">训练过程数据</div>
        </div>
        <div class="overflow-x-auto">
          <table class="min-w-full text-sm">
            <thead>
              <tr class="text-gray-600 border-b">
                <th class="py-1 text-left font-medium">Epoch</th>
                <th class="py-1 text-left font-medium">Loss</th>
                <th class="py-1 text-left font-medium">R²</th>
                <th class="py-1 text-left font-medium">Val Loss</th>
                <th class="py-1 text-left font-medium">Val R²</th>
              </tr>
            </thead>
            <tbody class="text-gray-600">
              <tr class="border-b hover:bg-gray-50">
                <td class="py-1">1</td>
                <td class="py-1">0.0701</td>
                <td class="py-1">-2.0892</td>
                <td class="py-1">0.0273</td>
                <td class="py-1">0.0185</td>
              </tr>
              <tr class="border-b hover:bg-gray-50">
                <td class="py-1">2</td>
                <td class="py-1">0.0136</td>
                <td class="py-1">0.4027</td>
                <td class="py-1">0.0080</td>
                <td class="py-1">0.7119</td>
              </tr>
              <tr class="text-center border-b hover:bg-gray-50">
                <td colspan="5" class="py-1">...</td>
              </tr>
              <tr class="border-b hover:bg-gray-50">
                <td class="py-1">69</td>
                <td class="py-1">0.0027</td>
                <td class="py-1">0.8823</td>
                <td class="py-1">0.0026</td>
                <td class="py-1">0.9072</td>
              </tr>
              <tr class="hover:bg-gray-50">
                <td class="py-1">70</td>
                <td class="py-1">0.0025</td>
                <td class="py-1">0.8904</td>
                <td class="py-1">0.0024</td>
                <td class="py-1">0.9148</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      <!-- 右侧：R^2曲线图和性能指标 -->
      <div class="bg-gradient-to-br from-gray-50 to-white p-2 rounded-lg shadow-sm">
        <div class="flex items-center mb-1">
          <div class="w-6 h-6 rounded-full bg-blue-100 flex items-center justify-center mr-2">
            <span class="text-blue-500 font-medium">5</span>
          </div>
          <div class="text-lg font-medium text-gray-700">模型性能分析</div>
        </div>
        <div class="flex flex-col">
          <div class="flex items-center justify-center">
            <img src="/img/R^2.png" class="w-11/12 rounded-lg shadow-sm mt-1" alt="Training Curves">
          </div>
          <div class="bg-gradient-to-r from-gray-50 to-white rounded-lg p-2">
            <div class="flex items-center mb-1">
              <div class="w-2 h-2 rounded-full bg-pink-400 mr-2"></div>
              <span class="text-pink-400 font-medium">最终性能指标</span>
            </div>
            <div class="grid grid-cols-2 gap-3">
              <div>
                <div class="text-base text-center text-gray-500">均方误差 (MSE)</div>
                <div class="text-lg text-center font-semibold text-gray-700">0.3388</div>
              </div>
              <div>
                <div class="text-base text-center text-gray-500">R² 分数</div>
                <div class="text-lg text-center font-semibold text-gray-700">0.9148</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
