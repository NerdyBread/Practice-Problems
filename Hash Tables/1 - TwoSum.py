def twoSum(self, nums: list, target: int) -> list:
	checked = dict()
	for i, n in enumerate(nums):
		complement = target - n
		if complement in checked.keys():
			return [i, checked[complement]]
		checked[n] = i