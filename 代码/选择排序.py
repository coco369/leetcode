"""
思路: 将需排列的数据看成两部分，第一部分为已排序序列，第二部分为未排序序列
已排序序列默认有第一个元素，未排序序列为第二个元素到末尾的元素
通过两次for循环，依次将已排序序列的元素与未排序队列中的元素进行比较，如果已排序序列的元素大于未排序序列的元素，则交换两个元素的位置
"""
old_list = [4, 2, 3, 6, 5]


def sort_list(old_list):
    print('排序前', old_list)
    for i in range(len(old_list)):
        for j in range(i+1, len(old_list)):
            if old_list[i] > old_list[j]:
                old_list[i], old_list[j] = old_list[j], old_list[i]
                print(f'第{i+1}排序中', old_list)
    print('排序后:', old_list)

sort_list(old_list)

