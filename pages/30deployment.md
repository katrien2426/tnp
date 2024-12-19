---
layout: default
---

<div class="bg-white bg-opacity-80 p-6 pb-4 rounded-lg mx-auto my-4 w-9/10">
  <div class="flex items-center justify-center mb-3">
    <h1 class="text-2xl font-bold text-gray-600">模型部署与应用</h1>
  </div>

  <div class="w-full bg-gradient-to-br from-gray-50 to-white rounded-lg p-4 pb-3">
    <div class="grid grid-cols-2 gap-6">
      <!-- 左侧：模型保存 -->
      <div class="bg-gradient-to-br from-gray-50 to-white p-3 rounded-lg shadow-sm">
        <div class="flex items-center mb-2">
          <div class="w-2 h-2 rounded-full bg-pink-400 mr-2"></div>
          <span class="text-pink-400 font-medium">模型存储</span>
        </div>
        <div class="bg-gradient-to-r from-gray-50 to-white rounded-lg p-3">
          <div class="text-center mb-3">
            <code class="bg-gray-100 px-3 py-1.5 rounded-md text-pink-600 font-mono text-sm">mlp_model.pth</code>
          </div>
          <ul class="list-disc ml-4 space-y-2 text-sm text-gray-600">
            <li>完整保存模型结构与参数</li>
            <li>包含优化器配置信息</li>
            <li>兼容主流深度学习框架</li>
            <li>支持跨平台部署使用</li>
          </ul>
        </div>
      </div>
      <!-- 右侧：应用场景 -->
      <div class="bg-gradient-to-br from-gray-50 to-white p-3 rounded-lg shadow-sm">
        <div class="flex items-center mb-2">
          <div class="w-2 h-2 rounded-full bg-blue-400 mr-2"></div>
          <span class="text-blue-400 font-medium">实际应用</span>
        </div>
        <div class="bg-gradient-to-r from-gray-50 to-white rounded-lg p-3">
          <ul class="list-disc ml-4 space-y-3 text-sm text-gray-600">
            <li>
              <div class="font-medium text-gray-700">Web API服务集成</div>
              <div class="text-gray-500 mt-0.5">支持RESTful接口调用，便于系统集成</div>
            </li>
            <li>
              <div class="font-medium text-gray-700">批量数据处理</div>
              <div class="text-gray-500 mt-0.5">高效处理大规模数据集，支持并行计算</div>
            </li>
            <li>
              <div class="font-medium text-gray-700">实时预测服务</div>
              <div class="text-gray-500 mt-0.5">毫秒级响应能力，满足实时性要求</div>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>