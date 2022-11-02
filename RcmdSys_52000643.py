import math 

myPathRoot = 'matrix.txt'

f = open(myPathRoot, "r")
f.readline()

matrix = []

for line in f:
  row = [int(i) for i in line.split(' ')]
  matrix.append(row)

matrix

def centerizeRow(row):
  sum = 0
  count = 0

  for i in row:
    if(i != 0): count += 1
    sum += i

  mean = sum / count
  return [i - mean if i != 0 else 0 for i in row ]

def sim(selectedRow, ui):
  #dot product
  prod = sum([x*y for x,y in zip(selectedRow, ui)])

  #magnitude product: tich do. dai`
  a = sum([i**2 for i in selectedRow])
  b = sum([i**2 for i in ui])

  return prod/(math.sqrt(a)*math.sqrt(b))

"""Sinh viên viết chương hàm predictRating(m, u, i, n) trả về số thực là giá trị rating dự đoán của user u cho film i với số lượng user tham khảo là n trên ma trận rating m theo chiến lược Collaborative Filtering. Nếu m[u, i] là giá trị đã tồn tại thì trả về giá trị đó, không cần dự đoán.
Sinh viên viết hàm main để đọc ma trận lên từ tập tin matrix.txt. Gọi thực thi hàm predictRating() để tính ra vài giá trị rating ví dụ, trong đó n = 4, giá trị trung bình dựa trên Pearson Correlation Coefficient.
"""

def predictRating(m, u, i, n):
  #m: matrix
  #u: user -> rows
  #i: item - film -> cols
  #n = 4 -> 4 most similar user

  if(m[u-1][i-1] != 0): return m[u-1][i-1]

  ###step 1: find centerize each row of matrix by subtract mean row
  new_matrix = [centerizeRow(row) for row in m]

  ###step 2: similarities (selected user|row, ui):
  selectedRow = new_matrix[u-1]
  sims = [sim(selectedRow, ui) for ui in new_matrix]

  ###step 3: find n most similar
  #dict: {user: cos}
  myDict = {user+1: round(cos,2) for user,cos in enumerate(sims)}
  #eliminate user himself
  del myDict[u]

  #desc sort because the greater cosine the more similar
  sortedDict = sorted(myDict.items(), key = lambda v: v[1], reverse=True)

  ###step 4: weighted mean
  a = 0
  b = 0

  for k in range(n):
    store_u = sortedDict[k][0]

    a += m[store_u-1][i-1] * sortedDict[k][1] #origin rating * sim
    b += sortedDict[k][1]

  return round(a/b, 2)

print('user 3 will rate film 3: ', predictRating(matrix, 3, 3, 4)) #(m, u/row, i/col, n)
print('user 4 will rate film 3: ', predictRating(matrix, 4, 3, 4)) #(m, u/row, i/col, n)
print('user 5 will rate film 3: ', predictRating(matrix, 5, 3, 4)) #(m, u/row, i/col, n)
print('user 6 will rate film 3: ', predictRating(matrix, 6, 3, 4)) #(m, u/row, i/col, n)
print('user 7 will rate film 3: ', predictRating(matrix, 7, 3, 4)) #(m, u/row, i/col, n)
print('user 8 will rate film 3: ', predictRating(matrix, 8, 3, 4)) #(m, u/row, i/col, n)