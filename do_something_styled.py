#!/usr/bin/env python3
import math


def do_something(size, out_list):
    """Perform a CPU-heavy operation and append results to a shared list."""
    for i in range(size):
        # simulate CPU-bound work
        result = (math.sqrt(i)) ** 2
        out_list.append(result)
