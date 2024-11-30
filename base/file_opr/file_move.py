##移动指定目录下的所有文件到另一个目录下

import os
import shutil


def move_files(source_dir, destination_dir):
    # 确保目标目录存在，如果不存在则创建它
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # 遍历源目录及其子目录下的所有文件
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            source_file_path = os.path.join(root, file)
            destination_file_path = os.path.join(destination_dir, file)

            # 移动文件
            shutil.move(source_file_path, destination_file_path)


if __name__ == "__main__":
    source_directory = "/Users/zengqingwen/Desktop/大数据面试/基础语法-wilia老师"
    destination_directory = "/Users/zengqingwen/Desktop/大数据面试/基础语法"

    move_files(source_directory, destination_directory)