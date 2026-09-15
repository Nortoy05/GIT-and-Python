print("==============================")
# in JAVA variables is a name storage location!
# in Python, variables is named reference!

count = 100
count_type = type(count)
print(f"the count: {count} and type: {count_type}")

result1 = count.bit_count() #method
result2 = count.numerator #state
print(result1, result2)