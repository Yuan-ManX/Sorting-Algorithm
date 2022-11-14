

def insertionSort(nums):

    # 遍历 len(nums)-1 次
    for i in range(len(nums) - 1):  

        # curNum 保存当前待插入的数
        curNum, preIndex = nums[i+1], i  

        # 将比 curNum 大的元素向后移动
        while preIndex >= 0 and curNum < nums[preIndex]: 

            nums[preIndex + 1] = nums[preIndex]

            preIndex -= 1

        # 待插入的数的正确位置  
        nums[preIndex + 1] = curNum   
        
    return nums