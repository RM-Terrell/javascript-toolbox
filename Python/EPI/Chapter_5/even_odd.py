from typing import List

def even_odd_mutation(input_array: List[int]):
    """
    Function to reorder an array / list, with even elements first and odd elements second.
    """
    next_even = 0
    list_end = len(input_array) - 1
    odd_count = 0
    while (next_even < list_end) and ((odd_count + next_even) < len(input_array)):
        if input_array[next_even] % 2 == 0:
            next_even += 1
        else:
            input_list[next_even], input_list[list_end] = input_list[list_end], input_list[next_even]
            odd_count += 1


if __name__ == "__main__":
    input_list = [2,4,6,8,7,7,7,7]
    even_odd_mutation(input_list)
    print(input_list)
