# 1注投10元，每投10元就加一注，猜中数字个数和奖金如award所示。
import random
#================================================================
# 设置
# 抽中次数和奖金
award = {0: 0, 1: 15, 2: 30, 3: 60, 4: 200, 5: 500, 6: 1000}

# 大奖数字
number = []
# 你的投注
answer = []

# 抽奖次数，不能超过6次
n = 3

# 抽奖数字范围，从1开始
scope = 20


# =================================================================
def printRule():
    print("=====游戏规则=====")
    print(f"投注额10，在1到{scope}范围内，说{n}个数字，作为奖注。")

    for i in range(n, 0, -1):
        print(f"{n-i+1}等奖，猜中{i}个数字，奖金为{award[i]}")

    print("-" * 10)


def genNumbers():
    for i in range(n):
        r = random.randint(1, scope)
        number.append(r)


def guess():
    for i in range(n):
        a = input(f"请说第{i+1}个数:")
        answer.append(int(a))


def drawAward():
    genNumbers()

    count = 0
    awardnum = []
    for i in answer:
        if i in number:
            count += 1
            awardnum.append(i)

    print(f"大奖数字为{number}")
    print(f"你的投注为：{answer}")
    if count == 0:
        print("对不起，你没有中奖。")
    else:
        print(f"你中了{n-count+1}等奖，中奖数字为{awardnum},奖金为{award[count]}")


play = True

printRule()
while play:
    guess()
    drawAward()

    p = input("还玩吗(Y/N)？[Y] ")
    if p == "N" or p == "n":
        play = False
        print("下次再来玩，祝好运！！！")
