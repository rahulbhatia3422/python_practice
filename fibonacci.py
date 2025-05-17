def fibonacci_series(n):
    """Return a list containing the Fibonacci series up to n terms."""
    if n <= 0:
        return []
    series = [0]
    if n == 1:
        return series
    series.append(1)
    for i in range(2, n):
        series.append(series[-1] + series[-2])
    return series