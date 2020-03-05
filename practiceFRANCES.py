# Partner 1: Frances McConnell
# Partner 2: Annie Watson

#######
# Assignment Name: GitHub Practice - 03/03/2020 - 20 points
import random
import numpy as np

def getNRandom(n):
	'''takes in an integer and returns a list of n random integers between 1 and 10, inclusive'''
    for i in range(n):
        print random.randint(1,11)

def multiplyRandom(n):
	'''takes in a list of n numbers and returns the product of the numbers'''
    nums = np.randint(low=None, high=None, size=n)
    answer = 1
    for i in range(nums):
        answer = answer*i
    return answer

multiplyRandom(5)

def main():
	print(multiplyRandom(getNRandom(10))

if __name__ == "__main__":
	main()
