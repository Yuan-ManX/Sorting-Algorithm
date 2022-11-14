

def selectionSort(nums):

    # 遍历 len(nums)-1 次
    for i in range(len(nums) - 1):  

        minIndex = i

        for j in range(i + 1, len(nums)):

            # 更新最小值索引
            if nums[j] < nums[minIndex]:  

                minIndex = j  

        # 把最小数交换到前面
        nums[i], nums[minIndex] = nums[minIndex], nums[i] 
        
    return nums