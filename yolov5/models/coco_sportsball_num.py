r'C:\ai\archive\coco2017\extracted_annotations\instances_sports_ball.json'

import json

# 加载JSON数据
with open(r'C:\ai\archive\coco2017\extracted_data\extracted_annotations\instances_val2017_sports_ball.json', 'r') as file:
    data = json.load(file)

# 创建一个集合来存储唯一的image_id
unique_image_ids = set()

# 遍历所有标注信息，添加image_id到集合中
for annotation in data['annotations']:
    unique_image_ids.add(annotation['image_id'])

# 统计唯一的image_id数量
num_unique_images = len(unique_image_ids)

print(f"Number of unique images containing 'sports ball': {num_unique_images}")