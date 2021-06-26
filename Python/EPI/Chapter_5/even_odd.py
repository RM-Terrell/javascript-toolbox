from typing import List


def even_odd_mutation(input_list: List[int]):
    """
    Function to reorder an array / list, with even elements first and odd elements second.
    """
    next_even = 0
    next_odd = len(input_list) - 1

    while (next_even < next_odd):
        if input_list[next_even] % 2 == 0:
            next_even += 1
        else:
            input_list[next_even], input_list[next_odd] = input_list[next_odd], input_list[next_even]
            next_odd -= 1


if __name__ == "__main__":
    input_list = [2, 4, 6, 8, 7, 7, 7, 7]
    input_list_2 = [9, 4, 5, 2, 4, 13, 2]
    even_odd_mutation(input_list_2)
    print(input_list_2)
