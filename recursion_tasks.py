# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# print(factorial(5))
#
# def summation(n):
#     if n == 1:
#         return 1
#     else:
#         return n + summation(n-1)
# print(summation(5))

def sum_odd(lis):
    if not lis:
        return 0
    else:
        for i in range(len(lis)):
            if lis[i] % 2 != 0:
                return lis[i] + sum_odd(lis[i+1:])
    return


print(sum_odd([1,2,4,6,8]))