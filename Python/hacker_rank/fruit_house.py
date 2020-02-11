import math
import os
import random
import re
import sys


# https://www.hackerrank.com/challenges/apple-and-orange/problem
def countApplesAndOranges(house_left_bound, house_right_bound, apple_tree, orange_tree, apples, oranges):
    apples_fallen_on_house = 0
    oranges_fallen_on_house = 0
    for apple in apples:
        fall_location = apple_tree + apple
        if fall_location >= house_left_bound and fall_location <= house_right_bound:
            apples_fallen_on_house += 1
    # Alternate crazy list comp solution
    # print(sum([1 for x in apples if (x + a) >= s and (x + a) <= t]))
    for orange in oranges:
        fall_location = orange_tree + orange
        if fall_location >= house_left_bound and fall_location <= house_right_bound:
            oranges_fallen_on_house += 1
    # Alternate crazy list comp solution
    # print(sum([1 for x in oranges if (x + b) >= s and (x + b) <= t]))

    return [apples_fallen_on_house, oranges_fallen_on_house]


if __name__ == '__main__':
    st = input().split()

    house_left_bound = int(st[0])

    house_right_bound = int(st[1])

    ab = input().split()

    apple_tree = int(ab[0])

    orange_tree = int(ab[1])

    mn = input().split()

    # these throw away variables are here cause for some reason the test cases input them
    throw_away_m = int(mn[0])
    throw_away_n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    fallen_fruit = countApplesAndOranges(house_left_bound, house_right_bound, apple_tree, orange_tree, apples, oranges)
    for fruit in fallen_fruit:
        print(fruit)
