# 看起来复杂其实也只是定义了几个函数，然后在一个循环里面不断调用这些函数而已。

from sys import exit
from random import randint

def death():
    quips = ['You died. You kinda suck at this.你死了。你有点烂。',
             'Nice job, you died ...jackass.干得好，你死了...混蛋。',
             'Such a luser.这样一个失败者。',
             'I have a small puppy that\'s better at this.我有一只小狗狗，它比你强。',]
    print(quips[randint(0, len(quips)-1)])
    exit(1)

def central_corridor():
    print('The Gothons of Planet Percal #25 have invaded your ship and destroyed percal25星球的哥顿人入侵了你的飞船，摧毁了')
    print('your entire crew. You are the last surviving member and your last 你的整个船员。你是最后一个幸存的成员，你的最后')
    print('mission is to get the neutron destruct bomb from the Weapons Armory,任务是从武器库中获得中子毁灭炸弹')
    print('put it in the bridge, and blow the ship up after getting into an escape把它放在桥上，在逃生舱进入后把船炸了')
    print('escape pod.你的逃生舱。')
    print('\n')
    print('You\'re running down the central corridor to the Weapons Armory when你正沿着中央走廊跑向武器库')
    print('a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume一个哥顿人跳了出来，红色的鳞皮，黑暗的牙齿，邪恶的小丑')
    print('costume flowing around his hate filled body. He\'s blocking the door to the他的仇恨充满了他的身体。他挡住了门')
    print('Armory and about to pull a weapon to blast you.武器库，准备拉出武器来爆炸你。')

    action = input('(shoot!) (dodge!) (tell a joke)> ')

    if action == 'shoot!':
        print('Quick on the draw you yank out your blaster and fire it at the Gothon.你很快就把你的爆破器拔出来，朝哥顿人开火。')
        print('His clown costume is flowing and moving around his body, which throws他的小丑服装在他的身上流动和移动，这使他')
        print('off your aim. Your laser hits his costume but misses him entirely.偏离了你的目标。你的激光击中了他的服装，但完全没有击中他。')
        print('This completely ruins his brand new costume his mother bought him,这完全毁了他妈妈给他买的全新的服装，')
        print('which makes him fly into an insane rage and blast you repeatedly in the face.这使他陷入疯狂的愤怒，并不断地在你的脸上爆炸。')
        print('You are dead.你死了。')
        return 'death'
    
    elif action == 'dodge!':
        print('Like a world class boxer you dodge, weave, slip and slide right你像一个世界级的拳击手一样躲避，编织，滑动和滑动')
        print('as the Gothon\'s blaster cranks a laser past your head. In the middle of当哥顿人的爆破器在你的头上发射激光时。在中间')
        print('your artful dodge your foot slips and you bang your head on the metal你的巧妙躲避你的脚滑倒了，你的头撞在金属上')
        print('wall and pass out. You wake up shortly after only to die as the你醒来后不久就死了')
        print('Gothon stomps on your head and eats you.哥顿人踩着你的头吃了你。')
        return 'death'
    
    elif action == 'tell a joke':
        print('Lucky for you they made you learn Gothon insults in the academy.幸运的是，他们让你在学院里学习哥顿侮辱。')
        print('You tell the one Gothon joke you know:你告诉你知道的一个哥顿笑话:')
        print('Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.你的妻子很伤心，当她在房子里走来走去时，她在房子里走来走去。')
        print('The Gothon stops, tries not to laugh, then busts out laughing and can\'t哥顿人停下来，试着不笑，然后大笑起来，笑不出来')
        print('move. While he\'s laughing you run up and shoot him square in the head你跑过去，朝他的头部开枪')
        print('putting him down, then jump through the Weapon Armory door.把他放下，然后跳过武器库的门。')
        return 'laser_weapon_armory'
    
    else:
        print('DOES NOT COMPUTE!无效操作，请重新输入！')
        return 'central_corridor'
    
def laser_weapon_armory():
    print('You do a dive roll into the Weapon Armory, crouch and scan the room你在武器库里做了一个潜水翻滚，蹲下来扫描房间')
    print('for more Gothons that might be hiding. It\'s dead quiet, too quiet你还有可能隐藏的哥顿人。它很安静，也很安静')
    print('You stand up and run to the far side of the room and find the你站起来跑到房间的另一边，找到了')
    print('neutron bomb in its container. There\'s a keypad lock on the box中子弹在它的容器里。盒子上有一个键盘锁')
    print('and you need the code to get the bomb out. If you get the code如果你得到了代码')
    print('wrong 10 times then the lock closes forever and you can\'t get the bomb如果你错了10次，锁就永远关闭了，你就不能得到炸弹')
    print('The code is 3 digits.代码是3位数字。')
    code = '%d%d%d' % (randint(1,9), randint(1,9), randint(1,9))
    guess = input('[keypad]> ')
    guesses = 0

    while guess != code and guesses < 10:
        print('BZZZZEDDD!')
        guesses += 1  
        guess = input('[keypad]> ')

    if guess == code:
        print('The container clicks open and the seal breaks, letting gas out.容器发出咔嗒声，密封破裂，放出气体。')
        print('You grab the neutron bomb and run as fast as you can to the bridge你抓起中子弹，尽可能快地跑到桥上')
        print('where you must place it in the right spot.你必须把它放在正确的地方。')
        return 'the_bridge'
    else:
        print('The lock buzzes one last time and then you hear a sickening melting sound锁最后一次嗡嗡作响，然后你听到一种令人作呕的融化声')
        print('as the mechanism is fused together. You decide to sit there你决定坐在那里')
        print('and finally the Gothons blow up the ship from their ship你最后哥顿人从他们的船上炸毁了船')
        print('and you die.你死了。')
        return 'death'
    
