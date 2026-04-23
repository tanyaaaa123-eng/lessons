def user(c,log_func):
    a = int(input())
    current = 0
    for i in c:
        a = i(a)
        print (log_func(a))
c=[lambda current,a:a+2,lambda current, a:a*3,lambda current,a:a+1]
log_func=lambda a:f"[Log] {a}"
print(user(c,log_func))
