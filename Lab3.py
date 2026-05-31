
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
          








