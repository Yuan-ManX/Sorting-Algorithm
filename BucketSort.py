


def bucketSort(nums, defaultBucketSize = 5):

    maxVal, minVal = max(nums), min(nums)

    # 如果没有指定桶的大小，则默认为5
    bucketSize = defaultBucketSize 

    # 数据分为 bucketCount 组
    bucketCount = (maxVal - minVal) // bucketSize + 1  

    # 二维桶
    buckets = []  

    for i in range(bucketCount):

        buckets.append([])

    # 利用函数映射将各个数据放入对应的桶中
    for num in nums:

        buckets[(num - minVal) // bucketSize].append(num)

    # 清空 nums
    nums.clear()  

    # 对每一个二维桶中的元素进行排序
    for bucket in buckets:

        # 假设使用插入排序
        insertionSort(bucket)  

        # 将排序好的桶依次放入到 nums 中
        nums.extend(bucket)    
        
    return nums