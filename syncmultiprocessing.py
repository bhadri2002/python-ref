"""
basically process doesn't share value 
using array and value we can done memory sharing
"""

import multiprocessing
from unittest import result


def sqar(mylist, result, sqrt_sum):

    for idx, num in enumerate(mylist):
        result[idx] = num * num
    sqrt_sum.value = sum(result)
    print(f"result in the procssor {result[:]}")
    print(f"sum of the product value {sqrt_sum.value}")


if __name__ == "__main__":
    mylist = [1, 2, 3, 4]
    result = multiprocessing.Array("i", 4)
    sqrt_sum = multiprocessing.Value("i")
    p1 = multiprocessing.Process(target=sqar, args=(mylist,result,sqrt_sum))
    p1.start()
    p1.join()
    print(f"main process result {result[:]}")
    print(f"sum of the value in main {sqrt_sum.value}")
