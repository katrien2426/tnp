---
layout: default
---

<div class="bg-white bg-opacity-80 p-6 pb-4 rounded-lg mx-auto my-4 w-9/10">
  <div class="flex items-center justify-center mb-2">
    <h1 class="text-2xl font-bold text-gray-600">模型构建：全连接神经网络</h1>
  </div>

  <div class="w-full bg-gradient-to-br from-gray-50 to-white rounded-lg p-3 pb-2">
    <div class="flex items-center mb-2">
      <div class="w-6 h-6 rounded-full bg-blue-100 flex items-center justify-center mr-2">
        <span class="text-blue-500 font-medium">1</span>
      </div>
      <div class="text-lg font-medium text-gray-700">模型架构设计</div>
    </div>
    <div class="grid grid-cols-2 gap-4">
      <!-- 左侧：网络结构图 -->
      <div class="bg-gradient-to-br from-gray-50 to-white p-2 rounded-lg shadow-sm">
        <svg width="100%" height="240" viewBox="0 0 400 300" class="mx-auto">
          <!-- 输入层 -->
          <g transform="translate(50,50)">
            <rect x="-30" y="-20" width="60" height="240" fill="#fecaca" opacity="0.3" rx="5"/>
            <text x="0" y="-30" text-anchor="middle" fill="#374151">输入层</text>
            <circle cx="0" cy="0" r="15" fill="#f87171" opacity="0.8"/>
            <circle cx="0" cy="50" r="15" fill="#f87171" opacity="0.8"/>
            <circle cx="0" cy="100" r="15" fill="#f87171" opacity="0.8"/>
            <text x="0" y="150" text-anchor="middle" fill="#374151">...</text>
            <circle cx="0" cy="200" r="15" fill="#f87171" opacity="0.8"/>
          </g>
          <!-- 隐藏层1 -->
          <g transform="translate(170,50)">
            <rect x="-30" y="-20" width="60" height="240" fill="#bfdbfe" opacity="0.3" rx="5"/>
            <text x="0" y="-30" text-anchor="middle" fill="#374151">隐藏层1</text>
            <circle cx="0" cy="0" r="15" fill="#60a5fa" opacity="0.8"/>
            <circle cx="0" cy="50" r="15" fill="#60a5fa" opacity="0.8"/>
            <circle cx="0" cy="100" r="15" fill="#60a5fa" opacity="0.8"/>
            <text x="0" y="150" text-anchor="middle" fill="#374151">128个</text>
            <circle cx="0" cy="200" r="15" fill="#60a5fa" opacity="0.8"/>
          </g>
          <!-- 隐藏层2 -->
          <g transform="translate(290,50)">
            <rect x="-30" y="-20" width="60" height="240" fill="#bfdbfe" opacity="0.3" rx="5"/>
            <text x="0" y="-30" text-anchor="middle" fill="#374151">隐藏层2</text>
            <circle cx="0" cy="0" r="15" fill="#60a5fa" opacity="0.8"/>
            <circle cx="0" cy="50" r="15" fill="#60a5fa" opacity="0.8"/>
            <circle cx="0" cy="100" r="15" fill="#60a5fa" opacity="0.8"/>
            <text x="0" y="150" text-anchor="middle" fill="#374151">128个</text>
            <circle cx="0" cy="200" r="15" fill="#60a5fa" opacity="0.8"/>
          </g>
          <!-- 输出层 -->
          <g transform="translate(380,130)">
            <rect x="-20" y="-20" width="40" height="40" fill="#86efac" opacity="0.3" rx="5"/>
            <text x="0" y="-30" text-anchor="middle" fill="#374151">输出层</text>
            <circle cx="0" cy="0" r="15" fill="#34d399" opacity="0.8"/>
          </g>
          <!-- 连接线 -->
          <g stroke="#9ca3af" stroke-width="1" opacity="0.2">
            <!-- 输入层到隐藏层1 -->
            <line x1="65" y1="50" x2="155" y2="50"/>
            <line x1="65" y1="50" x2="155" y2="100"/>
            <line x1="65" y1="100" x2="155" y2="50"/>
            <line x1="65" y1="100" x2="155" y2="100"/>
            <line x1="65" y1="200" x2="155" y2="200"/>
            <line x1="65" y1="200" x2="155" y2="150"/>
            <!-- 隐藏层1到隐藏层2 -->
            <line x1="185" y1="50" x2="275" y2="50"/>
            <line x1="185" y1="50" x2="275" y2="100"/>
            <line x1="185" y1="100" x2="275" y2="50"/>
            <line x1="185" y1="100" x2="275" y2="100"/>
            <line x1="185" y1="200" x2="275" y2="200"/>
            <line x1="185" y1="200" x2="275" y2="150"/>
            <!-- 隐藏层2到输出层 -->
            <line x1="305" y1="50" x2="365" y2="130"/>
            <line x1="305" y1="100" x2="365" y2="130"/>
            <line x1="305" y1="150" x2="365" y2="130"/>
            <line x1="305" y1="200" x2="365" y2="130"/>
          </g>
        </svg>
      </div>
      <!-- 右侧：网络配置说明 -->
      <div class="bg-gradient-to-br from-gray-50 to-white p-2 rounded-lg shadow-sm space-y-3">
        <!-- 网络结构 -->
        <div class="bg-gradient-to-r from-gray-50 to-white rounded-lg p-2">
          <div class="flex items-center mb-1">
            <div class="w-2 h-2 rounded-full bg-pink-400 mr-2"></div>
            <span class="text-pink-400 font-medium">网络结构</span>
          </div>
          <ul class="list-disc ml-4 space-y-0.5 text-sm text-gray-600">
            <li>输入层：特征维度大小</li>
            <li>隐藏层1：128个神经元 + ReLU激活</li>
            <li>隐藏层2：128个神经元 + ReLU激活</li>
          </ul>
        </div>
        <!-- 优化设置 -->
        <div class="bg-gradient-to-r from-gray-50 to-white rounded-lg p-2">
          <div class="flex items-center mb-1">
            <div class="w-2 h-2 rounded-full bg-blue-400 mr-2"></div>
            <span class="text-blue-400 font-medium">优化设置</span>
          </div>
          <ul class="list-disc ml-4 space-y-0.5 text-sm text-gray-600">
            <li>损失函数：均方误差（MSE）</li>
            <li>优化器：Adam (lr=0.001)</li>
            <li>批次大小：32</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>
