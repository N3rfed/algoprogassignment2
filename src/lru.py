# Implementation of LRU (Least Recently Used) Cache Eviction
def lru(capacity, sequenceSize, sequence):
    misses = 0
    cacheFrequency = {} # Use a hashmap to record object and frequency
    for i in range (sequenceSize):
        # Check to see if the requested object is in the cache. If it is, its a hit. Hits store the time of last access
        if sequence[i] in cacheFrequency:
            cacheFrequency[sequence[i]] = i
        # If the object is not in the cache:
        else:
        # Check to see if the cacheFrequency hashmap is at the capacity. If not, add the object to the hashmap with the current index i
            if len(cacheFrequency) != capacity:
                cacheFrequency[sequence[i]] = i
                misses += 1
        # If the hashmap is at the capacity, look for the object with the smallest index. Replace that object with the current object with current index i.
            else:
                evicted = min(cacheFrequency, key=cacheFrequency.get)
                del cacheFrequency[evicted]
                cacheFrequency[sequence[i]] = i 
                misses += 1