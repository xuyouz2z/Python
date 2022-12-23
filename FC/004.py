print("les's go")
# 进行转义
print('les\'s go')
print('''les's
go!go!''')

print('-'*20)

print('C:\now')
# 进行转义
print('C:\\now')

# 原始字符串（需在引号之前添加r）
str = r'C:\now\FC'
print(str)
# 注意：原始字符串末尾不能加反斜杠\
str1 = r'C:\now\FC''\\'
print(str1)
print(r'C:\now\FC\test''\\')

print('-'*20)

print('''你好
世界
哈哈哈''')