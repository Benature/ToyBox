# author: Benatuer
# date: 2018.10

'''
背景:
    给部员安排了PS作业, 需要每个部员随机给另一个部员
    点评一下对方作品, 然后再随机一位部长层做最终点评.
'''

from random import randint, choice
data = {
    '部员A': '青葱高三骄阳行',
    '部员K': '国金团委学术部',
    '部员L': '中珠幻境',
    '部员N': '中珠排协',
    '部员E': '街舞社招新',
    '部员f': '关爱老人',
    '部员Z': '民乐团招新',
    '部员C': 'UFO街舞大赛',
    '部员y': '篮协招新'
}

names = list(data.keys())
hws = list(data.values())

input("互评环节即将开始\n请大家系好安全带!")
print("-"*40)
while names:
    name = names.pop(randint(0, len(names)-1))
    print("【{}】同学请注意".format(name))
    hws_temp = hws.copy()
    try:
        hws_temp.remove(data[name])
    except:
        pass
    hw = choice(hws_temp)
    print("请你点评作品【{}】".format(hws.pop(hws.index(hw))))
    input("请其他同学补充点评")
    input("请部长(们)点评")
    input("next")
    print("-"*40)

print("请【{}】注意".format(choice(["部长", "副部长"])))
print("请你点评作品【{}】".format(hws[0]))

print("\n")
print("="*40)
print("\n互评环节到此结束")
input(".")
