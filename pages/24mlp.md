---
layout: default
---

<div class="bg-white bg-opacity-80 p-6 rounded-lg mx-auto my-4 w-9/10 h-9/10">
  <div class="flex items-center justify-center mb-2">
    <h1 class="text-2xl font-bold text-gray-600">模型构建：全连接神经网络</h1>
  </div>

  <div class="w-full bg-gradient-to-br from-gray-50 to-white rounded-lg p-4">
    <div class="grid grid-cols-2 gap-6">
      <!-- 左侧：网络结构图 -->
      <div class="bg-gradient-to-br from-gray-50 to-white p-4 rounded-lg shadow-sm">
        <svg width="320" height="260" viewBox="0 0 400 300">
          <!-- 输入层 -->
          <g transform="translate(50,50)">
            <circle cx="0" cy="0" r="15" fill="#f87171" opacity="0.8"/>
            <circle cx="0" cy="75" r="15" fill="#f87171" opacity="0.8"/>
            <circle cx="0" cy="150" r="15" fill="#f87171" opacity="0.8"/>
            <circle cx="0" cy="200" r="15" fill="#f87171" opacity="0.8"/>
            <text x="-40" y="100" fill="#374151" class="text-sm">输入层</text>
            <text x="-25" y="0" fill="#666" class="text-xs">x₁</text>
            <text x="-25" y="75" fill="#666" class="text-xs">x₂</text>
            <text x="-25" y="150" fill="#666" class="text-xs">x₃</text>
            <text x="-25" y="200" fill="#666" class="text-xs">x₄</text>
          </g>
          <!-- 隐藏层1 -->
          <g transform="translate(150,50)">
            <circle cx="0" cy="0" r="15" fill="#60a5fa" opacity="0.8"/>
            <circle cx="0" cy="75" r="15" fill="#60a5fa" opacity="0.8"/>
            <circle cx="0" cy="150" r="15" fill="#60a5fa" opacity="0.8"/>
            <text x="-40" y="100" fill="#374151" class="text-sm">隐藏层</text>
            <text x="-25" y="0" fill="#666" class="text-xs">h₁₁</text>
            <text x="-25" y="75" fill="#666" class="text-xs">h₁₂</text>
            <text x="-25" y="150" fill="#666" class="text-xs">h₁₃</text>
            <text x="-60" y="30" fill="#666" class="text-xs">w₁₁</text>
            <text x="-60" y="100" fill="#666" class="text-xs">w₁₂</text>
          </g>
          <!-- 隐藏层2 -->
          <g transform="translate(250,50)">
            <circle cx="0" cy="0" r="15" fill="#60a5fa" opacity="0.8"/>
            <circle cx="0" cy="75" r="15" fill="#60a5fa" opacity="0.8"/>
            <circle cx="0" cy="150" r="15" fill="#60a5fa" opacity="0.8"/>
            <text x="-25" y="0" fill="#666" class="text-xs">h₂₁</text>
            <text x="-25" y="75" fill="#666" class="text-xs">h₂₂</text>
            <text x="-25" y="150" fill="#666" class="text-xs">h₂₃</text>
          </g>
          <!-- 输出层 -->
          <g transform="translate(350,100)">
            <circle cx="0" cy="0" r="15" fill="#34d399" opacity="0.8"/>
            <text x="-40" y="50" fill="#374151" class="text-sm">输出层</text>
            <text x="25" y="0" fill="#666" class="text-xs">ŷ</text>
          </g>
          <!-- 连接线 -->
          <g stroke="#9ca3af" stroke-width="1" opacity="0.3">
            <!-- 输入层到隐藏层1的连接 -->
            <line x1="65" y1="50" x2="135" y2="50"/>
            <line x1="65" y1="50" x2="135" y2="125"/>
            <line x1="65" y1="50" x2="135" y2="200"/>
            <line x1="65" y1="125" x2="135" y2="50"/>
            <line x1="65" y1="125" x2="135" y2="125"/>
            <line x1="65" y1="125" x2="135" y2="200"/>
            <line x1="65" y1="200" x2="135" y2="50"/>
            <line x1="65" y1="200" x2="135" y2="125"/>
            <line x1="65" y1="200" x2="135" y2="200"/>
            <line x1="65" y1="250" x2="135" y2="50"/>
            <line x1="65" y1="250" x2="135" y2="125"/>
            <line x1="65" y1="250" x2="135" y2="200"/>
            <!-- 隐藏层1到隐藏层2的连接 -->
            <line x1="165" y1="50" x2="235" y2="50"/>
            <line x1="165" y1="50" x2="235" y2="125"/>
            <line x1="165" y1="50" x2="235" y2="200"/>
            <line x1="165" y1="125" x2="235" y2="50"/>
            <line x1="165" y1="125" x2="235" y2="125"/>
            <line x1="165" y1="125" x2="235" y2="200"/>
            <line x1="165" y1="200" x2="235" y2="50"/>
            <line x1="165" y1="200" x2="235" y2="125"/>
            <line x1="165" y1="200" x2="235" y2="200"/>
            <!-- 隐藏层2到输出层的连接 -->
            <line x1="265" y1="50" x2="335" y2="100"/>
            <line x1="265" y1="125" x2="335" y2="100"/>
            <line x1="265" y1="200" x2="335" y2="100"/>
          </g>
        </svg>
      </div>
      <!-- 右侧：网络结构说明 -->
      <div class="bg-gradient-to-br from-gray-50 to-white p-4 rounded-lg shadow-sm">
        <div class="space-y-1.5">
          <!-- 输入层说明 -->
          <div class="flex items-start">
            <div class="w-2 h-2 rounded-full bg-red-400 mt-2 mr-2 flex-shrink-0"></div>
            <div>
              <span class="text-red-400 font-medium">输入层</span>
              <ul class="list-disc ml-4 mt-1 space-y-0.5 text-sm text-gray-600">
                <li>接收原始特征向量 x = [<span class="text-red-400">x₁, x₂, x₃, x₄</span>]</li>
                <li>特征需要进行标准化处理</li>
              </ul>
            </div>
          </div>
          <!-- 隐藏层说明 -->
          <div class="flex items-start">
            <div class="w-2 h-2 rounded-full bg-blue-400 mt-2 mr-2 flex-shrink-0"></div>
            <div>
              <span class="text-blue-400 font-medium">隐藏层</span>
              <ul class="list-disc ml-4 mt-1 space-y-0.5 text-sm text-gray-600">
                <li>进行特征<span class="text-blue-400">变换</span>与<span class="text-blue-400">组合</span></li>
                <li>每层使用不同的权重矩阵 <span class="text-blue-400">W</span></li>
                <li>添加偏置项 <span class="text-blue-400">b</span> 调整拟合</li>
              </ul>
            </div>
          </div>
          <!-- 输出层说明 -->
          <div class="flex items-start">
            <div class="w-2 h-2 rounded-full bg-green-400 mt-2 mr-2 flex-shrink-0"></div>
            <div>
              <span class="text-green-400 font-medium">输出层</span>
              <ul class="list-disc ml-4 mt-1 space-y-0.5 text-sm text-gray-600">
                <li>生成最终预测值 <span class="text-green-400">ŷ</span></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
