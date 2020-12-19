import programmers.center_word

center_word

def function():
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        pass
    elif m % n == 0:
        print("factor")
        function()
    elif n % m == 0:
        print("multiple")
        function()
    else:
        print("neither")
        function()


function()
