# leetcode-solutions
このリポジトリは、私がLeetCodeの問題を解きながらアルゴリズムに関する能力を鍛えるための記録です。
主にコーディング面接対策と問題解決能力の向上を目的とし、まずは毎日コードを書くことに慣れるところから始めます。

LeetCode開始：2025/11/24
GitHubへの記録開始：2025/12/09
言語：Python3


メモ
enumerate()
    for i, j in enumerate(list):
    --> i==index, j==content
    ex. l = [1,2,3]
        for i, j in enumerate(l):
            print(i,j**2)
        # 0 1
        # 1 4
        # 2 9

排他的論理和 '^'
    数字で使うと重複を排除することができる。
    ex. True^True or False^False = False
        True^False = True
        1^3^3 = 1
        * 3^6 = (11)_2 ^ (110)_2 = (101)_2 = 5

