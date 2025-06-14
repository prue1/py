import re

def pprint(str, p):
    match = re.match(p, str)
    print(f"{str}<->{p}->{"T" if match is not None else "F"}")
    if(match):
        print(match.groupdict())
        for idx, group in enumerate(match.groups()):
            print(f"   g{idx+1}:{group}")

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

pprint("distance is 300 miles.", "([a-z\s]*+)([0-9]*) miles\.")

pprint("hello world", "(hell.*o).*") # 貪多
pprint("hello world", "(hell.*?o).*") # 不貪多，加一個問號(?)
pprint("hello world", "h([a-z]*+).*") # possessive, no backtracking
pprint("Its price is 130.0", "([a-zA-z\s]*)(\d*+)\.(\d*)")

pprint("Berry is $30元", "(.*) is \$(\d*)元") # 跳掉 $

pprint("berry", "b(.*)y")
pprint("berry", "b(.*+)y")
pprint("berry", "b(.*+)")

pprint("abcd", "^(abc)")
pprint("abcd", "^(abc).*")

pprint("abcd", "^(?P<gg1>abc).*") # (?<name>X) 命名group，named group
pprint("abcd", "^(?:abc).*") # ?: 忽略這個group
pprint("abcd", "^a(.*)d$")

pprint("abcde", "ab(?=[a-z])(.*)") # 理解成：(?=)僅做為邏輯條件，不屬於pattern的一部份
#pprint("abcde", "([ab]{2})(?<=[a-z]*)cde") # error: look-behind requires fixed-width pattern
pprint("abcde", "([ab]{2})(?<=[a-z])cde") # 同上，但拿掉星號*

pprint("abcabcabcde", "((abc)*)de");
pprint("abc123abcabcabde", "[(abc)123]*de"); # [] 裏的 () 似乎沒特別意義，這個pattern等價於 [abc123]*de。如下：
pprint("abc123abcabcabde", "[abc123]*de");