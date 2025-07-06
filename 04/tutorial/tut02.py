def solution(n: int) -> int:
    if n == 0:
        return 1
    if n < 0:
        return 0
    return solution(n - 1) + solution(n - 2)