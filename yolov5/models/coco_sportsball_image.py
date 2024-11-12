import os
import json
import shutil

# 设置COCO数据集路径
coco_dir = r'C:\ai\archive\coco2017'
annotations_dir = os.path.join(coco_dir, 'annotations')
images_dir = os.path.join(coco_dir, 'train2017')
extracted_dir = os.path.join(coco_dir, 'extracted_sports_ball')

# 确保提取目录存在
if not os.path.exists(extracted_dir):
    os.makedirs(extracted_dir)

# 目标类别ID
target_category_id = 37

# 遍历标注文件
for annotation_file in os.listdir(annotations_dir):
    if annotation_file.startswith('instances') and annotation_file.endswith('.json'):
        with open(os.path.join(annotations_dir, annotation_file), 'r') as f:
            data = json.load(f)
            for annotation in data['annotations']:
                if annotation['category_id'] == target_category_id:
                    image_id = annotation['image_id']
                    # 查找对应的图片信息
                    image_info = next((item for item in data['images'] if item['id'] == image_id), None)
                    if image_info:
                        img_file_name = image_info['file_name']
                        # 复制图片
                        src_img_path = os.path.join(images_dir, img_file_name)
                        dst_img_path = os.path.join(extracted_dir, img_file_name)
                        shutil.copy(src_img_path, dst_img_path)
                        # 复制标注
                        src_annotation_path = os.path.join(annotations_dir, annotation_file)
                        dst_annotation_path = os.path.join(extracted_dir, annotation_file)
                        shutil.copy(src_annotation_path, dst_annotation_path)

print(f"Extracted images and annotations of 'sports ball' to {extracted_dir}")