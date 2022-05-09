def count_positives_sum_negatives(arr):
    if arr == []:
        return arr
    else:
        count_positives = 0
        sum_negatives = 0
        for i in arr:
            if i > 0:
                count_positives += 1
            if i < 0:
                sum_negatives += i
        return [count_positives, sum_negatives]
