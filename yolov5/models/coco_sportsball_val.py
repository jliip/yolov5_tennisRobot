import os
import json
import shutil

# COCO数据集路径
coco_dir = r'C:\ai\archive\coco2017'
val_images_dir = os.path.join(coco_dir, 'val2017')
val_annotations_path = os.path.join(coco_dir, 'annotations', 'instances_val2017.json')

# 提取后的目录
extracted_dir = os.path.join(coco_dir, 'extracted_val2017_sports_ball')
if not os.path.exists(extracted_dir):
    os.makedirs(extracted_dir)

# 加载标注文件
with open(val_annotations_path, 'r') as f:
    annotations = json.load(f)

# 创建一个新的标注集，仅包含“sports ball”类别的标注
extracted_annotations = {
    'images': [],
    'annotations': [],
    'categories': [{'id': 37, 'name': 'sports ball'}]
}

# 遍历所有标注信息
for annotation in annotations['annotations']:
    if annotation['category_id'] == 37:
        image_id = annotation['image_id']
        # 查找对应的图片信息
        image_info = next((item for item in annotations['images'] if item['id'] == image_id), None)
        if image_info:
            extracted_annotations['images'].append(image_info)
            extracted_annotations['annotations'].append(annotation)

            # 复制图片
            img_file_name = image_info['file_name']
            src_img_path = os.path.join(val_images_dir, img_file_name)
            dst_img_path = os.path.join(extracted_dir, img_file_name)
            shutil.copy(src_img_path, dst_img_path)

# 保存提取的标注信息到新的JSON文件
extracted_annotations_path = os.path.join(extracted_dir, 'instances_val2017_sports_ball.json')
with open(extracted_annotations_path, 'w') as out_file:
    json.dump(extracted_annotations, out_file, indent=4)

print(f"Extracted annotations and images of 'sports ball' saved to {extracted_dir}")