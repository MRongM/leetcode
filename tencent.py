"""
去掉k个字符生成最小整形,前置0去除
10200 1 => 200
1234 1 => 123
143234 3 => 124
1432219 3 => 1219
5337 2 => 33
4321 2 => 21
"""


def removek(ss, k):
    if len(ss) == k:
        return '0'

    stack = []
    for i in range(len(ss)):
        value = ss[i]
        if not stack:
            stack.append(value)
        else:
            if value < stack[-1]:
                stack.pop()
                stack.append(value)
                k -= 1
            else:
                stack.append(value)
        if k == 0:
            ans = ''.join(stack) + ss[i + 1:]
            break
    else:
        ans = ''.join(stack[:len(stack) - k])

    return str(int(ans))


def removek2(ss, k):
    if len(ss) == k:
        return '0'

    ans = ''
    for idx, i in enumerate(ss):
        if not ans:
            ans += i
        else:
            if ans[-1] > i:
                ans = ans[:-1] + i
                k -= 1
            else:
                ans += i
        if k == 0:
            ans += ss[idx + 1:]
            break
    if k:
        ans = ans[:len(ans) - k]

    return str(int(ans))


ss = '100000'
k = 4

# ss = '1432219'
# k = 3
print(removek2(ss, k))
