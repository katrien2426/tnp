---
layout: default
---

<div class="bg-white bg-opacity-80 p-6 rounded-lg mx-auto my-4 w-9/10 h-9/10">
  <div class="flex items-center justify-center mb-4">
    <h1 class="text-2xl font-bold text-gray-600">特征选择</h1>
  </div>

  <div class="w-full bg-gradient-to-br from-gray-50 to-white rounded-lg shadow-sm p-3">
    <div class="flex items-center mb-4">
      <div class="w-6 h-6 rounded-full bg-blue-100 flex items-center justify-center mr-3">
        <span class="text-blue-500 font-medium text-base">1</span>
      </div>
      <div class="text-lg font-medium text-gray-700">特殊特征的提前处理</div>
    </div>
    <div class="grid grid-cols-3 gap-4 mb-4">
      <div class="bg-pink-50 p-4 rounded-lg transform hover:scale-102 transition-transform duration-200 shadow-sm">
        <div class="font-bold text-pink-600 mb-3">非特征</div>
        <div class="text-sm text-gray-600 leading-relaxed">
          • GEO_ID（主键）<br>
          • 与目标变量一一对应<br>
          • 不携带有效信息
        </div>
      </div>
      <div class="bg-blue-50 p-4 rounded-lg transform hover:scale-102 transition-transform duration-200 shadow-sm">
        <div class="font-bold text-blue-600 mb-3">不适当特征</div>
        <div class="text-sm text-gray-600 leading-relaxed">
          • TRUE/FALSE<br>
          • 与目标变量直接相关的二分类<br>
          • 贡献度异常之高
        </div>
      </div>
      <div class="bg-green-50 p-4 rounded-lg transform hover:scale-102 transition-transform duration-200 shadow-sm">
        <div class="font-bold text-green-600 mb-3">保留特征</div>
        <div class="text-sm text-gray-600 leading-relaxed">
          • pct_share<br>
          • 反映需求构成<br>
          • 可能需要标准化处理
        </div>
      </div>
    </div>
    <div class="bg-gray-50 p-2 rounded-lg font-mono text-sm text-gray-700">
```python
# 删除不需要的特征
features_to_drop = ['GEO_ID', 'TRUE', 'FALSE']
chicago_features_df = chicago_features_df.drop(columns=features_to_drop)
```
    </div>
  </div>
</div>
