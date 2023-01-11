# Input: The first line contains an integer n, the next one contains
#        The next line is a sequence of n integers.
# Output: 1, if there is an element that is repeated more than n/2 times, 
#         0 otherwise.


def get_majority_element_naive(a, left, right):
    count = {}
    majority_bound = len(a) // 2 + 1
    for i in a:        
        if i in count:
            count[i] += 1
            if count[i] >= majority_bound:
                print(1)
                return
        else:
            count[i] = 1
    # print(count)
    print(0)


def get_majority_element(a, left, right):
    if left == right:  # only 1 element => returns right
        return -1
    if left + 1 == right:  # 2 elements => there is no majority element
        return a[left]
    # write your code here

    return -1  # -1 means there is the majority element


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    # get_majority_element_naive(a, 0, n)
    if get_majority_element(a, 0, len(a)) != -1:
        print(1)
    else:
        print(0)
