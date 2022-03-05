def normalize(numbers):
    dist = sum(i ** 2 for i in numbers) ** 0.5
    return [x / dist for x in numbers]


print(' '.join(["%.5f" % x for x in normalize((2.2, 5.6, 4.3, 3.0, 0.5))]))
print('-----')
for n in normalize((2.2, 5.6, 4.3, 3.0, 0.5)):
    print(f"{n:5f}")
