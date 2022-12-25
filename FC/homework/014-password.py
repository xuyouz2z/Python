password = 8888
# 输入次数
count = 3
while count:
    user = input('请输入密码：')
    if user == password:
        print('输入正确')
        break
    elif '*' in user:
        print(f'密码中不能含有“*”号，请重新输入，您还有{count}机会')
        # continue跳过循环（后边的语句不执行）
        continue
    elif count == 1:
        print('输入错误，请稍后再试')
    else:
        print(f'请重新输入，还有{count-1}次机会')
    count -= 1