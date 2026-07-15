
from operator import le

from numpy import append

# 1
List1 = [1,2,3,4,5,6,7,8,9,10]
print(List1[0])
print(List1[-1])
print(f"Length of the list1: {len(List1)}\n")

# 2
List2 = []
List2.append(0)
List2.append(2)
List2.append(4)
List2.append(6)
List2.append(8)
List2.append(10)
List2.append(12)
List2.append(14)
List2.append(16)
List2.append(18)
List2.append(20)
print(List2)
print(f"Length of the list: {len(List2)}\n")


# 3
List3 = [1,2,3,4,5,6,7,8,9,10]
print(f"Average of List3: {sum(List3)/len(List3)}")

total = 0
for num in List3:
    total += num
print(f"Sum of List3: {total} ")

min = List3[0]
for num in List3:
    if num < min:
        min = num
print(f"Min of List3: {min}") 

max = List3[0]
for num in List3:
    if num> max:
        max = num
print(f"Max of list3 : {max}\n")



# 4
List4 = [1,2,3,4,5,6,7,8,9,10]
Even  = 0
Odd = 0
for num in List4:
    if num%2 == 0:
        Even = Even + 1
    else:
        Odd = Odd + 1
print(f"Numver of Even numbers: {Even}")
print(f"Number of Odd numbers: {Odd}\n")



# 5
List5 = [1,2,3,4,5,6]
Even_list = []
for num in List5:
    if num%2 == 0:
        Even_list.append(num)
print(Even_list)
print()


# 6
List6 =[1,2,3,4,5,6,7,8,9,10]
num = int(input("Enter the number:"))
if num in List6:
    print(f"{num} is in the list and index is : {List6.index(num)}")
else:
    print(f"{num} isn't in the list and no index found \n ")
          

# 7
numbers = [1, 2, 2, 3, 1, 1]

frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

for key, value in frequency.items():
    print(key, "->", value)



# 8
numbers = [1, 2, 2, 3, 3, 4]

unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)

print(unique)



# 9
A = [1, 2, 3]
B = [4, 5, 6]

# (a) append()
C = A.copy()
C.append(B)
print("append():", C)

# (b) extend()
D = A.copy()
D.extend(B)
print("extend():", D)

# (c) + operator
E = A + B
print("+ operator:", E)



# 10
numbers = [10, 20, 30, 40, 50]

# (a) reverse()
A = numbers.copy()
A.reverse()
print(A)

# (b) slicing
print(numbers[::-1])



# 11
numbers = [5, 2, 9, 1, 6]

numbers.sort()
print("Ascending:", numbers)

numbers.sort(reverse=True)
print("Descending:", numbers)



# 12
students = ["Ali", "Sara", "John"]

students.append("Emma")
students.insert(1, "David")
students.remove("Sara")
students.sort()

print(students)



# 13
numbers = [10, 20, 30]

numbers.append(40)
print("append:", numbers)

numbers.insert(1, 15)
print("insert:", numbers)

numbers.remove(20)
print("remove:", numbers)

removed = numbers.pop()
print("pop:", numbers)
print("Removed:", removed)

copy_list = numbers.copy()
print("copy:", copy_list)

numbers.clear()
print("clear:", numbers)



# 14 
numbers = [10,20,30,40,50,60,70]

print("First three:", numbers[:3])
print("Last three:", numbers[-3:])
print("Every second:", numbers[::2])
print("Reverse:", numbers[::-1])



# 15
numbers = list(map(int, input("Enter numbers: ").split()))

print("Sum =", sum(numbers))
print("Average =", sum(numbers)/len(numbers))
print("Largest =", max(numbers))
print("Smallest =", min(numbers))


# 16
numbers = [x for x in range(1, 21)]
print(numbers)

even = [x for x in range(1, 21) if x % 2 == 0]
print(even)

odd = [x for x in range(1, 21) if x % 2 != 0]
print(odd)

squares = [x**2 for x in range(1, 11)]
print(squares)




# 17
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print("Matrix:")
for row in matrix:
    print(row)

print("First row:", matrix[0])

print("Last column:")
for row in matrix:
    print(row[-1])

total = 0
for row in matrix:
    total += sum(row)

print("Sum =", total)




# 18
matrix = []

print("Enter 3 rows:")

for i in range(3):
    row = list(map(int, input().split()))
    matrix.append(row)

print("Row sums:")
for row in matrix:
    print(sum(row))

print("Column sums:")
for j in range(3):
    total = 0
    for i in range(3):
        total += matrix[i][j]
    print(total)

total = 0
for row in matrix:
    total += sum(row)

print("Total sum =", total)




# 19
marks = []

print("Enter marks of 10 students:")

for i in range(10):
    marks.append(int(input()))

average = sum(marks)/len(marks)

print("Highest =", max(marks))
print("Lowest =", min(marks))
print("Average =", average)

count = 0
for mark in marks:
    if mark > average:
        count += 1

print("Above average =", count)






# 20
runs = []

print("Enter runs for 15 matches:")

for i in range(15):
    runs.append(int(input()))

print("Total runs =", sum(runs))
print("Average =", sum(runs)/len(runs))
print("Highest =", max(runs))
print("Lowest =", min(runs))

half = 0
century = 0

for score in runs:
    if score >= 50:
        half += 1
    if score >= 100:
        century += 1

print("Half-centuries =", half)
print("Centuries =", century)





#  Bonus Challenge Problems

# 1
numbers = [10, 20, 30, 50, 40]
numbers.sort()
print("Second largest =", numbers[-2])


# 2
numbers = [1,2,3,4,5]
numbers = [numbers[-1]] + numbers[:-1]
print(numbers)



# 3
A = [1,3,5]
B = [2,4,6]

merged = A + B
merged.sort()
print(merged)





# 4
table = []

for i in range(1, 6):
    row = []
    for j in range(1, 6):
        row.append(i * j)
    table.append(row)

for row in table:
    print(row)




# 5
primes = [
    n for n in range(2, 101)
    if all(n % i != 0 for i in range(2, int(n**0.5) + 1))
]
print(primes)

