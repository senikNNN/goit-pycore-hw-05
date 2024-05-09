from typing import Callable

def caching_fibonacci() -> Callable[[int], int]:
    cache = dict()
    
    def fibonacci(n: int) -> int:
        if n < 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    
    return fibonacci


count_fibonacci = caching_fibonacci()

print(count_fibonacci(10))
print(count_fibonacci(15))