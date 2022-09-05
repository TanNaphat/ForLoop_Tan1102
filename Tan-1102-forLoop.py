#Code 1
for i in range(0, 10, 2):
    print(i)
print("Goodbye!")

#Code 2
print("Hello!")
for i in range(10, 0, -2):
    print(i)

#Code 3
end = 6
data = 0
counter = 1
for i in range(end):
    data += counter
    counter += 1
print(data)