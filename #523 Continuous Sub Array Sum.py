def checkSubarraySum(nums, k):
    hashMap = {0: -1}
    sum=0

    for i in range(len(nums)):
        sum+=nums[i]
        if(k!=0):
            sum=sum%k
        if(sum in hashMap.keys()):
            print("HERE")
            if(i - hashMap[sum] >=2):
                print("true")
                return True
            
        else:
            hashMap[sum]=i
            print(hashMap)

    return False


checkSubarraySum([23, 2, 4, 6, 7],6)

