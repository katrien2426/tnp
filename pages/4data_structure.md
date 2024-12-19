---
layout: default
---

<div class="bg-white bg-opacity-80 p-6 rounded-lg mx-auto my-4 w-9/10 h-9/10">
  <h1 class="text-lg font-bold text-gray-600 mb-6 text-center">数据结构分析</h1>

  <div class="grid grid-cols-5 gap-8">
    <div class="col-span-2 flex flex-col items-center">
      <div class="relative w-7/10 group">
        <img src="/img/chicago.png?url" alt="芝加哥普查区编号" class="w-full object-contain rounded-lg shadow-md transition-all duration-300 ease-in-out transform group-hover:scale-200 group-hover:shadow-xl"/>
        <div class="text-sm text-gray-500 mt-3 text-center">图1 芝加哥普查区编号分布图</div>
      </div>
    </div>
    <div class="col-span-3 flex flex-col items-start">
      <div class="w-full bg-gradient-to-br from-gray-50 to-white rounded-lg shadow-sm p-4">
        <div class="font-mono text-sm text-gray-700">
```python
file_path = './chicago_tnp.geojson'
with open(file_path, 'r') as f:
    geojson_data = json.load(f)
properties_data = [feature['properties'] 
    for feature in geojson_data['features']]
chicago_features_df = pd.DataFrame(properties_data)
chicago_features_df.head()
```
        </div>
      </div>
    </div>
  </div>

  <div class="mt-6 p-4 bg-gradient-to-br from-gray-50 to-white rounded-lg shadow-sm">
    <p class="text-base text-gray-600 leading-relaxed">
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;以<span class="text-pink-500 font-medium">普查区编号</span>为主键，<span class="text-blue-500 font-medium">TripCount</span>为目标值的一系列地理特征值，包含了平均通勤时间、种族比例、教育水平、行程时间、行程距离和费用在内的总计<span class="text-purple-500 font-medium">37</span>个特征值。
    </p>
  </div>
</div>
