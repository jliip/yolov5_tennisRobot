import os
import shutil

# 设置COCO128数据集路径
coco128_dir = r'C:\Users\lijia\yolov5\coco128'
labels_dir = os.path.join(coco128_dir, 'labels','train2017')
images_dir = os.path.join(coco128_dir, 'images','train2017')
extracted_dir = os.path.join(coco128_dir, 'extracted_32')  # 创建一个新的目录来存储提取的图片


# 确保提取目录存在
if not os.path.exists(extracted_dir):
    os.makedirs(extracted_dir)

# 目标类别ID
target_category_id = 32

# 递归遍历所有标签文件
for root, dirs, files in os.walk(labels_dir):
    for file in files:
        if file.endswith('.txt'):
            with open(os.path.join(root, file), 'r') as f:
                lines = f.readlines()
                # 检查每一行是否包含目标类别ID
                if any(line.split()[0] == str(target_category_id) for line in lines):
                    # 如果找到目标类别ID，提取图片文件名和标注文件名
                    img_file_name = file.replace('.txt', '.jpg')  # 假设图片文件名与标签文件名对应，除了扩展名
                    annotation_file_name = file  # 标注文件名与原文件名相同

                    # 复制图片到提取目录
                    src_img_path = os.path.join(images_dir, img_file_name)
                    dst_img_path = os.path.join(extracted_dir, img_file_name)
                    shutil.copy(src_img_path, dst_img_path)

                    # 复制标注文件到提取目录
                    src_annotation_path = os.path.join(root, annotation_file_name)
                    dst_annotation_path = os.path.join(extracted_dir, annotation_file_name)
                    shutil.copy(src_annotation_path, dst_annotation_path)

print(f"Extracted images and annotations of category ID {target_category_id} to {extracted_dir}")