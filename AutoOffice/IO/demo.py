import os,re
path=os.path.join('user','bin','spam')  #生成适配于操作系统的路径
print(path)

print(os.getcwd())  #当前路径
print()
aboult_path='/Users/zengqingwen/PycharmProjects/python/AutoOffice/IO/demo.py'
# with open(r'/Users/zengqingwen/PycharmProjects/python/AutoOffice/IO/knowledge',"r") as file:
#     lines = file.readlines()
#
# filelines=[]
#
# for line in lines:
#     if not re.search(r'^复制',line):
#         filelines.append(line)
# with open(r'/Users/zengqingwen/PycharmProjects/python/AutoOffice/IO/knowledges',"w") as file:
#     file.writelines(filelines)

#计算相对路径
print(os.path.relpath('/Users/zengqingwen/PycharmProjects/python/AutoOffice/IO/demo.py','/Users/zengqingwen'))

#计算文件大小
print(os.path.getsize('/Users/zengqingwen/PycharmProjects/python/AutoOffice/IO/demo.py'))
#文件夹下内容
print(os.listdir('../'))

#判断路径是否存在
print(os.path.exists(aboult_path))

#是否目录
print(os.path.isdir(aboult_path))

#是否文件
print(os.path.isfile(aboult_path))




