"""
Ref: https://leetcode.com/problems/climbing-stairs/solution/
"""

class ClimeStairs:
    def __init__(self, total_steps=10):
        self.total_steps = total_steps
        self.steps_stack = [1, 2]
        self.calculation_count = 0

    def calc_solutions(self, n):
        self.calculation_count += 1
        return(self.steps_stack[n-1] + self.steps_stack[n-2])

    def get_calculation_count(self):
        return self.calculation_count

    def solve(self):
        for i in range(2, self.total_steps):
            self.steps_stack.append(self.calc_solutions(i))
        return self.steps_stack[self.total_steps-1]

new_challenge = ClimeStairs(10000)
print('Answer is: ' + str(new_challenge.solve()))
print('Total calculations: ' + str(new_challenge.get_calculation_count()))
