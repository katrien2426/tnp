---
layout: default
---

<div class="bg-white bg-opacity-80 p-6 rounded-lg mx-auto my-4 w-9/10 h-9/10">
  <div class="flex items-center justify-center mb-2">
    <h1 class="text-xl font-bold text-gray-600">模型假设：图神经网络</h1>
  </div>

  <div class="w-full bg-gradient-to-br from-gray-50 to-white rounded-lg p-2">
    <div class="grid grid-cols-2 gap-6">
      <!-- 左侧：结果图 -->
      <div class="bg-gradient-to-br from-gray-50 to-white p-2 rounded-lg shadow-sm flex justify-center items-center">
        <img src="/img/GNN_R^2.png" 
          class="w-full h-auto object-contain rounded-lg" 
          alt="GNN R^2 Score"/>
      </div>
      <!-- 右侧：分析内容 -->
      <div class="bg-gradient-to-br from-gray-50 to-white p-2 rounded-lg shadow-sm">
        <div class="space-y-4">
          <!-- 初始考虑 -->
          <div class="flex items-start">
            <div class="w-2 h-2 rounded-full bg-pink-400 mt-2 mr-2 flex-shrink-0"></div>
            <div>
              <span class="text-pink-400 font-medium">初始考虑原因</span>
              <div class="text-base text-gray-600 mt-1">
                期望通过<span class="text-pink-400">地理邻接关系</span>挖掘节点间的相关性
              </div>
            </div>
          </div>
          <!-- 遇到的问题 -->
          <div class="flex items-start">
            <div class="w-2 h-2 rounded-full bg-blue-400 mt-1 mr-2 flex-shrink-0"></div>
            <div>
              <span class="text-blue-400 font-medium">遇到的问题</span>
              <div class="text-base text-gray-600 mt-1">
                <span class="text-blue-400">R²始终为负值</span>，说明模型预测结果比使用平均值来预测还要差
              </div>
            </div>
          </div>
          <!-- 可能原因 -->
          <div class="flex items-start">
            <div class="w-2 h-2 rounded-full bg-green-400 mt-2 mr-2 flex-shrink-0"></div>
            <div>
              <span class="text-green-400 font-medium">可能原因</span>
              <div class="text-base text-gray-600 mt-0.5">
                <ul class="list-disc ml-3 space-y-0.5">
                  <li>缺乏能<span class="text-green-400">有效区分</span>节点特性的高质量特征</li>
                  <li><span class="text-green-400">邻接矩阵</span>构造未能准确反映节点关系</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
