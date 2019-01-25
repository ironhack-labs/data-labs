"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class ClimeStairs:
    """
    Class constructor
    total_steps: how many steps in total in the stair
    """
    def __init__(self, total_steps=10): 
        self.total_steps = total_steps
        self.calculation_count = 0

    """
    This function calculates how many solutions are there to reach the top when I am currently at the ith step
    i - the step I am currently at
    """
    def calc_solutions(self, i):
        # If the current step is already larger than total steps, there's 0 solution
        if i > self.total_steps:
            return 0

        # If the current step equals to the total steps, there is only one solution because I've reached the top
        if i == self.total_steps:
            return 1

        # If I am still in the middle of the stair, continue calculating
        self.calculation_count += 1

        # Call the current function recursively. 
        # The number of solutions at the ith step equals to the number of solutions at the (i+1)th step 
        # plus the number of solutions at the (i+2)th step
        return(self.calc_solutions(i+1) + self.calc_solutions(i+2))

    def get_calculation_count(self):
        return self.calculation_count

    def solve(self):
        return self.calc_solutions(0)

new_challenge = ClimeStairs(10)
print('Answer is: ' + str(new_challenge.solve()))
print('Total calculations: ' + str(new_challenge.get_calculation_count()))
