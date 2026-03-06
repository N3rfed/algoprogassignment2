import os
import random
from fifo import fifo
from lru import lru
from optff import optff

def generateInput(filename, k=3, m=60, max_id=10):
    requests = []
    for i in range(m):
        if random.random() < 0.7:
            requests.append(random.randint(1, 5))
        else:
            requests.append(random.randint(1, max_id))

    with open(filename, "w") as f:
        f.write(f"{k} {m}\n")
        f.write(" ".join(map(str, requests)))
    return requests

def runTests():
    base_folder = "tests"
    os.makedirs(base_folder, exist_ok=True)

    existing = [
        d for d in os.listdir(base_folder)
        if d.startswith("question1-test")
    ]

    test_number = len(existing) + 1
    test_folder = os.path.join(base_folder, f"question1-test{test_number}")
    os.makedirs(test_folder)

    results = []
    for i in range(1, 4):

        filename = f"file{i}.in"
        filepath = os.path.join(test_folder, filename)

        k = random.randint(3, 6)
        m = random.randint(50, 80)

        sequence = generate_input(filepath, k, m)

        fifo_misses = fifo(k, m, sequence)
        lru_misses = lru(k, m, sequence)
        optff_misses = optff(k, m, sequence)

        results.append((filename, k, m, fifo_misses, lru_misses, optff_misses))

    print("\nInput File\tk\tm\tFIFO\tLRU\tOPTFF")

    for r in results:
        print(f"{r[0]}\t{r[1]}\t{r[2]}\t{r[3]}\t{r[4]}\t{r[5]}")

if __name__ == "__main__":
    runTests()