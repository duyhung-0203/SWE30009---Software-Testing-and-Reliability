def split_and_sort(nums):
    # check if input list length is less than or equal to 20
    if len(nums) > 20:
        return "Error: Input list should not contain more than 20 integers."

    # check if 0 is in the input list
    if 0 in nums:
        return "Error: The number 0 is not a valid input."

    # filter odd and even numbers into two separate lists
    odd_nums = [num for num in nums if num % 2 == 1]
    even_nums = [num for num in nums if num % 2 == 0]

    # remove duplicates and sort
    odd_nums = sorted(set(odd_nums))  # Old programming: odd_nums = sorted(odd_nums)
    even_nums = sorted(set(even_nums))  # Old programming: even_nums = sorted(even_nums)

    return odd_nums, even_nums

nums = [2, 3, 0]
result = split_and_sort(nums)  # Old programming: odd_nums, even_nums = split_and_sort(nums)

if isinstance(result, str):  # Check if the result is an error message (a string)
    print(result)
else:
    odd_nums, even_nums = result  # Assign variables if no error
    print("Odd numbers:", odd_nums)
    print("Even numbers:", even_nums)
