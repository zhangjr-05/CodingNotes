import os

# 获取当前文件的目录
current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)
# 获取上一级目录
parent_dir = os.path.dirname(current_dir)

# 列出上一级目录中的所有文件
files_in_parent_dir = os.listdir(parent_dir)

# # 打印文件路径
# for file_name in files_in_parent_dir:
#     file_path = os.path.join(parent_dir, file_name)
#     print(file_path)

