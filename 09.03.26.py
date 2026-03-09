# a = input()
# def lower(a):
#     b = str()
#     for i in a:
#         if 65<= ord(i)<=90:
#             i = chr(ord(i)+32)
#         b += i
#     return b
# print(lower(a))
tests = [("Hello World","Hello",True)]
def startswith(string,sub_string):
    c = 0
    for i in range(len(sub_string)):
        s1=string[i]
        s2 = sub_string[i]
        # if s1 != s2:
           # return False
    #return True
        return string[:len(sub_string)]== sub_string
        if s1 == s2:
            c+=1
    if c == len(sub_string):
        return True
    else:
        return False
for i in tests:
    string=i[0]
    sub_string = i[1]
    res = startswith(string,sub_string)
    if res != i[2]:
        print("Программа неверная")


