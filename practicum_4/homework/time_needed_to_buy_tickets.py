from typing import Any

import yaml
import numpy as np


def time_taken(tickets: list[int], k: int) -> int:
    seconds_elapsed = 0

    iteration = 0

    while tickets[k]:
        index = iteration % len(tickets)
        if tickets[index]:
            tickets[index] -= 1
            seconds_elapsed += 1
        iteration += 1
        
    return seconds_elapsed


if __name__ == "__main__":
    # Let's solve Time Needed to Buy Tickets problem from leetcode.com:
    # https://leetcode.com/problems/time-needed-to-buy-tickets/
    with open("spbu-fundamentals-of-algorithms/practicum_4/time_needed_to_buy_tickets_cases.yaml", "r") as f:
        cases = yaml.safe_load(f)
    for c in cases:
        res = time_taken(tickets=c["input"]["tickets"], k=c["input"]["k"])
        print(f"Input: {c['input']}. Output: {res}. Expected output: {c['output']}")
