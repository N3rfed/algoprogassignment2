# algoprogassignment2
Brianna Chua, 76131392

Jaden Delapaz, 19812001

# Requirements/Assumptions
1. Python is installed

# How to Run (singular tests)
1. In a terminal, enter the src directory
2. Run "python main.py /tests/example.in"

# How to Run (question 1 test and generation)
1. In a terminal, enter the src directory
2. Run "python generator.py"
3. 3 nontrivial files can be found in /tests/question1-test#

# Question 1
![table of input files and results](image.png)
(3 generated files can be seen in /tests/question1-test1)

Does OPTFF have the fewest misses?
Yes. According to the table, in all three input files, OPTFF has the fewest cache misses compared to FIFO and LRU.

How does FIFO compare to LRU?
In these tests, LRU performs slightly better than FIFO. While in file1.in, FIFO and LRU perform the exact same (51 misses each), in file2.in and file3.in, LRU performs better with 3 and 1 less misses respectively.

# Question 2

There exists a request sequence where k = 3 for which OPTFF incurs strictly fewer misses than LRU.

Suppose we have a sequence:

[4 3 2 1 4 3 3]

With LRU as our cache eviction policy, it will have a total of 6 misses.
With OPTFF as our cache eviction policy, it will have a total of 4 misses. 

The reason why OPTFF has strictly fewer misses than LRU in this case is because OPTFF knows when an item will be used in the future. In this case, it sees that [4 3] will be requested again, and does not evict them. On the other hand, the LRU eviction policy only chooses to evict the item when it sees that it hasn't been used in a while. This causes more misses, since it evicts the item 4 when 1 is requested, not knowing 4 will be requested right after.

# Question 3