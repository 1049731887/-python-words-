import random
import time

def readenv():
    """读取words，返回一个字典"""
    words = {}
    filename = "English.txt"
    with open(filename) as file_object:
        English = file_object.readlines()
    filename = "Chinese.txt"
    with open(filename) as file_object:
        Chinese = file_object.readlines()
    n = len(English)
    for i in range(0, n):
        words[English[i].rstrip()] = Chinese[i].rstrip()
    return words

def clear_screen():
    print("\033[2J\033[H", end="")

def readfile(filename):
    """读取文件返回int"""
    with open(filename) as file_object:
        contents = file_object.read()
        return int(contents.rstrip())

def turn():
    """一个轮回"""
    study()
    EcC()
    CcE()
    # day+=1 并写入文件
    day = readfile("day.env")
    day += 1
    with open("day.env", "w") as file_object:
        file_object.write(str(day))

def study():
    # clear_screen()
    print("开始学习\n")
    day = readfile("day.env")
    wordnum = day * 5
    Es = list(words.keys())
    tostudy_Es = Es[wordnum : wordnum + 5]
    Cs = list(words.values())
    tostudy_Cs = Cs[wordnum : wordnum + 5]
    for i in range(0, 5):
        print("正在学习……\n")
        try:
            print("单词：", tostudy_Es[i])
            print("释义：", tostudy_Cs[i])
        except IndexError:
            clear_screen()
            print("恭喜您学完啦~！！")
            quit()
        try:
            input("\n按 Enter 键下一个")
        except KeyboardInterrupt:
            quit()
        clear_screen()

def EcC():
    print("英文选中文\n")
    day = readfile("day.env")
    wordnum = day * 5
    error_words_n=[]
    Es = list(words.keys())
    tostudy_Es = Es[wordnum : wordnum + 5]
    Cs = list(words.values())
    tostudy_Cs = Cs[wordnum : wordnum + 5]

    for i in range(0, 5):
        # 设置其他答案
        otherCs = tostudy_Cs[:]
        otherCs.remove(tostudy_Cs[i])
        choices = random.sample(otherCs, 3)
        choices.append(tostudy_Cs[i])
        random.shuffle(choices)
        # 开始选
        print("第", i + 1, "个：\n")
        print("单词：", tostudy_Es[i])
        print("A. ", choices[0])
        print("B. ", choices[1])
        print("C. ", choices[2])
        print("D. ", choices[3])
        ans = int(let_choose()) - 1
        print()
        if choices[ans] == tostudy_Cs[i]:
            print("选对了！！！！！！")
            time.sleep(1)
        else:
            print("选错了。。。。。。")
            time.sleep(1)
            error_words_n.append(i)
        clear_screen()
    # 重新选择错误的
    for i in error_words_n:
        # 设置其他答案
        otherCs = tostudy_Cs[:]
        otherCs.remove(tostudy_Cs[i])
        choices = random.sample(otherCs, 3)
        choices.append(tostudy_Cs[i])
        random.shuffle(choices)
        # 开始选
        print("第", i + 1, "个：\n")
        print("单词：", tostudy_Es[i])
        print("A. ", choices[0])
        print("B. ", choices[1])
        print("C. ", choices[2])
        print("D. ", choices[3])
        ans = int(let_choose()) - 1
        print()
        if choices[ans] == tostudy_Cs[i]:
            print("选对了！！！！！！")
            time.sleep(1)
        else:
            print("又选错了。。。。。。")
            time.sleep(1)
            error_words_n.append(i)
        clear_screen()
    for i in error_words_n:
        # 设置其他答案
        otherCs = tostudy_Cs[:]
        otherCs.remove(tostudy_Cs[i])
        choices = random.sample(otherCs, 3)
        choices.append(tostudy_Cs[i])
        random.shuffle(choices)
        # 开始选
        print("第", i + 1, "个：\n")
        print("单词：", tostudy_Es[i])
        print("A. ", choices[0])
        print("B. ", choices[1])
        print("C. ", choices[2])
        print("D. ", choices[3])
        ans = int(let_choose()) - 1
        print()
        if choices[ans] == tostudy_Cs[i]:
            print("选对了！！！！！！")
            time.sleep(1)
        else:
            print("又双叒叕选错了。。。。。。")
            time.sleep(1)
            error_words_n.append(i)
        clear_screen()

