# Input: A sequence of non-negative integers.
# Output: The maximum value that can be obtained by multiplying 
# two different elements from the sequence.

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            if numbers[first] * numbers[second] 
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
