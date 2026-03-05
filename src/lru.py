# Implementation of LRU (Least Recently Used) Cache Eviction
def lru(capacity, sequenceSize, sequence):
    misses = 0
    cacheFrequency = {} # Use a hashmap to record object and frequency
    
    for i in range (sequenceSize):
        if sequence[i] in cacheFrequency: # Check to see if the requested object is in the cache. If it is, its a hit. Hits store the time of last access
            cacheFrequency[sequence[i]] = i

        else: # If the object is not in the cache:
            
            if len(cacheFrequency) != capacity: # Check to see if the hashmap is at the capacity. If not, add the object to the hashmap with the current index i
                cacheFrequency[sequence[i]] = i
                misses += 1
            
            else: # If the hashmap is at the capacity, look for the object with the smallest index. Replace that object with the current object with current index i.
                evicted = min(cacheFrequency, key=cacheFrequency.get)
                del cacheFrequency[evicted]
                cacheFrequency[sequence[i]] = i 
                misses += 1