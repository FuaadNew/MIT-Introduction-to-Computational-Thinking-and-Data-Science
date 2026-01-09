###########################
# 6.0002 Problem Set 1b: Space Change
# Name: fuaadnew
# Collaborators: None
# Time: 1 hour
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # TODO: Your code here
    def dfs(i,egg_length,weight):
        if (i,egg_length, weight) in memo:
            return memo[(i,egg_length, weight)]
        if weight > target_weight:
            return float('inf')
        if  i >= len(egg_weights):
            return float('inf')
        if  weight == target_weight:
            return egg_length
        #include egg
        include = dfs(i, egg_length + 1, weight +  egg_weights[i])
        #exclude
        exclude = dfs(i + 1, egg_length, weight)

       
        memo[(i,egg_length, weight)] = min(include, exclude)
        return  memo[(i,egg_length, weight)]

        #no include egg
    
    return dfs(0,0,0)

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()