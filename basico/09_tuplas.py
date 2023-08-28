#inmutables
numbers = (1,2,3,4,5,4)
str = ('hector', 'david', 'gasca')

print(f"{numbers} del tipo {type(numbers)} y {str} del tipo {type(str)}")

print(numbers[0])
print(numbers[-1])

#print(numbers.count())
print(f"cuantas?: {numbers.count(4)}")

print(f"en donde?: {numbers.index(4)}")

#conversion de tupla a list
listNum = list(numbers)
listNum.append(6)
print(numbers)
print(listNum)

listTuple = tuple(listNum)
print(listTuple)
print(type(listTuple))

a = {1,2,2}
b = {2,3}
print(a | b)