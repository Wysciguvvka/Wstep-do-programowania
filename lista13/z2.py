nums = list(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(51)))
num = 5
# print(any(filter(lambda x: x == num, nums)))
print(f"{num} jest wielokrotnością 3 lub 5 w zakresie od 0 do 50") if num in nums else print(
    f"{num} nie jest wielokrotnością 3 lub 5 w zakresie od 0 do 50")
# print(nums)
print(', '.join([str(n) for n in nums]))