def the_bridge():
    print('You burst onto the Bridge with the neutron destruct bomb你用中子毁灭炸弹冲进桥')
    print('under your arm and surprise 5 Gothons who are trying to你的手臂下面，惊讶地发现5个哥顿人正在试图')
    print('take control of the ship. Each of them has an even uglier控制船。他们每个人都有一个更丑陋的')
    print('clown costume than the last. They haven\'t pulled their小丑服装比上一个更丑陋。他们还没有拉出他们的')
    print('weapons out yet, as they see the active bomb under your arm.武器还没有出来，因为他们看到了你手臂下的活炸弹。')
    print('What do you do?你要怎么做？')

    action = input('1.slowly place the bomb 2.throw the bomb> ')

    if action == 'throw the bomb':
        print('In a panic you throw the bomb at the group of Gothons你惊慌失措地把炸弹扔给了一群哥顿人')
        print('and make a leap for the door. Right as you drop it a Gothon并且向门口跳去。就在你放下它的时候，一个哥顿人')
        print('Gothon shoots you right in the back killing you. 哥顿人朝你的背部开枪，杀了你。')
        print('As you die you see another Gothon frantically try to disarm你死了，你看到另一个哥顿人拼命试图解除武装')
        print('the bomb. You die knowing they will probably blow up when你死了，知道他们可能会爆炸')
        print('it goes off.它爆炸了。')
        return 'death'
    
    elif action == 'slowly place the bomb':
        print('You point your blaster at the bomb under your arm你用爆破器指着你手臂下的炸弹')
        print('and the Gothons put their hands up and start to sweat.哥顿人举起手开始流汗。')
        print('You inch backward to the door, open it, and then carefully你向后退到门口，打开门，然后小心地')
        print('place the bomb on the floor, pointing your blaster at it.把炸弹放在地上，用爆破器指着它。')
        print('You then jump back through the door, punch the close button你然后跳回门口，按下关闭按钮')
        print('and blast the lock so the Gothons can\'t get out.然后炸开锁，哥顿人无法出去。')
        print('Now that the bomb is placed you run to the escape pod to现在炸弹已经放置好了，你跑到逃生舱')
        print('get off this tin can.离开这个锡罐。')
        return 'escape_pod'
    
    else:
        print('DOES NOT COMPUTE!无效操作，请重新输入！')
        return 'the_bridge'
    
def escape_pod():
    print('You rush through the ship desperately trying to make it to你拼命地穿过船，试图让它到达')
    print('the escape pod before the whole ship explodes. It seems like在整艘船爆炸之前逃生舱。好像')
    print('hardly any Gothons are on the ship, so your run is clear of几乎没有哥顿人在船上，所以你的跑步是清晰的')
    print('interference. You get to the chamber with the escape pods,干扰。你到达了逃生舱的房间')
    print('and now need to pick one to take. Some of them could be damaged现在需要挑选一个。其中一些可能已经损坏了')
    print('but you don\'t have time to look. There\'s 5 pods, which one但你没有时间看。有5个舱，哪一个')
    print('do you take?你要怎么做？')

    good_pod = randint(1,5)
    guess = input('[pod #]> ')

    if int(guess) != good_pod:
        print('You jump into pod %s and hit the eject button.你跳进了%s号舱，按下了弹出按钮。' % guess)
        print('The pod escapes out into the void of space, then你跳进了%s号舱，按下了弹出按钮。' % guess)
        print('implodes as the hull ruptures, crushing your body in压碎你的身体')
        print('into jam jelly.你跳进了%s号舱，按下了弹出按钮。' % guess)
        return 'death'
    else:
        print('You jump into pod %s and hit the eject button.你跳进了%s号舱，按下了弹出按钮。' % guess)
        print('The pod easily slides out into space heading to你跳进了%s号舱，按下了弹出按钮。' % guess)
        print('the planet below. As it flies to the planet, you look back舱轻松地滑出太空，飞向下面的行星。当它飞向行星时，你回头看')
        print('back and see your ship implode then explode like a你回头看，看到你的船像一个')
        print('bright star, taking out the Gothon ship at the same time.明亮的星星，同时消灭了哥顿人的船。')
        print('time, You won!你赢了！')
        exit(0)

ROOMS = {
    'death': death,
    'central_corridor': central_corridor,
    'laser_weapon_armory': laser_weapon_armory,
    'the_bridge': the_bridge,
    'escape_pod': escape_pod
}

def runner(map,start):   # 这个函数的作用是不断调用ROOMS里面的函数，直到返回值为death
    next = start

    while True:
        room = map[next]
        print('\n--------')
        next = room()

runner(ROOMS, 'central_corridor')