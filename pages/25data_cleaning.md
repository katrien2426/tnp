---
layout: default
---

<div class="bg-white bg-opacity-80 p-6 pb-4 rounded-lg mx-auto my-4 w-9/10">
  <div class="flex items-center justify-center mb-2">
    <h1 class="text-2xl font-bold text-gray-600">模型构建：全连接神经网络</h1>
  </div>

  <div class="w-full bg-gradient-to-br from-gray-50 to-white rounded-lg p-3 pb-2">
    <div class="text-gray-700  px-2">
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-pink-400 font-medium">前向传播</span>是神经网络从输入层到输出层的计算过程，而<span class="text-blue-400 font-medium">反向传播</span>则是通过计算梯度来不断调整网络参数以减小误差的过程。
    </div>
    <div class="grid grid-cols-2 gap-4">
      <!-- 左侧：网络结构图 -->
      <div class="bg-gradient-to-br from-gray-50 to-white p-2 rounded-lg shadow-sm">
        <svg width="100%" height="250" viewBox="0 0 400 250" class="mx-auto">
          <!-- 输入层 -->
          <g transform="translate(50,50)">
            <circle cx="0" cy="0" r="15" fill="#f87171" opacity="0.8"/>
            <circle cx="0" cy="75" r="15" fill="#f87171" opacity="0.8"/>
            <circle cx="0" cy="150" r="15" fill="#f87171" opacity="0.8"/>
            <circle cx="0" cy="200" r="15" fill="#f87171" opacity="0.8"/>
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
          <!-- 数学公式 -->
          <g transform="translate(0,270)">
            <text x="200" y="0" text-anchor="middle" fill="#374151" class="text-xs">h = σ(Wx + b)</text>
            <text x="200" y="20" text-anchor="middle" fill="#374151" class="text-xs">ŷ = σ(W₂h + b₂)</text>
          </g>
        </svg>
      </div>
      <!-- 右侧：数学原理说明 -->
      <div class="bg-gradient-to-br from-gray-50 to-white p-2 rounded-lg shadow-sm space-y-0.5">
        <!-- 前向传播 -->
        <div class="bg-gradient-to-r from-gray-50 to-white rounded-lg p-2">
          <div class="flex items-center mb-1">
            <div class="w-2 h-2 rounded-full bg-pink-400 mr-2"></div>
            <span class="text-pink-400 font-medium">前向传播</span>
          </div>
          <ul class="list-disc ml-4 space-y-0.5 text-sm text-gray-600">
            <li>隐藏层计算：h = σ(Wx + b)</li>
            <li>输出层计算：ŷ = σ(W₂h + b₂)</li>
            <li>激活函数：ReLU(x) = max(0, x)</li>
          </ul>
        </div>
        <!-- 反向传播 -->
        <div class="bg-gradient-to-r from-gray-50 to-white rounded-lg p-2">
          <div class="flex items-center mb-1">
            <div class="w-2 h-2 rounded-full bg-blue-400 mr-2"></div>
            <span class="text-blue-400 font-medium">反向传播</span>
          </div>
          <ul class="list-disc ml-4 space-y-0.5 text-sm text-gray-600">
            <li>损失函数：MSE = (y - ŷ)²</li>
            <li>权重更新：w = w - α∇L</li>
            <li>偏置更新：b = b - α∇L</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>
