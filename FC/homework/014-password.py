for i in range(3):
    password = int(input('请输入密码：'))
    if password == 88888888:
        print('输入正确')
        break
    else:
        print(f'请重新输入，还有{i}次机会')