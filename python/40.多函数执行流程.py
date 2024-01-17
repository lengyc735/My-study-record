glo_num = 0

def test_1():
    global glo_num
    glo_num = 777

def test_2():
    print(glo_num)

print(glo_num) # 0
test_2() # 0
test_1()
test_2() # 777
print(glo_num) # 777