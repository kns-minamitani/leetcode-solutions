class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        title_list = list(columnTitle)
        title_list.reverse()
        column_number = 0
        for i in range(len(title_list)):
            column_number += (ord(title_list[i]) - ord('A') + 1) * 26 ** i
        return column_number