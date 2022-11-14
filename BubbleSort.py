

def bubbleSort(nums):

    # 遍历 len(nums)-1 次
    for i in range(len(nums) - 1): 

        # 已排好序的部分不用再次遍历
        for j in range(len(nums) - i - 1): 

            if nums[j] > nums[j+1]:
                
                # Python 交换两个数不用中间变量
                nums[j], nums[j+1] = nums[j+1], nums[j] 
                
    return nums