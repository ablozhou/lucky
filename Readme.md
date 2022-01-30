# draw award for family and kids
A game for family to draw award and play with kids.

过年家庭玩的抽奖程序

给孩子玩的, 可以通过抽奖赢取钱或游戏时间。

# env
python 3+

# config
modify source code lucky.py:
```python
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
```
# run
```sh
zhh@/Users/zhh/git/lucky git:(master) ✗ $ python lucky.py
=====游戏规则=====
投注额10，在1到20范围内，说3个数字，作为奖注。
1等奖，猜中3个数字，奖金为60
2等奖，猜中2个数字，奖金为30
3等奖，猜中1个数字，奖金为15
----------
请说第1个数:2
请说第2个数:5
请说第3个数:8
大奖数字为[8, 1, 2]
你的投注为：[2, 5, 8]
你中了2等奖，中奖数字为[2, 8],奖金为30
还玩吗(Y/N)？[Y] n
下次再来玩，祝好运！！！
```