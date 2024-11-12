import json

# 路径到COCO的标注文件
annotation_file = r'C:\ai\archive\coco2017\annotations\instances_train2017.json'

# 加载标注数据
with open(annotation_file, 'r') as f:
    coco_data = json.load(f)

# 打印所有类别的ID和名称
for category in coco_data['categories']:
    print(f"ID: {category['id']}, Name: {category['name']}")