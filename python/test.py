numbers = [-2,-2,-2,0,2]
target_list = []
numbers_new = {}
result = []
for x in range(len(numbers)):
    numbers_new[numbers[x]] = x
for x in numbers:
    if not(x in target_list):
        target_list.append(x)
        target = x
        anumbers_new = numbers_new
        anumbers = numbers
        del anumbers_new[x]
        del anumbers[x]
        for x in anumbers:
            searched = target - x
            if searched in anumbers_new:
                result.append(numbers_new[searched] + 1)
result.sort()
print(result)