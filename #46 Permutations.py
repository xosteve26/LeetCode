def permute(nums):
    result = []
    if(len(nums) == 1):
        print("FIRST IF ", nums)
        return [nums.copy()]

    for i in range(len(nums)):
        print("I IS ", i)
        n = nums.pop(0)
        perms = permute(nums)
        print("PERMS", perms)

        for perm in perms:

            perm.append(n)
            print("IN FOR PERM AFTER APPEND IS", perm)
        result.extend(perms)
        print("RESULT ", result)
        nums.append(n)
        print("NUMS AFTER RESULT", nums)
    print("FINAL RESULT", result)

    return result


permute([1, 2, 3])
