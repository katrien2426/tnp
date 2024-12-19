---
layout: default
---

<div class="bg-white bg-opacity-80 p-2 rounded-lg mx-auto mt-4 mb-2 w-9/10 h-9/10">
  <h1 class="text-lg font-bold text-gray-600 mb-6 text-center">数据预处理</h1>

  <div class="flex flex-col gap-4">
    <div class="w-full bg-gradient-to-br from-gray-50 to-white rounded-lg shadow-sm p-3">
      <div class="flex items-center mb-2">
        <div class="w-5 h-5 rounded-full bg-pink-100 flex items-center justify-center mr-2">
          <span class="text-pink-500 font-medium text-sm">1</span>
        </div>
        <div class="text-sm font-medium text-gray-700">缺失值检查</div>
      </div>
      <div class="bg-gray-50 p-1 rounded-lg font-mono text-sm text-gray-700">
```python
missing_values = chicago_features_df.isnull().sum()
```
      </div>
      <div class="mt-1 text-sm text-gray-600">
        <p class="leading-relaxed">
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;数据中<span class="text-pink-500 font-medium">不存在缺失值</span>，完整性良好，无需针对缺失值进行<span class="text-blue-500 font-medium">填充或删除</span>等预处理步骤。
        </p>
      </div>
    </div>
    <div class="w-full bg-gradient-to-br from-gray-50 to-white rounded-lg shadow-sm p-3">
      <div class="flex items-center mb-2">
        <div class="w-5 h-5 rounded-full bg-blue-100 flex items-center justify-center mr-2">
          <span class="text-blue-500 font-medium text-sm">2</span>
        </div>
        <div class="text-sm font-medium text-gray-700">数据类型检查</div>
      </div>
      <div class="bg-gray-50 p-1 rounded-lg font-mono text-sm text-gray-700">
```python
print(chicago_features_df.dtypes)
```
      </div>
      <div class="mt-1 text-sm text-gray-600">
        <p class="leading-relaxed">
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;均为<span class="text-pink-500 font-medium">float64和int64</span>，说明数据主要由数值组成，没有非数值（如字符串、日期等）类型，可以直接用于数值计算和统计分析，例如均值、标准差、回归模型等，不需要额外的<span class="text-blue-500 font-medium">类型转换</span>。
        </p>
      </div>
    </div>
  </div>
</div>