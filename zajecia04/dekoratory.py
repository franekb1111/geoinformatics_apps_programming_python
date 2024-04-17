import time

def time_measure(unit):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            elapsed_time = time.time() - start_time
            
            if unit == 'microseconds':
                elapsed_time *= 1000000  # przeliczenie sekund na mikrosekundy
                print(f"Czas wykonania funkcji {func.__name__}: {elapsed_time} mikrosekund")
            else:
                print(f"Czas wykonania funkcji {func.__name__}: {elapsed_time} sekund")
            
            return result
        return wrapper
    return decorator


@time_measure('microseconds')
def funkcja_dodawanie(a,b):
    time.sleep(1)
    return a +b

@time_measure('seconds')
def funkcja_dodawanie_2(a,b):
    time.sleep(2)
    return a +b

print(funkcja_dodawanie(1,2))
print(funkcja_dodawanie_2(1,2))
