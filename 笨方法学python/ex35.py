from sys import exit          # exit 函数可以使你的脚本在任何地方停止执行

def gold_room():
    print("This room is full of gold. How much do yuo take?")  # 这个房间里满是金子。你要拿走多少？

    next = input("请输入一个你想拿走的金额(数字)> ")
    if "0" in next or "1" in next:
        how_much = int(next)     
    else:
        dead("Man, learn to type a number.")  # 人类，学着打数字吧。

    if how_much < 50:
        print("Nice, you're not greedy, you win!")   # 很好，你不贪心，你赢了！
        exit(0)                 # 0 代表正常退出，1 代表错误退出
    else:
        dead("You greedy bastard!")    # 你这个贪心的混蛋！


def bear_room():
    print('There is a bear here.')                         # 这里有一只熊。
    print('The bear has a bunch of honey.')                # 熊有一堆蜂蜜。
    print('The fat bear is in front of another door.')     # 胖熊在另一扇门前面。
    print('How are you going to move the bear?')           # 你打算怎么移动熊？
    bear_moved = False  # 设定熊的基础状态是不移动

    while True:
        next = input('>take honey,taunt bear,open door选择一个> ')

        if next == 'take honey':
            dead('The bear looks at you then slaps your face off.')    # 熊看着你，然后把你的脸拍掉。
        elif next == 'taunt bear' and not bear_moved:
            dead('The bear has moved from the door. You can go through it now.')    # 熊已经从门口走开了。你现在可以通过它。
        elif next == 'taunt bear' and bear_moved:
            dead('The bear gets pissed off and chews your leg off.')    # 熊生气了，咬掉了你的腿。
        elif next == 'open door':
            gold_room()      # 掉用函数，进入金币房间
        else:
            print('I got no idea what that means.')      # 我不知道你在说什么。


def cthulhu_room():
    print('Here you see the great evil Cthulhu.')                 # 在这里你可以看到邪恶的克苏鲁。
    print('He, it, whatever stares at you and you go insane.')    # 他，它，无论什么盯着你，你都会发疯。
    print('Do you flee for your life or eat your head?')          # 你是逃命还是吃你的脑子？

    next = input('>flee或者head> ')

    if 'flee' in next:
        start()           # 重新开始
    elif 'head' in next:
        dead('Well that was tasty!')         # 好吧，那很好吃！
    else: 
        cthulhu_room()    # 用户的输入既不包含 'flee' 也不包含 'head'，那么程序会再次调用 cthulhu_room 函数，重新进入克苏鲁房间
 
def dead(why):
    print(why, 'Good job!')          # 为什么，干得好！'
    exit(0)                      # 退出

def start():
    print('You are in a dark room.')           # 你在一个黑暗的房间里。
    print('There is a door to your right and left.')        # 你的左右两边各有一扇门。
    print('Which one do you take?')        # 你选择哪一个？

    next = input('>right or left> ')

    if next == 'left':
        bear_room()        # 进入熊房间
    elif next == 'right':
        cthulhu_room()     # 进入克鲁苏房间
    else:
        dead("You stumble around the room until you starve.")       # 你在房间里跌跌撞撞，直到饿死。

start()     # 调用函数，开始游戏