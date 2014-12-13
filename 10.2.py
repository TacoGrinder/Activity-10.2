__author__ = 'Sean'

#1
m = [1, 6, 4, 3, 5, 8, 9, 10, 2, 7]

#2
for j in range(len(m)):
    for i in range(len(m)-1):
        if m[i] > m[i+1]:
            a = m[i]
            m[i] = m[i+1]
            m[i+1] = a
print(m)