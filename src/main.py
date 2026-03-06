import sys
from fifo import fifo
from lru import lru
from optff import optff
def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py [input]")
        return
    
    try:
        with open(sys.argv[1], 'r') as f:
            k, m = map(int, f.readline().split()) # Read k and m from the first line
            sequence = list(map(int, f.readline().split())) # Read sequence after k and m
        
        print(f"FIFO: {fifo(k, m, sequence)}")
        print(f"LRU: {lru(k, m, sequence)}")
        print(f"OPTFF: {optff(k, m, sequence)}")

    except:
        print("Could not find input file.")

if __name__ == "__main__":
    main()