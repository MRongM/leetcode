"""
去掉k个字符生成最小整形,前置0去除
10200 1 => 200
1234 1 => 123
143234 3 => 124
1432219 3 => 1219
5337 2 => 33
4321 2 => 21
"""


def removeK(ss, k):
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

    for i in range(len(ans)):
        if ans[i] != '0':
            ans = ans[i:]
            break

    return ans


ss = '1432219'
k = 3

# ss = '10200'
# k = 1
print(removeK(ss, k))
