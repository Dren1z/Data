'''
This program calculates the total time of the triathlon and determines the reward

variables:
    swim        - Total time of swimming
    cycle       - Total time of cycling
    run         - Total time of running
    total_time  - sum of all of the times
'''


swim = int(input("Total time of swimming in minutes: "))
cycle = int(input("Total time of cycling in minutes: "))
run = int(input("Total time of running in minutes: "))

total_time = swim + cycle + run # sum of the times

if 0 <= total_time <= 100:
    print("Provincial Colours")
if 101 <= total_time <=105:
    print("Provincial Half Colours")
if 106<= total_time <= 110:
    print("Provincial Scroll")
if total_time >= 111:
    print("No award")