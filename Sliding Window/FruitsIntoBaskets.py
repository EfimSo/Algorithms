# given an array of chars representing fruits (eg. ['A', 'B', 'C', 'A', 'C'])
# find the greatest continuous subarray with at most two types of fruit
# (baskets can hold only two fruit types but any number of fruit)
# same as longest substring with at most k distinct chars for 2 chars

def findFruitBasket(fruits: list[str]):
    window_start, max_len = 0, 0
    fruit_freq = dict() # for keeping the number of unique fruits in basket

    for window_end in range(len(fruits)):
        # grow window by adding fruit
        right_fruit = fruits[window_end]
        if right_fruit not in fruit_freq:
            fruit_freq[right_fruit] = 0
        fruit_freq[right_fruit] += 1

        # shrink window until at most 2 unique fruits
        while len(fruit_freq) > 2:
            left_fruit = fruits[window_start]
            fruit_freq[left_fruit] -= 1
            if fruit_freq[left_fruit] == 0:
                del fruit_freq[left_fruit]
            window_start += 1
        
        max_len = max(max_len, window_end - window_start + 1)

    return max_len


fruit1=['A', 'B', 'C', 'A', 'C']
print(findFruitBasket(fruit1)) # should be 3

fruit2 = ['A', 'B', 'C', 'B', 'B', 'C']
print(findFruitBasket(fruit2)) # should be 5
