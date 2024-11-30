import re
phoneNumRegex = re.compile(r'(\d{3})-\d{3}-\d{4}')
mo = phoneNumRegex.search('my number is 2415-444-44544')
print(mo.group(1))
result = re.findall(r'\w','cabcd')
#['c', 'a', 'b', 'c', 'd']

result = re.findall(r'\w.*','cabcd')
#['cabcd']

result = re.findall(r'\w+','cabcd')
#['c', 'a', 'b', 'c', 'd']
print(result)


#匹配方式二
result = re.search(r'\w+','2ead')
print(result.group())


'''
compile()
第二个参数传入re.I或re.IGNORECASE 表示忽略大小写
第二个参数传入re.VERBOSE忽律空白符合和注释
'''