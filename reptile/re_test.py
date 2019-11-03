import re

line = "Cats are smarter than dogs"

print("------------compare re.match and re.search------------")
matchObj = re.match(r'dogs', line, re.M | re.I)
if matchObj:
    print("match --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")

matchObj = re.search(r'dogs', line, re.M | re.I)
if matchObj:
    print("search --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")

print("------------re.sub------------")
phone = "2004-959-559 # This is Phone Number"
print("Phone Num : ", phone)
# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print("Phone Num :", num, "AAA")
# Remove anything other than digits
num = re.sub(r'\D', "", phone)
print("Phone Num :", num)

print("------------正则表达式修饰符:可选标志------------")
print("修饰符	描述")
print("re.I	使匹配对大小写不敏感")
print("re.L	做本地化识别（locale-aware）匹配")
print("re.M	多行匹配，影响 ^ 和 $")
print("re.S	使 . 匹配包括换行在内的所有字符")
print("re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \\b, \B.")
print("re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。")

print("------------正则表达式模式------------")
print("模式	描述")
print("^	匹配字符串的开头")
print("$	匹配字符串的末尾。")
print(
    ".	匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。或者要匹配包括 '\\n' 在内的任何字符，请使用象 '[.\\n]' 的模式。")
print("[...]	用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'")
print("[^...]	不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。")
print("re*	匹配0个或多个的表达式。")
print("re+	匹配1个或多个的表达式。")
print("re?	匹配0个或1个由前面的正则表达式定义的片段，贪婪方式")
print("re{ n}	")
print("re{ n,}	精确匹配n个前面表达式。")
print("re{ n, m}	匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式")
print("a| b	匹配a或b")
print("(re)	G匹配括号内的表达式，也表示一个组")
print("(?imx)	正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域。")
print("(?-imx)	正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域。")
print("(?: re)	类似 (...), 但是不表示一个组")
print("(?imx: re)	在括号中使用i, m, 或 x 可选标志")
print("(?-imx: re)	在括号中不使用i, m, 或 x 可选标志")
print("(?#...)	注释.")
print("(?= re)	前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边。")
print("(?! re)	前向否定界定符。与肯定界定符相反；当所含表达式不能在字符串当前位置匹配时成功")
print("(?> re)	匹配的独立模式，省去回溯。")
print("\w	匹配字母数字,等价于'[A-Za-z0-9_]'")
print("\W	匹配非字母数字,等价于 '[^A-Za-z0-9_]'")
print("\s	匹配任意空白字符，等价于 [\\t\\n\\r\\f].")
print("\S	匹配任意非空字符,等价于 [^ \\f\\n\\r\\t\\v]")
print("\d	匹配任意数字，等价于 [0-9].")
print("\D	匹配任意非数字,等价于 [^0-9]")
print("\A	匹配字符串开始")
print("\Z	匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。c")
print("\z	匹配字符串结束")
print("\G	匹配最后匹配完成的位置。")
print("\\b	匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配\"never\" 中的 'er'，但不能匹配 \"verb\" 中的 'er'。")
print("\B	匹配非单词边界。'er\B' 能匹配 \"verb\" 中的 'er'，但不能匹配 \"never\" 中的 'er'。")
print("\\n, \\t, 等.	匹配一个换行符。匹配一个制表符。等")
print("\\1...\9	匹配第n个分组的子表达式。")
print("\\10	匹配第n个分组的子表达式，如果它经匹配。否则指的是八进制字符码的表达式。")
