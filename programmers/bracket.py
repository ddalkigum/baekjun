s = "(())()"

def solution(s):
    answer = True
    while True:
        if s[0] == ")":
            return False
        elif s[-1] == "(":
            return False
        else:
            s = s.replace("()", "")
            if len(s) == 1:
                return False
            elif len(s) == 0:
                return True

solution(s)