def CcE():
    print("英文选中文\n")
    day = readfile("day.env")
    wordnum = day * 5
    error_words_n=[]
    Cs = list(words.values())
    tostudy_Cs = Cs[wordnum : wordnum + 5]
    Es = list(words.keys())
    tostudy_Es = Es[wordnum : wordnum + 5]

    for i in range(0, 5):
        # 设置其他答案
        otherEs = tostudy_Es[:]
        otherEs.remove(tostudy_Es[i])
        choices = random.sample(otherEs, 3)
        choices.append(tostudy_Es[i])
        random.shuffle(choices)
        # 开始选
        print("第", i + 1, "个：\n")
        print("单词：", tostudy_Cs[i])
        print("A. ", choices[0])
        print("B. ", choices[1])
        print("C. ", choices[2])
        print("D. ", choices[3])
        ans = int(let_choose()) - 1
        print()
        if choices[ans] == tostudy_Es[i]:
            print("选对了！！！！！！")
            time.sleep(1)
        else:
            print("选错了。。。。。。")
            time.sleep(1)
            error_words_n.append(i)
        clear_screen()
    # 重新选择错误的
    for i in error_words_n:
        # 设置其他答案
        otherEs = tostudy_Es[:]
        otherEs.remove(tostudy_Es[i])
        choices = random.sample(otherEs, 3)
        choices.append(tostudy_Es[i])
        random.shuffle(choices)
        # 开始选
        print("第", i + 1, "个：\n")
        print("单词：", tostudy_Cs[i])
        print("A. ", choices[0])
        print("B. ", choices[1])
        print("C. ", choices[2])
        print("D. ", choices[3])
        ans = int(let_choose()) - 1
        print()
        if choices[ans] == tostudy_Es[i]:
            print("选对了！！！！！！")
            time.sleep(1)
        else:
            print("又选错了。。。。。。")
            time.sleep(1)
            error_words_n.append(i)
        clear_screen()
    for i in error_words_n:
        # 设置其他答案
        otherEs = tostudy_Es[:]
        otherEs.remove(tostudy_Es[i])
        choices = random.sample(otherEs, 3)
        choices.append(tostudy_Es[i])
        random.shuffle(choices)
        # 开始选
        print("第", i + 1, "个：\n")
        print("单词：", tostudy_Cs[i])
        print("A. ", choices[0])
        print("B. ", choices[1])
        print("C. ", choices[2])
        print("D. ", choices[3])
        ans = int(let_choose()) - 1
        print()
        if choices[ans] == tostudy_Es[i]:
            print("选对了！！！！！！")
            time.sleep(1)
        else:
            print("又双叒叕选错了。。。。。。")
            time.sleep(1)
            error_words_n.append(i)
        clear_screen()

def let_choose():
    # 定义一个字典，将字母映射到数字
    letter_to_number = {
        "A": "1",
        "B": "2",
        "C": "3",
        "D": "4",
        "a": "1",
        "b": "2",
        "c": "3",
        "d": "4",
    }
    # 定义一个空字符串，用于存储转换后的结果
    output_str = ""
    # 遍历输入字符串中的每个字符
    try:
        char = input("请选择：")
    except KeyboardInterrupt:
        quit()
    try:
        if char.isalpha():
            output_str += letter_to_number[char.upper()]
        # 如果字符是数字，就直接保留它
        elif char.isdigit():
            output_str += char
        if int(output_str) > 4:
            print("请选择范围内的项！")
            output_str = let_choose()
    except ValueError:
        print("输入选项并回车！")
        output_str = let_choose()
    except KeyError:
        print("请在上述选项中选择！")
        output_str = let_choose()
    # else:
    #     output_str = let_choose()
    # 返回转换后的结果
    return output_str

def quit():
    print("\n退出系统！")
    time.sleep(1)
    exit()

print()
day = readfile("day.env")

words = readenv()
words_source = 1
if int(day) == 0:
    print("欢迎进入单词背记系统！！！")
    print("使用 Ctrl+C 退出系统！")
else:
    print("------第", int(day), "天------")

#print("单词（字典）：", words)
turn_n=[1]
for i in turn_n:
    turn()
    want=input("是否还要再来一轮？输入【1/0 是/否】：")
    want=int(want)
    if want:
        turn_n.append(1)



time.sleep(2)