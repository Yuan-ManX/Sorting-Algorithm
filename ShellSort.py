


def shellSort(nums):

    lens = len(nums)

    gap = 1  

    while gap < lens // 3:

        # 动态定义间隔序列
        gap = gap * 3 + 1  

    while gap > 0:

        for i in range(gap, lens):

            # curNum 保存当前待插入的数
            curNum, preIndex = nums[i], i - gap 
            
            while preIndex >= 0 and curNum < nums[preIndex]:

                # 将比 curNum 大的元素向后移动
                nums[preIndex + gap] = nums[preIndex] 

                preIndex -= gap

            # 待插入的数的正确位置
            nums[preIndex + gap] = curNum 

        # 下一个动态间隔
        gap //= 3  
        
    return nums