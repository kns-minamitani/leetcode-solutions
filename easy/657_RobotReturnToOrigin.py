class Solution:
    def judgeCircle(self, moves: str) -> bool:
        move_counter = {'U':0, 'D':0, 'L':0, 'R':0}
        for i in moves:
            move_counter[i] += 1
        
        return move_counter['U'] == move_counter['D'] and move_counter['L'] == move_counter['R']