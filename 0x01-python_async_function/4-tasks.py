#!/usr/bin/env python3
"""Tasks. Another version of wait_n from task 1"""

import asyncio

task_wait_random = __import__("3-tasks").tasks_wait_random


import asyncio
from typing import List


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawn task_wait_random n times with the specified max_delay.
    Return a list containing all delays in seconds
    """
    delays = []
    tasks = []
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays