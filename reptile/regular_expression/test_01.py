# import re


# a = 'cat'
# b = 'bird'
# string = 'dog and cat'
# print(re.search(a, string))
# print(re.search(b, string))

# import re


# a = r"r[au]n"
# print(re.search(a, "dog runs to cat"))
# import re


# # 匹配正则表达式，r使之成为正则表达式，[]里面可以是一个或者多个，既可以匹配ran又可以匹配run，请看代码
# a = r"r[au]n"
# print('1')
# # 匹配以r开头，中间是a或者u都可以，在以n结尾的字符串
# print(re.search(a, "dog runs to cat"))
# print('2')
# # 匹配以r开头，中间是大写(A-Z)的任意字母都可以，在以n结尾的字符串
# print(re.search(r'r[A-Z]n', "dog runs to cat"))
# print('3')
# # 匹配以r开头，中间是小写（a-z）的任意字母都可以，在以n结尾的字符串
# print(re.search(r'r[a-z]n', "dog runs to cat"))
# print('4')
# # 匹配以r开头，中间是0-9的任意数字都可以，在以n结尾的字符串
# print(re.search(r'r[0-9]n', "dog runs to cat"))
# print('5')
# # 匹配以r开头，中间是A-Z或0-9任意字母都可以，在以n结尾的字符串
# print(re.search(r'r[a-z0-9]n', "dog runs to cat"))
# import re


# print("\d")
# # \d: 代表匹配r n 中间只要是数字，就可以匹配到
# print(re.search(r"r\dn", "run r4n"))
# print("\D")
# # \D: 代表匹配r n 中间只要是不是数字，就可以匹配到
# print(re.search(r"r\Dn", "run r4n"))

# import re


# # \s:
# print("\s")
# print(re.search(r"r\sn", "r\nn r4n"))
# # \S:
# print("\S")
# print(re.search(r"r\Sn", "r\nn r4n"))

# import re


# # \w: 匹配所有包含任意字母、数字和下划线_的字符串
# print("\w")
# print(re.search(r"r\wn", "r\nn r4n"))
# # \W: 匹配所有不包含任意字母、数字和下划线_的字符串
# print("\W")
# print(re.search(r"r\Wn", "r\nn r4n"))

# import re


# # \b: 匹配所有run两边各带一个空格的字符串
# print("\\b")
# print(re.search(r'\bruns\b', "dog runs to cat"))
# # \B: 匹配所有非run两边各带一个空格的字符串
# print("\B")
# print(re.search(r"\B runs \B", "dog   runs   to cat"))

# import re


# # \双斜线
# print("\\")
# print(re.search(r"runs\\", "runs\ to me"))
# # . 点
# print(".")
# print(re.search(r"r.ns", "r[ns\ to me"))
# import re


# # ^ :从句首开始一直匹配到g
# print('^')
# print(re.search(r"^dog", "dog   runs   to cat"))
# # $ :从c开始一直匹配到句尾
# print('$')
# # print(re.search(r"cat$", "dog   runs   to cat"))

# import re


# # ? :是否,这个数据是否包含我想要的数据，不管包含还是不包含，都会输出
# print(re.search(r"Mon(day)?", "Monday"))
# print(re.search(r"Mon(day)?", "Mon"))

# import re


# # 多行匹配
# string = '''
# dog runs to cat.
# I run to dog.
# '''
# print(re.search(r"^I", string))
# print(re.search(r"^I", string, flags=re.M))
# import re


# # *: 出现0次或者多次
# print(re.search(r"ab*", "a"))
# print(re.search(r"ab*", "abbbbbbb"))

# import re


# # +: 出现1次或者多次
# print(re.search(r"ab+", "a"))
# print(re.search(r"ab+", "abbbbbbb"))
# import re


# # {n,m}: 出现n-m次
# print(re.search(r"ab{2,10}", "a"))
# print(re.search(r"ab{2,10}", "abbbbbbb"))
# import re


# # 首先，是分成了两组，(\d+)和Date:(.+)，group()代表是不分组，全部输出，组号从1开始
# # (\d+) 代表匹配数字出现了一次或者多次的字符串
# # 
# match = re.search(r"(\d+), Date:(.+)", "ID:021523, Date:Feb/29/3/2019")
# print(match.group())
# print(match.group(1))
# print(match.group(2))
# import re


# # 首先，是分成了两组，(\d+)和Date:(.+)，group()代表是不分组，全部输出，组号从1开始
# # (\d+) 代表匹配数字出现了一次或者多次的字符串
# # 
# match = re.search(r"(\d+), Date:(.+)", "ID:021523, Date:Feb/29/3/2019")
# print(match.group())
# print(match.group(1))
# print(match.group(2))
# print("-------------------------------")
# # 为了避免出现混多组，用序号标记容易混淆，我们也可以给组加上名字?<name>
# match1 = re.search(r"(?P<id>\d+), Date:(?P<date>.+)", "ID:021523, Date:Feb/29/3/2019")
# print(match1.group('id'))
# print(match1.group('date'))
# import re


# # findall 匹配所有符合的字符串
# print(re.findall(r"r[ua]n", "run ran ren"))
# print("1---------------------------")
# # | :或者的意思 or
# print(re.findall(r"r(u|a)n", "run ran ren"))
# import re


# # sub 替换将正则表达式替换成其他字符串
# print(re.sub(r"r[ua]n", "cathes","run ran ren"))
# # split 分裂，将匹配到的符号两边的数据，分割开来
# print(re.split(r"[,;\.]", "a;b,c.d;e"))
import re


compiled_re = re.compile(r"r[ua]n")
print(compiled_re.search("dog ran to cat"))