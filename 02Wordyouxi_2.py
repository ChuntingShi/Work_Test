print('--------------小史------------')
temp = input('不妨猜一下我心理想的数字：')
guess = int(temp)
while guess != 8:
    temp = input('哎呀，猜错了，重新输入一个数字：')
    guess = int(temp)
    if guess == 8:
        print('good,恭喜你才对了^_^')
        print('但是没有奖品哦！！！')
    else:
        if guess > 8:
            print('猜大了！！')
        else:
            print('猜小了！！')
print('游戏结束，不玩啦！！！')
