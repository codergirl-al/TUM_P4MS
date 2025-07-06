from typing import List

def solution(lst: List[int]) -> bool:
	n = len(lst)
	for i in range(n):
		if lst[i] == 2:
			if n == 1:
				return False
			prev_idx = (i - 1) % n
			next_idx = (i + 1) % n
			if lst[prev_idx] != 2 and lst[next_idx] != 2:
				return False
	return True