word_map = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tvu",
    "9": "wxyz",
}

res = []
item = []


def letterCombinations(digits):
    if not digits:
        res.append(''.join(item))
        return
    word = word_map[digits[0]]
    for w in word:
        item.append(w)
        letterCombinations(digits[1:])
        item.pop(-1)


def letterCombinations2(digits):
    key = {k: [i for i in v] for k, v in word_map.items()}
    ans = ['']
    for i in digits:
        ans = [pre + sub for pre in ans for sub in key[i]]

    return ans


digit = "23"
# letterCombinations(digit)
res = letterCombinations2(digit)
# res = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
print(res)
