def get_matrix(n, m, value):
    matrix = []
    #в цикле лучше всегда использовать после for (i, j, k) сначала прописал for n in range... не работало
    for i in range(n):
        matrix.append([])
        #в цикле лучше всегда использовать после for (i, j, k) сначала прописал for m in range... не работало
        for j in range(m):
            #это подсмотрел в интернете, потому что у меня не выводило m количество в подсписок
            matrix[i] = [value] * m
    return matrix
result_1 = get_matrix(2, 2, 10)
result_2 = get_matrix(3, 5, 42)
result_3 = get_matrix(4, 2, 13)
print(result_1)
print(result_2)
print(result_3)