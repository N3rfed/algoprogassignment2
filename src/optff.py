# Implementation of OPTFF (Belady’s Farthest-in-Future, optimal offline) Cache Eviction
def optff(capacity, sequenceSize, sequence):
    misses = 0
    cacheMap = {}
    
    for i in range(sequenceSize):
        if sequence[i] in cacheMap: # First check if the cache is a hit.
            continue
        
        else: # Otherwise, this is a miss. 

            if len(cacheMap) != capacity: # Check if the cache is full. If not, we just continue.
                continue
            
            else: # Cache is full, we need to evict
                pass
            misses += 1
