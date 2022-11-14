


def mergeSort(nums):

    # 归并过程
    def merge(left, right):

        # 保存归并后的结果
        result = [] 

        i = j = 0

        while i < len(left) and j < len(right):

            if left[i] <= right[j]:

                result.append(left[i])

                i += 1

            else:

                result.append(right[j])

                j += 1

        # 剩余的元素直接添加到末尾
        result = result + left[i:] + right[j:] 

        return result

    # 递归过程
    if len(nums) <= 1:

        return nums

    mid = len(nums) // 2

    left = mergeSort(nums[:mid])

    right = mergeSort(nums[mid:])
    
    return merge(left, right)