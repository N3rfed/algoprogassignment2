# Implementation of OPTFF (Belady’s Farthest-in-Future, optimal offline) Cache Eviction
def optff(capacity, sequenceSize, sequence):
    cache = set()
    misses = 0

    for i in range(sequenceSize):
        r = sequence[i]
        if r in cache:
            continue
        misses += 1

        if len(cache) < capacity:
            cache.add(r)
            continue

        farthest = -1
        victim = None

        for item in cache:
            next_use = float('inf')

            for j in range(i + 1, sequenceSize):
                if sequence[j] == item:
                    next_use = j
                    break

            if next_use > farthest:
                farthest = next_use
                victim = item

        cache.remove(victim)
        cache.add(r)
    return misses
