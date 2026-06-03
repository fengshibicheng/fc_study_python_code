def merge_sort(arr):

    # 返回数组长度为0或者1的状态
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left_sorted = merge_sort(left_arr)
    right_sorted = merge_sort(right_arr)

    return merge(left_sorted, right_sorted) # 这是一个注释

def merge(left, right):

    merge = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merge.append(left[i])
            i += 1
        else:
            merge.append(right[j])
            j += 1

    merge.extend(left[i:])
    merge.extend(right[j:])

    return merge

# 测试数据
arr = [12, 15, 30, 10, 9, 25, 33, 40, 1]
print('原始的数组为:', arr)
sort_arr = merge_sort(arr)
print('排序后的数组为:', sort_arr)






