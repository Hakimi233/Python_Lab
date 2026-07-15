# list1 = [1,2,3]
# list2 = [4,5,6]
# list1.append(list2)


# Ma = [
#  [1 ,2 ,3] ,
#  [4 ,5 ,6] ,
#  [7 ,8 ,9]
#  ]
# #print(Ma[0][2])


# list = [x for x in range(1,11) if x % 2 == 0]
# print(list)

# list1 = [1,2,3,2,4,2]
# #print(list1[0])
# #print(list1.index(2))


# numbers = [10 ,20 ,30]
# for i in range (len( numbers ) ) :
#     print (i , numbers [ i ])

# # Enumerate ; retren index and value
# Name = ["Ali" , "Farzana" , "Mom"]
# for index, value in enumerate(Name) :
#     print(index, value)


# # taking input from the user
# list = []
# for i in range(6):
#     x = int(input("Enter the numbers: "))
#     list.append(x)
# print(list)


# 2 method 
#number = list(map(int, input("Enter numbers: ") .split()))
#print(number)


#List Comprehension
num = [ x*x for x in range(1, 100) if x % 2 ==0]
#print(num)


#Nested List Comprehension
Num = [[i*j for i in range(5)] for j in range(6)]
#print(Num)



# numbers = []
# for i in range (5) :
#     x = int( input () )
#     numbers . append ( x )
# print ( numbers )



numbers = [10 , 20 , 30 , 40 , 50]
print ( numbers [0])
print ( numbers [ -1])
print ( numbers [1:4])


list1 = [1 , 2 , 3]
list2 = [4 , 5]
list2 = list1.copy()
print(list2)
list1 . append ( list2 )
print ( list1 )
print()


# list = [1 , 2 , 3]
# list3 = sorted(list)
# print(list3)
# print()
# list.sort()
# print(list)



# numbers = [10 , 20 , 30 , 40]
# for i in range(len(numbers)):
#     print(i, numbers[i])

# numbers = [10 , 20 , 30]
# numbers . remove (7)
# print ( numbers )



numbers = [1 , 2 , 2 , 3 , 2]
print ( numbers . count (2) )
print ( numbers . index (2) )



matrix = [
[1 , 2 , 3] ,
[4 , 5 , 6]
]
for x in matrix:
    print(x)



matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

for row in matrix:
    for value in row:
        print(value)