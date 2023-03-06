import sys
import threading
import numpy

def compute_height(n, parents):
    parent = numpy.zeros
    def height(i):

        if parent[i] != 0:
            return parent[i]

        if parents[i] == -1:
            parent[i] = 1

        else:
            parent[i] = height(parents[i])+1
        return parent[i]
    
    for i in range(n):
        height(i)
    return int(max(parent))

def main():
    mode = input()

    if "F" in mode:
        filename = input()

        if "a" not in filename:
            with open(str("test/"+filename), mode="r") as f:
                nav = int(f.readline())
                parent = list(map(int, f.readline().split()))

        else :
            print("error")

    elif "I"in mode:
        nav = int(input())
        parent = list(map(int, input().split()))
        
    else:
        print("Invalid input mode.")
    print(compute_height(nav, parent))
        
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()