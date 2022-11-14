


def countingSort(nums):

    # 桶的个数
    bucket = [0] * (max(nums) + 1) 

    # 将元素值作为键值存储在桶中，记录其出现的次数
    for num in nums:  

        bucket[num] += 1

    # nums 的索引
    i = 0  

    for j in range(len(bucket)):

        while bucket[j] > 0:

            nums[i] = j

            bucket[j] -= 1

            i += 1
            
    return nums