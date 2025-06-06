import re

def pprint(str, p):
    x = re.search(p, str)
    print(str + "<->" + p)
    if(x):
        for group in x.groups():
            print(group)

pprint("abc", "abc")
pprint("abc", "ab")
pprint("abc", "ab.")
pprint("abc", "...")
pprint("abc", "[abc]abc")
pprint("abc", "[abc]bc")
pprint("abc", "[a|ab|abc]bc")
pprint("abc", "[a|b|c]bc")
pprint("abc", "(.)(.)(.)")

pprint("Hello", ".*([Hh][Ee][Ll][Ll][Oo]).*")
pprint("hello", ".*([Hh][Ee][Ll][Ll][Oo]).*")
pprint("Hello World.", ".*([Hh][Ee][Ll][Ll][Oo]).*")
pprint("hello world.", ".*([Hh][Ee][Ll][Ll][Oo]).*")
pprint("HHello world.", ".*([Hh][Ee][Ll][Ll][Oo]).*")
pprint("HHello world.", ".*([Hh][Ee][Ll][Ll][Oo]).*")

pprint("distance is 300 miles.", "([a-z\\s]*+)([0-9]*) miles\\.")

pprint("hello world", "(hell.*o).*") # 貪多
pprint("hello world", "(hell.*?o).*") # 不貪多，加一個問號(?)
pprint("hello world", "h([a-z]*+).*") # possessive, no backtracking
pprint("Its price is 130.0", "([a-zA-z\\s]*)(\\d*+)(\\.\\d*)")

pprint("Berry is $30元", "(.*) is \\$(\\d*)元") # 跳掉 $

pprint("berry", "b(.*)y")
pprint("berry", "b(.*+)y")
pprint("berry", "b(.*+)")

pprint("abcd", "^(abc)")
pprint("abcd", "^(abc).*")

pprint("abcd", "^(?P<gg1>abc).*") # (?<name>X) 命名group
pprint("abcd", "^(abc).*")
pprint("abcd", "^(?:abc).*") # ?: 忽略這個group
pprint("abcd", "^a(.*)d$")

pprint("abcde", "ab(?=[a-z])(.*)") # 理解成：(?=)僅做為邏輯條件，不屬於pattern的一部份
#pprint("abcde", "([ab]{2})(?<=[a-z]*)cde") # error: look-behind requires fixed-width pattern
pprint("abcde", "([ab]{2})(?<=[a-z])cde") # 同上，但拿掉星號*