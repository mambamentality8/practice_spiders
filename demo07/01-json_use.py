import json

json_data = '[{"name":"张三","age":"20"},{"name":"李四","age":"18"}]'
# 将json转换成列表
list_data1 = json.loads(json_data)
print(list_data1)
print(type(list_data1))

list_data2 = [{"name": "张三", "age": "20"}, {"name": "李四", "age": "18"}]
# 将列表转换成字符串
json_data2 = json.dumps(list_data2)

print(type(json_data2))
print(json_data2)

# 将列表写入文件
list_data3 = [{"name": "张三", "age": "20"}, {"name": "李四", "age": "18"}]
json.dump(list_data3, open('01new.json', 'w'))

# 读取json文件将json转换成列表
result = json.load(open('01new.json', 'r'))
print(result)
