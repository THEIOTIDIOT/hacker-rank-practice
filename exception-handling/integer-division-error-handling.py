# https://docs.python.org/2/tutorial/errors.html#handling-exceptions

import sys
for _ in range(int(input())):
    try:
        nums = list(map(int,input().split()))
        print(nums[0] // nums[1])
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as ve:
        print("Error Code:",ve)