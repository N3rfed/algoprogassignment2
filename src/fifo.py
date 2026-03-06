from collections import deque
# Implementation of First In First Out Cache Eviction
def fifo(capacity, sequenceSize, sequence):
    misses = 0
    fifoQueue = deque(maxlen=capacity)

    for i in range(sequenceSize):
        if sequence[i] in fifoQueue: # Hit
            continue
            
        else: # Miss, have to check if queue is full or if there is space
            misses += 1
            if len(fifoQueue) < capacity: # Queue is not full
                fifoQueue.append(sequence[i])
                continue
            else: # Queue is full
                fifoQueue.popleft()
                fifoQueue.append(sequence[i])
                continue
    
    return misses