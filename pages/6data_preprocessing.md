---
layout: default
---

<div class="bg-white bg-opacity-80 p-6 rounded-lg mx-auto my-4 w-9/10 h-9/10">
  <div class="flex items-center justify-center mb-2">
    <h1 class="text-2xl font-bold text-gray-600">数据预处理</h1>
  </div>

  <div class="w-full bg-gradient-to-br from-gray-50 to-white rounded-lg shadow-sm p-3">
    <div class="flex items-center mb-3">
      <div class="w-5 h-5 rounded-full bg-purple-100 flex items-center justify-center mr-2">
        <span class="text-purple-500 font-medium text-sm">3</span>
      </div>
      <div class="text-lg font-medium text-gray-700">异常值检查</div>
    </div>
    <div class="mt-2 text-base text-gray-600">
      <p class="leading-relaxed">
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;曾考虑使用<span class="text-pink-500 font-medium">IQR 方法（四分位距）</span>自动化处理异常值。然而，发现<span class="text-blue-500 font-medium">离群点数量较多</span>，可能受<span class="text-purple-500 font-medium">地理因素</span>等外部条件的影响，于是采取更为简单的策略，通过判断<span class="text-green-500 font-medium">是否存在小于零的值</span>来识别特别离谱的数据。
      </p>
    </div>
    <div class="bg-gray-50 p-2 rounded-lg font-mono text-base text-gray-700 my-3">
```python
negative_values = (chicago_features_df.select_dtypes(include=['float64', 'int64']) < 0).sum()
```
    </div>
    <div class="mt-2 text-base text-gray-600">
      <p class="leading-relaxed">
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;经过检查，各列数据中均<span class="text-pink-500 font-medium">未发现</span>小于零的值，说明数据没有明显不合理的小于零值，整体质量较好，当前无需进行针对性的异常值处理。
      </p>
    </div>
  </div>
</div>