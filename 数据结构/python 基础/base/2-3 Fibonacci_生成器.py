def Fibonacci(num):
    a, b = 0, 1
    current_num = 0
    while current_num < num:
        yield a
        a, b = b, a + b
        current_num += 1
    return "ok....."


obj = Fibonacci(20)

while True:
    try:
        ret = next(obj)
        print(ret)
    except Exception as e:
        print(e)
        print(e.args)
        print(e.value)
        break
