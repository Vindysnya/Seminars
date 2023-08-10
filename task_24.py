lst = [1, 2, 58, 4, 5, 6, 7, 8]
res = max([(lst[i - 1] + lst[i] + lst[(i + 1) % len(lst)], i + 1)
          for i in range(len(lst))])
print(f' Макс. кол-во ягод {res[0]}, собрано для куста {res[1]}')
