---
layout: default
math: true
---

<div class="bg-white bg-opacity-80 p-6 rounded-lg mx-auto my-4 w-9/10 h-9/10">
  <div class="flex items-center justify-center mb-2">
    <h1 class="text-2xl font-bold text-gray-600">特征选择</h1>
  </div>

  <div class="w-full bg-gradient-to-br from-gray-50 to-white rounded-lg shadow-sm p-4 mt-2">
    <div class="flex items-center">
      <div class="w-6 h-6 rounded-full bg-blue-100 flex items-center justify-center mr-3">
        <span class="text-blue-500 font-medium text-base">2</span>
      </div>
      <div class="text-lg font-medium text-gray-700">方差分析</div>
    </div>
    <div class="text-base text-gray-600 p-4 pb-2">
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;通过计算各特征的方差来识别<span class="text-pink-500">低变异特征</span>，评估其对模型预测的潜在贡献。特征的方差越大，表明其<span class="text-blue-500">区分样本的能力越强</span>。
    </div>
    <div class="grid grid-cols-2 gap-4 px-4">
      <div class="p-2">
        <div class="font-bold mb-2">方差计算公式</div>
        <div class="text-center bg-white p-3 rounded-lg">
        
$$\text{Var}(X) = \frac{1}{n} \sum_{i=1}^n (x_i - \mu)^2$$
</div>
      </div>
      <div class="p-2">
        <div class="font-bold mb-2">代码实现</div>
        <div class="bg-gray-50 p-3 rounded-lg font-mono text-sm text-gray-700">
```python
X = chicago_features_df.drop(columns=[target_column])
y = chicago_features_df[target_column]
variance_threshold = 0.1 
low_variance_features = X.columns[X.var() < variance_threshold].tolist()
```
        </div>
      </div>
    </div>
  </div>
</div>
