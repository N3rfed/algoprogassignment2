import sys
from fifo import fifo
from lru import lru
from optff import optff

def main():
    
    if len(sys.argv) < 2:
        print("Usage: python main.py [input]")
        return
    
    inputFile = sys.argv[1]
    outputFile = inputFile.replace(".in", ".out") if ".in" in inputFile else "example.out"

    try:
        
        with open(sys.argv[1], 'r') as inputF:
            k, m = map(int, inputF.readline().split()) # Read k and m from the first line
            sequence = list(map(int, inputF.readline().split())) # Read sequence after k and m
        
        with open(outputFile, 'w') as outputF:
            outputF.write(f"FIFO: {fifo(k, m, sequence)}\n")
            outputF.write(f"LRU: {lru(k, m, sequence)}\n")
            outputF.write(f"OPTFF: {optff(k, m, sequence)}")

    except:
        print("Could not find input file.")

if __name__ == "__main__":
    main()