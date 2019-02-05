import json
import csv

# 需求 json 中的数据转换成 csv文件


# 1.分别 读 ,创建文件
json_fp = open('01new.json', 'r')
csv_fp = open('03csv.csv', 'w')
# 2.提出表头,表内容
data_list = json.load(json_fp)
sheet_title = ["姓名","年龄"]
#data_list[0].keys()
print(sheet_title)
sheet_data = []
for data in data_list:
    sheet_data.append(data.values())
# 3.csv写入器
writer = csv.writer(csv_fp)
# 4.写入表头
writer.writerow(sheet_title)
# 5.写入内容
writer.writerows(sheet_data)
# 6.关闭两个文件
json_fp.close()
csv_fp.close()