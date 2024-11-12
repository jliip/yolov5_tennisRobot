import os
import json

# 设置COCO数据集路径
coco_dir = r'C:\ai\archive\coco2017'
annotations_dir = os.path.join(coco_dir, 'annotations')
extracted_annotations_dir = os.path.join(coco_dir, 'extracted_annotations')

# 确保提取标注目录存在
if not os.path.exists(extracted_annotations_dir):
    os.makedirs(extracted_annotations_dir)

# 目标类别ID
target_category_id = 37  # "sports ball" 的类别ID

# 创建一个新的标注文件，包含目标类别的所有标注
extracted_annotations = {
    'images': [],
    'annotations': [],
    'categories': [{'id': target_category_id, 'name': 'sports ball'}]
}

# 遍历标注文件
# 遍历标注文件
for annotation_file in os.listdir(annotations_dir):
    if annotation_file.startswith('instances') and annotation_file.endswith('.json') and 'val' in annotation_file:
        with open(os.path.join(annotations_dir, annotation_file), 'r') as f:
            data = json.load(f)
            # 遍历所有图片信息
            for image_info in data['images']:
                extracted_annotations['images'].append(image_info)
            # 遍历所有标注信息
            for annotation in data['annotations']:
                if annotation['category_id'] == target_category_id:
                    extracted_annotations['annotations'].append(annotation)

# 保存提取的标注信息到新的JSON文件
with open(os.path.join(extracted_annotations_dir, 'instances_sports_ball_val.json'), 'w') as out_file:
    json.dump(extracted_annotations, out_file, indent=4)

print(f"Extracted annotations of 'sports ball' to {extracted_annotations_dir}")


