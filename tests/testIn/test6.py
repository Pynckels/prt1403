import time

def sum_integers():
    total = 0
    for i in range(1, 10**7):
        total += i
    return total

start_time = time.time()
result = sum_integers()
end_time = time.time()

print(f"Python: The sum is {result}")
print(f"Python: Time taken = {end_time - start_time} seconds")
