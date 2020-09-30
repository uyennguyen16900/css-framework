import math

def rotate_array(a,n):
    remainder = len(a) % n
    temp = 0
    count = 1
    while count <= n:
        temp = a[-count]
        i = 0
        while i < len(a) // n - 1:
            a[-(i*n+count)] = a[-(i*n+n+count)]
            print(-(i*n+n+count))
            i+=1
        
        if remainder != 0:
            print(((i-1)*n+remainder+count+1), -((i-1)*n+remainder*2+count+1))
            a[-((i-1)*n+remainder+count+1)] = a[-((i-1)*n+remainder*2+count+1)]
        #     print(a)
        # else:
        #     a[-count+n] = temp

        count+=1
    




       
    return a
        
def rotate_matrix(matrix):
    n = len(matrix)
    for x in range(n // 2):
        for y in range(x, n - x - 1):
            temp = matrix[n-y-1][x]
            matrix[n-y-1][x] = matrix[n-x-1][n-y-1]
            matrix[n-x-1][n-y-1] = matrix[y][n-x-1]
            matrix[y][n-x-1] = matrix[x][y]
            matrix[x][y] = temp

    return matrix

matrix = [[1,2,3], [4,5,6,], [7,8,9]]
# print(rotate_matrix(matrix))

# def find_majority_element(a):
#     s = 0
#     pointer = 0
#     for i, element in enumerate(a):


# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6

# def merge_linkedlists(lists):
#     while True:
#         for i in range(len(lists)):

def search(array, target):
    return binary_search(array, len(array)-1, 0, target)
            
def binary_search(array, high, low, target):
    if high <= low:
        return -1
    else:
        mid = (high + low) // 2
        if array[mid] == target:
            return mid  
        else:
            if array[low] <= array[mid]:
                if target >= array[low] and target <= array[mid]:
                    return binary_search(array, mid-1, low, target)
                else:
                    return binary_search(array, high, mid+1, target)

            elif target >= array[mid] and target <= array[high]:
                return binary_search(array, high, mid+1, target)
            return binary_search(array, mid-1, low, target)

def modulo(num1, num2):
    if num2 == 0:
        return num1 
    else:
        return modulo(num2, num1 % num2)

def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    gcd = modulo(len(nums), k)
    n = 0
    for j in range(gcd): 
        i = len(nums) - 1 - j
        temp = nums[i]
        n = i

        while True:
            # nums[i], nums[i-1] = nums[i-1], nums[i]
            if n == j:
                break
            else:
                n = i - k
            print(nums)
            nums[i] = nums[n]
            i = n
        nums[len(nums)-1-j] = temp
    return nums
            
def schedule(schedule1, bound1, schedule2, bound2):
    # i = 0
    # j = 0
    # while i <= len(schedule1) and j <= len(schedule2):
    #     if schedule1[i][0]
    pass

def expand_center(s, l, r):
    left = l
    right = r
    while left >= 0 and right < len(s) and s[left] == s[right]:          
        left -= 1
        right += 1        
    return right - left - 1

def find_longest_pa(s):
    start = 0
    end = 0
    for i in range(len(s)):
        len1 = expand_center(s, i, i)
        len2 = expand_center(s, i, i + 1)

        length = max(len1, len2)
        if length > end - start:
            end = i + length // 2
            start = i - (length - 1) // 2
            print(i, length)
    return s[start:end+1]


def sum_linkedlists(ll1,ll2):
    pointer_1 = ll1.head
    pointer_2 = ll2.head
    curr = None
    carry = 0
    while pointer_1 and pointer_2:
        curr.val = (pointer_1 + pointer_2 + carry) % 10
        carry = (pointer_1 + pointer_2) // 10
        pointer_2 = pointer_2.next
        pointer_1 = pointer_1.next
        curr = curr.next

    if pointer_1:
        curr.value = (pointer_1.val + carry) % 10
    elif pointer_2:
        curr.value = (pointer_2.val + carry) % 10



if __name__ == "__main__":
    # print(rotate_array([1,2,3,4,5,6,7,8], 3))
    # print(binary_search([1,2,3,4,5,6], 6, 0, 0))
    # print(search([4,5,6,7,0,1,2], 3))
    # print(rotate([1,2,3,4,5], 3))
    # val = 5
    # checker = 0
    # checker |= 1 << val
    # val = 2
    # checker |= 1 << val

    # print(checker)
    # print(ord('a'))
    print(find_longest_pa('cbbd'))


