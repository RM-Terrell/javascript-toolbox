# https://www.hackerrank.com/challenges/compare-the-triplets/problem
def compareTriplets(alice, bob):
    """
    :param [int] alice:
    :param [int] bob:
    """
    alice_score = 0
    bob_score = 0
    assert len(alice) == 3
    assert len(bob) == 3
    for idx, score in enumerate(alice):
        if alice[idx] == bob[idx]:
            pass
        elif alice[idx] > bob[idx]:
            alice_score += 1
        else:
            bob_score += 1

    return [alice_score, bob_score]


if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)
