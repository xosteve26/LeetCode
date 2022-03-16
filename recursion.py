# def rec(n):
#     if(n == 0):
#         return
#     print(n)
#     rec(n-1)
#     print(n)


# rec(5)


# def fact(i):
#     if(i == 1):
#         return 1
#     return i*fact(i-1)


# fact(5)

# def sumN(num):
#     dig = num % 10
#     num //= 10
#     if num == False:
#         return dig
#     return dig + sumN(num)


# sumN(314)


# def rev(num):
#     dig = num % 10  # 4 #1 #3
#     num //= 10  # 31 #3
#     if(num == False):
#         return str(dig)

#     return str(dig) + rev(num)


# def palindrome(num):
#     return num == int(rev(num))


# palindrome(12134)


# def c0(num, count):
#     dig = num % 10
#     num //= 10

#     if num == False:
#         return count

#     if(dig == 0):
#         return c0(num, count+1)
#     return c0(num, count)


# print(c0(1200900, 0))


# def sorting(arr, i):
#     if(i+1 == len(arr)):
#         return True

#     if(arr[i+1] < arr[i]):
#         return False

#     return sorting(arr, i+1)


# print(sorting([1, 2, 3, 4, 5], 0))


# def linsearch(arr, target, index):
#     res = []
#     if(index == len(arr)):
#         return res

#     if(arr[index] == target):
#         res.append(index)
#     belowans = linsearch(arr, target, index+1)

#     return res+belowans


# print(linsearch([6, 5, 8, 98, 98, 67], 98, 0))

# With variable in body
# def removea(string, index, astring):

#     if(index == len(string)):
#         return astring
#     if(string[index] != 'a'):
#         astring += string[index]

#     return removea(string, index+1, astring)


# print(removea('baccad', 0, ''))

# With variable in body
# def removea(string, index):
#     astring = ''
#     if(index == len(string)):
#         return astring

#     if(string[index] != 'a'):
#         astring += string[index]

#     rval = removea(string, index+1)
#     return astring+rval


# print(removea('baccad', 0))


# Processed & Unprocessed  For removing 'a' from Strings
# def removea(processed, unprocessed):
#     print(processed)
#     if(unprocessed == ''):
#         print("PROCESSED")
#         return processed

#     c = unprocessed[0]
#     if(c != 'a'):
#         return removea(processed+c, unprocessed[1:])
#     else:
#         return removea(processed, unprocessed[1:])


# print("answer", removea('', 'baccdah'))

# Processed & Unprocessed Trick For Strings


# def removea(unprocessed):

#     if(unprocessed == ''):
#         print("PROCESSED")
#         return ''

#     c = unprocessed[0]
#     if(c != 'a'):
#         return c+removea(unprocessed[1:])
#     else:
#         return removea(unprocessed[1:])


# print("answer", removea('baccdah'))


# Skip a string using recursion
# def skipString(unprocessed):
#     if(unprocessed == ''):
#         return ''
#     c = unprocessed[0]
#     if(unprocessed.startswith('app')):
#         if(unprocessed.startswith('apple')):
#             return c+skipString(unprocessed[1:])
#         else:
#             return skipString(unprocessed[3:])

#     return c+skipString(unprocessed[1:])


# print(skipString('stappartsapplewithapp'))

# Subset using recursion
#[a,    b,      c,      ab,     bc,     ca,     abc]
# def subset(processed, unprocessed):
#     if(unprocessed == ''):
#         print(processed)
#         return

#     ch = unprocessed[0]
#     subset(processed, unprocessed[1:])
#     subset(processed+ch, unprocessed[1:])


# subset('', 'abc')

# Subset with Array using recursion
# def subsetR(processed, unprocessed):
#     arr = []
#     if(unprocessed == ''):
#         arr.append(processed)
#         return arr
#     ch = unprocessed[0]
#     left = subsetR(processed+ch, unprocessed[1:])
#     right = subsetR(processed, unprocessed[1:])
#     return left+right


# print(subsetR('', 'abc')[:-1])

