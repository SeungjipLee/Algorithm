p = "(()())()"


def is_correct(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        else:
            if not stack:
                return False
            stack.pop()
    return not stack


def split_balanced(s):
    balance = 0
    for i in range(len(s)):
        if s[i] == '(':
            balance += 1
        else:  # s[i] == ')'
            balance -= 1
        if balance == 0:
            return s[:i + 1], s[i + 1:]
    return s, ''


def solution(p):
    if p == '':
        return ''
    u, v = split_balanced(p)
    if is_correct(u):
        return u + solution(v)
    else:
        result = '('
        result += solution(v)
        result += ')'
        u_prime = u[1:-1]
        u_prime = ''.join('(' if c == ')' else ')' for c in u_prime)
        result += u_prime
        return result


print(solution(p))
