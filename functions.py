def readenv():
	"""读取words，返回一个字典"""
	words={}
	filename = "English.txt"
	with open(filename) as file_object:
		English = file_object.readlines()
	filename = "Chinese.txt"
	with open(filename) as file_object:
		Chinese = file_object.readlines()
	n=len(English)
	for i in range(0,n):
		words[English[i].rstrip()] = Chinese[i].rstrip()
	return words

def choose_words():
	return 1

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

def study():
    print("study")
    words = readenv()
    day = readfile("day.env")
    wordnum = day * 10
    Es = words.keys()
    tostudy.Es = Es[wordnum:wordnum+10]
    print("study_end")

def let_choose():
    # 定义一个字典，将字母映射到数字
    letter_to_number = {"A": "1", "B": "2", "C": "3", "D": "4", "a": "1", "b": "2", "c": "3", "d": "4"}
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
    if int(output_str)>4:
        output_str = let_choose()
    return output_str
