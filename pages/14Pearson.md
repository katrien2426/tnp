---
layout: default
---

<div class="bg-white bg-opacity-80 p-6 rounded-lg mx-auto my-4 w-9/10 h-9/10">
  <div class="flex items-center justify-center mb-2">
    <h1 class="text-2xl font-bold text-gray-600">特征选择</h1>
  </div>

  <div class="w-full bg-gradient-to-br from-gray-50 to-white rounded-lg p-4">
    <div class="flex items-center mb-3">
      <div class="w-6 h-6 rounded-full bg-blue-100 flex items-center justify-center mr-2">
        <span class="text-blue-500 font-medium">5</span>
      </div>
      <div class="text-lg font-medium text-gray-700">皮尔逊相关性分析</div>
    </div>
    <div class="text-base text-gray-600 mb-4 leading-relaxed" style="text-indent: 2em;">
      <span class="text-pink-400 font-medium">皮尔逊相关系数</span>是一种统计学方法，用于衡量两个变量之间的线性关系强度。
      其值范围在 -1 到 1 之间。绝对值越接近 1，表示两个变量的线性相关性越强；绝对值接近 0，则相关性较弱。
    </div>
    <div class="grid grid-cols-5 gap-4">
      <div class="col-span-3 bg-gradient-to-br from-gray-50 to-white p-4 rounded-lg shadow-sm hover:shadow-md transition-all">
        <div class="font-bold text-gray-700 mb-4">皮尔逊相关系数</div>
        <div class="text-center">
$$
r_{xy} = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^n (x_i - \bar{x})^2} \sqrt{\sum_{i=1}^n (y_i - \bar{y})^2}}
$$
</div>
      </div>
      <div class="col-span-2 bg-gradient-to-br from-gray-50 to-white p-4 rounded-lg shadow-sm hover:shadow-md transition-all">
        <div class="font-bold text-gray-700 mb-4">代码实现</div>
```python
# 设置相关性阈值
correlation_threshold = 0.3
# 计算与 TripCount 的相关性
correlations = chicago_features_df.corr(method='pearson')['TripCount'].abs()
```
      </div>
    </div>
  </div>
</div>