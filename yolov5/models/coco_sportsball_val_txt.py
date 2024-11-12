import os
import json

# JSON文件路径
instances_json_path = r'C:\ai\archive\coco2017\extracted_data\extracted_annotations\instances_val2017_sports_ball.json'  # 实际路径
images_dir = r"C:\ai\archive\coco2017\extracted_data\extracted_val2017_sports_ball"  # 实际图片存放路径
labels_dir = r"C:\Users\lijia\yolov5\extracted_data\labels\val"  # 存放TXT文件的路径

if not os.path.exists(labels_dir):
    os.makedirs(labels_dir)

# 读取instances_sports_ball.json文件
with open(instances_json_path, 'r') as file:
    instances_data = json.load(file)

# 创建一个从image_id到图片信息的映射
image_info_map = {img['id']: img for img in instances_data['images']}

# 检查映射是否正确
print("Image info map created with {} images.".format(len(image_info_map)))

# 遍历instances_data中的每条注释
for annotation in instances_data['annotations']:
    image_id = annotation['image_id']
    image_info = image_info_map.get(image_id)

    if image_info:
        file_name = image_info['file_name']
        txt_file_path = os.path.join(labels_dir, os.path.splitext(file_name)[0] + '.txt')

        # 检查文件路径是否正确
        print("Processing file: {}".format(txt_file_path))

        # 写入TXT文件
        with open(txt_file_path, 'w') as txt_file:
            category_id = annotation['category_id']
            bbox = annotation['bbox']
            x_center = (bbox[0] + bbox[2] / 2) / image_info['width']
            y_center = (bbox[1] + bbox[3] / 2) / image_info['height']
            width = bbox[2] / image_info['width']
            height = bbox[3] / image_info['height']
            txt_file.write(f"{category_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")
            print("Wrote annotation to {}".format(txt_file_path))
    else:
        print(f"No image info found for image ID {image_id}")

print("Conversion completed.")