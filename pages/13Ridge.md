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
        <span class="text-blue-500 font-medium">4</span>
      </div>
      <div class="text-lg font-medium text-gray-700">嵌入式方法（Ridge正则化）</div>
    </div>
    <div class="text-base text-gray-600 mb-4 leading-relaxed" style="text-indent: 2em;">
      我们还尝试了常见的嵌入式方法，包括 
      <span class="text-pink-400 font-medium">Lasso和Ridge正则化</span>。
      使用 <span class="text-blue-400 font-medium">Lasso</span> 时发现，
      由于其正则化强度较高，导致很多特征的系数被缩至零，筛选结果过于激进。
      因此，我们最终选择使用 <span class="text-purple-400 font-medium">Ridge回归</span>，
      它通过平滑特征的重要性，在减少过拟合的同时保留更多的有价值特征。
    </div>
    <div class="grid grid-cols-5 gap-4">
      <div class="col-span-3 bg-gradient-to-br from-gray-50 to-white p-4 rounded-lg shadow-sm hover:shadow-md transition-all">
        <div class="font-bold text-gray-700 mb-4">Ridge回归优化目标</div>
        <div class="text-center">
$$
\min_{\beta} \sum_{i=1}^n (y_i - \beta_0 - \sum_{j=1}^p \beta_j x_{ij})^2 + \lambda \sum_{j=1}^p \beta_j^2
$$
</div>
      </div>
      <div class="col-span-2 bg-gradient-to-br from-gray-50 to-white p-4 rounded-lg shadow-sm hover:shadow-md transition-all">
        <div class="font-bold text-gray-700 mb-4">代码实现</div>
```python
ridge = RidgeCV(alphas=[0.1, 1.0, 10.0], cv=5)
ridge.fit(X_scaled, y)
```
      </div>
    </div>
  </div>
</div>