


# LSD Radix Sort
def radixSort(nums):

    mod = 10

    div = 1

    # 最大数的位数决定了外循环多少次
    mostBit = len(str(max(nums)))  

    # 构造 mod 个空桶
    buckets = [[] for row in range(mod)] 

    while mostBit:

        # 将数据放入对应的桶中
        for num in nums:  

            buckets[num // div % mod].append(num)

        # nums 的索引
        i = 0  

        # 将数据收集起来
        for bucket in buckets:  

            while bucket:

                # 依次取出
                nums[i] = bucket.pop(0) 

                i += 1

        div *= 10

        mostBit -= 1
        
    return nums