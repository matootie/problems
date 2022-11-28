"""Problem 2225. Find Players With Zero or One Losses
"""

from typing import List, Set


def solution(matches: List[List[int]]) -> List[List[int]]:

    winners: Set[int] = set()
    losers: Set[int] = set()
    invalid: Set[int] = set()

    for match in matches:
        winner, loser = match
        if winner not in losers and winner not in invalid:
            winners.add(winner)
        if loser in losers:
            losers.remove(loser)
            invalid.add(loser)
        elif loser not in invalid:
            losers.add(loser)
        if loser in winners:
            winners.remove(loser)

    return [sorted(list(winners)), sorted(list(losers))]
