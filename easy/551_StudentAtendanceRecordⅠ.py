class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 0
        con_late = 0
        for i in s:
            if i == 'A':
                absent += 1
                con_late =0
                if absent >= 2:
                    return False
            elif i == 'L':
                con_late += 1
                if con_late >= 3:
                    return False
            else:
                con_late = 0
        return True