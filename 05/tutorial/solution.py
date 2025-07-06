def solution(nums):
	n = len(nums)
	if n == 0 or n == 1:
		return False
	if 2 not in nums:
		return False
	if nums[0] == 2 and nums[n-1] == 2:
		return True
	for i in range(n):
		if nums[i] == 2:
			if nums[i-1] == 2 or nums[i+1] == 2:
				return True
	return False
