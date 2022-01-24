def distributeCandies(candyType):
    no_of_acceptable = len(candyType)//2
    unique_candies = len(set(candyType))
    if unique_candies <= no_of_acceptable:
        return unique_candies
    else:
        if(unique_candies >= no_of_acceptable):
            return no_of_acceptable


distributeCandies([1, 1, 2, 2, 3, 3])
