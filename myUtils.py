import random
import math
import csv

#low and high denote range random values could be
def make_list(size, low=0, high=1000):
    high = size
    list = []
    for i in range(0, size):
        list.append(math.floor(low+random.random()*high))
    return list

def write_to_file(results):
    with open(f'results.csv', "a") as f:
        writer = csv.writer(f,delimiter= ',')
        writer.writerows(results)
    return

def print_pretty(i, size, time,ROUND):
    print(f"Test #{i+1}")
    print(f"List size:\t{size}")
    rtime = round(time, ROUND)
    print(f"Time:\t\t{rtime} seconds\n")
    return