# Create Subset of array using iteration
# arr = [1, 2, 3]
# outer = [[]]
# for i in arr:
#     for j in range(len(outer)):
#         outer.append(outer[j]+[i])
#     print(outer)

# print(outer[1:])

# Permutations
# i/p = "abc"
# o/p = ["cba", "bca", "bac", "cab", "acb", "abc"]

# def permutation(processed, unprocessed, perms):

#     if(unprocessed == ''):
#         perms.append(processed)
#         return perms
#     for i in range(len(processed)+1):
#         permutation(processed[0:i]+unprocessed[0] + processed[i:], unprocessed[1:], perms)
#     return perms
# print(len(permutation('', 'abc', [])))


#Count number of permutations

# def permutation(processed, unprocessed, perms):

#     if(unprocessed == ''):
#         perms+=1
#         return perms
#     for i in range(len(processed)+1):
#         perms=permutation(processed[0:i]+unprocessed[0] + processed[i:], unprocessed[1:], perms)
#     return perms
# print(permutation('', 'abc', 0))


# def permutations(processed, unprocessed, perms):
#   if(len(unprocessed) == 0):
#     perms.append(processed)
#     return perms
#   l=[]
#   for i in range(len(processed)+1):
#     l.append(processed[0:i])
#     l.append(unprocessed[0])
#     l.append(processed[i:])
#     permutations(l, unprocessed[1:], perms)

#   return perms


# print(permutations('', [1, 2, 5], []))

# target=5
# res=[]
# for i in range(1,target+1):
#   res.append([i,target-i])

# print(res)

#Maze: Find Count
# def maze(r,c,count,target):
#   if r == target[0] or c == target[1]:
#     count+=1
#     return count

#   v1=maze(r+1,c,count,target)
#   v2=maze(r,c+1,count,target)
#   count=count+v1+v2
#   return count

# print(maze(1,1,0,(3,3)))

#Maze: Find Path
# def maze(processed,r,c,target,array):
#   if r == target[0] and c == target[1]:
#     array.append(processed)
#     return array
#   if(r<target[0]):
#     maze(processed+'D',r+1,c,target,array)
#   if(c<target[1]):
#     maze(processed+'R',r,c+1,target,array)
#   return array

# print(maze('',1,1,(3,3),[]))

# def mergeOverlappingIntervals(intervals):
#     intervals.sort()
#     first,end=0,0
#     arr=[]
#     i,j=0,0
#     print("intervals",intervals)
#     while i<=len(intervals)-1:
#       print(i)
#       if(i == len(intervals)-1):
#           print("IN IF")
#           arr.append(intervals[i])
#           break
#       if(intervals[i+1][0]>intervals[i][1]):

#         arr.append(intervals[i])
#         i+=1
#         j+=1
#         print(arr)
#         continue

#       first=intervals[i]
#       end=intervals[j][1]
#       print("FIRST < I",first,i)
#       while j<len(intervals)-1 and intervals[j+1][0]<=end:
#         end=max(first[1],intervals[j+1][1])
#         j+=1
#         print("J IS ",j)
#       arr.append([first[0],end])
#       print("ARR END",arr,j)
#       i=j+1
#       j+=1
#     return arr


# array = [
#     [20, 21],
#     [22, 23],
#     [0, 1],
#     [3, 4],
#     [23, 24],
#     [25, 27],
#     [5, 6],
#     [7, 19]
#   ]

# print(mergeOverlappingIntervals(array))

# def fourNumberSum(array, targetSum):
#   array.sort()
#   left = 0
#   right = len(array)-1
#   sum = 0
#   result = []
#   for i in range(len(array)):
#     for j in range(i+1, len(array)-1):
#       left = j+1
#       right = len(array)-1
#       while left>-1 and left < right:
#         sum = array[i]+array[j]+array[left]+array[right]
#         if(sum < targetSum):
#           left-=1
#         elif(sum > targetSum):
#           right -= 1
#         else:
#           if([array[i], array[j], array[left], array[right]] not in result):
#             result.append([array[i], array[j], array[left], array[right]])
#           left += 1
#           right -= 1
         
#   return result


# array = [1,0,-1,0,-2,2]

# print(fourNumberSum(array,0))

