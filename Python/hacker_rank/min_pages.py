import os

# https://www.hackerrank.com/challenges/drawing-book/problem
def pageCount(n_pages, target_page):
    # int division for whole pages
    total_possible_turns = n_pages // 2
    forward_page_turns = target_page // 2
    backwards_turns = total_possible_turns - forward_page_turns

    return min(backwards_turns, forward_page_turns)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
