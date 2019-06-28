# _*_ coding=utf-8 _*_


# 冒泡排序，时间复杂度O(n²)
def bubble_sort(num):
    """
    如果冒泡排序中的一次排序没有发生交换，则说明列表已经有序，可以直接结束算法
    :param num:
    :return:
    """
    for i in range(len(num) - 1):
        exchange = False
        print(num)
        for j in range(len(num) - 1 - i):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
                exchange = True
        if not exchange:
            return num
    return num


l = [33,11,12,1,2,3,4,5,22]
print(bubble_sort(l))
