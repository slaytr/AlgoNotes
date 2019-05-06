import math

# Problem 1 - Hello World
print("Problem 1:", sum(x for x in range(1000) if x % 5 == 0 or x % 3 == 0))

# Problem 2 - Iterative Solution 
def fib():
    first, second = 0, 1
    even_sum = 0
    for _ in range(0, 100):
        first, second = second, first + second
        if first % 2 == 0:
            even_sum += first
        if first > 4000000:
            break
    return even_sum
#print(fib()) # ans 4613732

# Problem 3 - Largest Prime Factor
def prime(n): 
    primes = []
    while n % 2 == 0: 
        n /= 2
    for i in range(3, int(math.sqrt(n))+1, 2): 
        while n % i == 0: 
            primes.append(i)
            n /= i 
    return max(primes) if primes else n
#print(prime(600851475143))

# Problem 4 - Largest Palindrome Product
def find_palin():
    largest = 0
    for i in range(900,1000):
        for j in range(900, 1000):
            temp = str(i*j)
            if temp == temp[::-1] and int(temp) > largest:
                largest = int(temp)
    return largest
#print(find_palin())

# Problem 5 - Smallest Multiple
def smallest_multiple():
    stack = []
    divs = []
    count = 2520

    for i in range(10, 21):
        divs.append(i)
        
    while True:
        count += 2520 # must be multiple of 2520 if evenly divisible by range(1, 11)
        for number in divs:
            if count % number == 0:
                stack.append(number)
        if stack == divs:
            break
        stack = []
    return count
#print(smallest_multiple())

# Problem 6 - Sum Square Difference
print("Problem 6:", sum(x for x in range(1, 101))**2-sum(x**2 for x in range(1, 101)))

# Problem 7 - 10001st prime
def another_prime():
    count, number = 0, 2
    while count < 10000:
        number += 1
        if all(number % i for i in range(3, int(math.sqrt(number)) + 1, 2)) == True and number % 2 != 0:
            count += 1
    return number
print("Problem 7:", another_prime())

# Problem 77
def last_prime(n):
    # Generate List of Primes
    primes = [2]
    count, number = 0, 2
    while count < 30:
        number += 1
        if all(number % i for i in range(3, int(math.sqrt(number)) + 1, 2)) == True and number % 2 != 0:
            count += 1
            primes.append(number)
    
    # Find Solution
    value = 0 
    while True:
        ways = [1] + [0] * value # List of variations 
        for prime in primes: 
            for i in range(prime, value+1):
                ways[i] += ways[i-prime] 
        if ways[value] > n: # Change 5 to 5000
            break    
        value += 1
    return value
print("Problem 77:", last_prime(5))