def f(x):
    return 2 ** x + x - 5

def solve_bisection(low, high, epsilon=1e-6):
    while (high - low) > epsilon:
        mid = (low + high) / 2
        if f(mid) == 0:
            return mid
        elif f(low) * f(mid) < 0:
            high = mid
        else:
            low = mid
    return (low + high) / 2

# Задаем начальный диапазон для поиска
low = 0
high = 2

# Решаем уравнение
root = solve_bisection(low, high)
print(f"Приближенное решение: x ≈ {root:.6f}")
