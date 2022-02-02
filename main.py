#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from functools import wraps


def running_time(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        elapsed_time = (end - start)
        res = time.strftime("%H Hours, %M minutes %S seconds ",
                            time.gmtime(elapsed_time))
        number_dec = str(elapsed_time-int(elapsed_time))[2:]
        formated_time_string = res + f"{number_dec} millisecs"
        full_string = function.__name__ + " took: " + formated_time_string
        print(full_string)
        return result
    return function_timer


@running_time
def sample_function():
    for i in range(1000):
        print(i)
    time.sleep(13)
    return 0


if __name__ == "__main__":
    sample_function()
