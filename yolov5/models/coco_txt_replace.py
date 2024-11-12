import os

# 定义原始标签文件和新标签文件的目录
labels_dir = r"C:\Users\lijia\yolov5\extracted_data\labels\extracted_val2017_sports_ball"
new_labels_dir = r"C:\Users\lijia\yolov5\extracted_data\labels_new\extracted_val2017_sports_ball"

# 如果新标签文件目录不存在，则创建它
if not os.path.exists(new_labels_dir):
    os.makedirs(new_labels_dir)

# 遍历labels_dir目录中的所有文件
for filename in os.listdir(labels_dir):
    if filename.endswith('.txt'):
        # 构建完整的文件路径
        file_path = os.path.join(labels_dir, filename)
        new_file_path = os.path.join(new_labels_dir, filename)

        # 读取TXT文件内容，并替换类别ID为37的标签
        with open(file_path, 'r') as file:
            lines = file.readlines()

        with open(new_file_path, 'w') as new_file:
            for line in lines:
                # 替换每行开头的数字37为0
                new_line = line.replace('37', '0', 1)
                new_file.write(new_line)

print("Labels conversion completed.")