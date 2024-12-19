---
layout: default
---

<div class="bg-white bg-opacity-80 p-6 rounded-lg mx-auto my-4 w-9/10 h-9/10">
  <div class="flex items-center justify-center mb-2">
    <h1 class="text-2xl font-bold text-gray-600">模型构建：全连接神经网络</h1>
  </div>

  <div class="w-full bg-gradient-to-br from-gray-50 to-white rounded-lg p-4 pb-1">
    <div class="grid grid-cols-3 gap-6">
      <!-- 左侧：数据处理流程图 -->
      <div class="bg-gradient-to-br from-gray-50 to-white p-2 rounded-lg shadow-sm">
        <div class="flex items-center mb-3">
          <div class="w-6 h-6 rounded-full bg-blue-100 flex items-center justify-center mr-2">
            <span class="text-blue-500 font-medium">2</span>
          </div>
          <div class="text-lg font-medium text-gray-700">数据预处理流程</div>
        </div>
        <svg width="250" height="250" viewBox="0 0 400 400">
          <defs>
            <marker id="arrowhead" markerWidth="10" markerHeight="7" 
                  refX="9" refY="3.5" orient="auto">
              <polygon points="0 0, 10 3.5, 0 7" fill="#4b5563"/>
            </marker>
          </defs>
          <!-- 原始数据 -->
          <g transform="translate(150,80)">
            <rect x="-90" y="-25" width="180" height="50" fill="#fecaca" rx="5" opacity="0.8"/>
            <text x="0" y="0" text-anchor="middle" fill="#374151" dominant-baseline="middle">原始数据</text>
          </g>
          <!-- 数据清洗 -->
          <g transform="translate(150,160)">
            <rect x="-90" y="-25" width="180" height="50" fill="#bfdbfe" rx="5" opacity="0.8"/>
            <text x="0" y="0" text-anchor="middle" fill="#374151" dominant-baseline="middle">移除非数值列</text>
          </g>
          <!-- 特征处理 -->
          <g transform="translate(150,240)">
            <rect x="-90" y="-25" width="180" height="50" fill="#c7d2fe" rx="5" opacity="0.8"/>
            <text x="0" y="0" text-anchor="middle" fill="#374151" dominant-baseline="middle">MinMaxScaler标准化</text>
          </g>
          <!-- 数据集划分 -->
          <g transform="translate(150,320)">
            <rect x="-90" y="-25" width="180" height="50" fill="#86efac" rx="5" opacity="0.8"/>
            <text x="0" y="0" text-anchor="middle" fill="#374151" dominant-baseline="middle">训练集/测试集划分</text>
          </g>
          <!-- 连接箭头 -->
          <g stroke="#4b5563" stroke-width="2" marker-end="url(#arrowhead)">
            <line x1="150" y1="105" x2="150" y2="125"/>
            <line x1="150" y1="185" x2="150" y2="205"/>
            <line x1="150" y1="265" x2="150" y2="285"/>
          </g>
        </svg>
      </div>
      <!-- 右侧：训练过程分析 -->
      <div class="col-span-2 bg-gradient-to-br from-gray-50 to-white p-2 rounded-lg shadow-sm">
        <div class="flex items-center mb-3">
          <div class="w-6 h-6 rounded-full bg-blue-100 flex items-center justify-center mr-2">
            <span class="text-blue-500 font-medium">3</span>
          </div>
          <div class="text-lg font-medium text-gray-700">训练过程分析</div>
        </div>
        <div class="space-y-4">
          <!-- 训练策略 -->
          <div class="flex items-start">
            <div class="w-2 h-2 rounded-full bg-red-400 mt-2 mr-2 flex-shrink-0"></div>
            <div class="w-full">
              <span class="text-red-400 font-medium">训练策略</span>
              <div class="grid grid-cols-2 gap-4 mt-1">
                <div class="text-sm text-gray-600">
                  • 训练轮次：<span class="text-red-400">70</span> epochs
                </div>
                <div class="text-sm text-gray-600">
                  • 同时监控训练集验证集的损失
                </div>
              </div>
            </div>
          </div>
          <!-- 收敛分析 -->
          <div class="grid grid-cols-3 gap-2">
            <div class="flex items-start">
              <div class="w-2 h-2 rounded-full bg-blue-400 mt-2 mr-2 flex-shrink-0"></div>
              <div>
                <span class="text-blue-400 font-medium">收敛分析</span>
                <ul class="list-disc ml-4 mt-1 space-y-1 text-sm text-gray-600">
                  <li>训练/测试损失稳定下降</li>
                  <li>未出现明显的过拟合现象</li>
                </ul>
              </div>
            </div>
            <div class="col-span-2">
              <img src="/img/loss.png" class="w-full rounded-lg shadow-sm" alt="Training Process">
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
