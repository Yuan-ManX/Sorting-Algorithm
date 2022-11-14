

# 这种写法的平均空间复杂度为 O(nlogn)
def quickSort(nums):  

    if len(nums) <= 1:

        return nums

    # 基准值
    pivot = nums[0]  

    left = [nums[i] for i in range(1, len(nums)) if nums[i] < pivot] 

    right = [nums[i] for i in range(1, len(nums)) if nums[i] >= pivot]

    return quickSort(left) + [pivot] + quickSort(right)


'''
@param nums: 待排序数组
@param left: 数组上界
@param right: 数组下界
'''

# 这种写法的平均空间复杂度为 O(logn) 
def quickSort2(nums, left, right):  

    # 分区操作
    def partition(nums, left, right):

        # 基准值
        pivot = nums[left]  

        while left < right:

            while left < right and nums[right] >= pivot:

                right -= 1

            # 比基准小的交换到前面
            nums[left] = nums[right]  

            while left < right and nums[left] <= pivot:

                left += 1

            # 比基准大交换到后面
            nums[right] = nums[left]  

        # 基准值的正确位置，也可以为 nums[right] = pivot
        nums[left] = pivot 

        # 返回基准值的索引，也可以为 return right
        return left  

    # 递归操作
    if left < right:

        pivotIndex = partition(nums, left, right)

        # 左序列
        quickSort2(nums, left, pivotIndex - 1)  

        # 右序列
        quickSort2(nums, pivotIndex + 1, right) 
        
    return nums