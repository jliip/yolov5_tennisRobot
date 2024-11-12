import os
import json

# JSON文件路径
captions_json_path = r"C:\ai\archive\coco2017\annotations\captions_train2017.json"
instances_json_path = r'C:\ai\archive\coco2017\extracted_annotations\instances_sports_ball.json'  # 实际路径
images_dir = r"C:\ai\archive\coco2017\extracted_data\extracted_sports_ball"  # 实际图片存放路径
labels_dir = r"C:\Users\lijia\yolov5\extracted_data\labels"  # 存放TXT文件的路径

if not os.path.exists(labels_dir):
    os.makedirs(labels_dir)

# 读取instances_sports_ball.json文件
with open(instances_json_path, 'r') as file:
    instances_data = json.load(file)

# 创建一个从file_name到图片信息的映射
image_info_map = {img['file_name']: img for img in instances_data['images']}

# 读取captions_train2017.json文件
with open(captions_json_path, 'r') as file:
    captions_data = json.load(file)

# 遍历captions_data中的每条注释
for annotation in captions_data['annotations']:
    image_id = annotation['image_id']

    # 在instances_data中查找对应的图片信息
    # 由于我们没有instances_data中的image_id到file_name的直接映射，我们需要遍历instances_data['images']来找
import os

# 存放TXT文件的目录
labels_dir = r"C:\Users\lijia\yolov5\extracted_data\labels"

# 遍历labels_dir目录中的所有文件
for filename in os.listdir(labels_dir):
    # 构建完整的文件路径
    file_path = os.path.join(labels_dir, filename)

    # 检查文件是否是TXT文件
    if filename.endswith('.txt'):
        # 获取文件大小
        if os.path.getsize(file_path) == 0:
            # 删除0KB的TXT文件
            os.remove(file_path)
            print(f"Deleted 0KB file: {file_path}")