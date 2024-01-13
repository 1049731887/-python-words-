import random


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
    clear_screen()
    print("开始学习\n")
    day = readfile("day.env")
    wordnum = day * 5
    Es = list(words.keys())
    tostudy_Es = Es[wordnum : wordnum + 5]
    Cs = list(words.values())
    tostudy_Cs = Cs[wordnum : wordnum + 5]
    # for i in range(0, 5):
    #     print("正在学习……\n")
    #     print("单词：", tostudy_Es[i])
    #     print("释义：", tostudy_Cs[i])
    #     input("\n按 Enter 键下一个")
    #     clear_screen()


def EcC():
    print("英文选中文\n")
    day = readfile("day.env")
    wordnum = day * 5
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
        # print(choices)
        print("第", i + 1, "个：\n")
        print("单词：", tostudy_Es[i])
        print("A. ", choices[0])
        print("B. ", choices[1])
        print("C. ", choices[2])
        print("D. ", choices[3])
        ans = int(let_choose())-1
        print("------调试： ",ans,choices[ans],tostudy_Cs[i])
        if choices[ans]==tostudy_Cs[i]:
            print("选对了！！！！！！")
        input()
        clear_screen()


def CcE():
    print("中文选英文\n")
    day = readfile("day.env")
    wordnum = day * 5
    Es = list(words.keys())
    tostudy_Es = Es[wordnum : wordnum + 5]
    Cs = list(words.values())
    tostudy_Cs = Cs[wordnum : wordnum + 5]
    for i in range(0, 5):
        print("第", i + 1, "个：")
        print("单词：", tostudy_Es[i])
        print("释义：", tostudy_Cs[i])
        input("\n按 Enter 键下一个")
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
    char = input("请选择：")
    try:
        if char.isalpha():
            output_str += letter_to_number[char.upper()]
        # 如果字符是数字，就直接保留它
        elif char.isdigit():
            output_str += char
    except:
        output_str = let_choose()
    # 返回转换后的结果
    if int(output_str) > 4:
        output_str = let_choose()
    return output_str


print()
day = readfile("day.env")
print("------第", int(day), "天------")
words = readenv()
words_source = 1
if int(day) == 0:
    print("欢迎进入单词背记系统！")
    # words_source = input("请选择词库：")

# print("words_source: "+str(words_source))

# print(let_choose())

print("单词（字典）：", words)

turn()
print()
