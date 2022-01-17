Binary Search

    - Binary search is an algorithm; its input is a sorted list of elements
        - Return position of element or null if can't be found
        - With binary search, you guess the middle number and eliminate half the remaining numbers every time.
        - log<sub>10</sub>100 is like asking how many times do we multiply 10s to get 100

            - 2<sup>3</sup> = 8 <--> log<sub>2</sub>8 = 3
    
    - This search only works when our list is sorted.

    - Suppose you have a sorted list of 128 names, and you’re searching through it using binary search. What’s the maximum number of steps it would take?

    - Binary search runs in logarithmic time or log time,

    


     Items        |    Linear      |  Binary
    ------------- | -------------  |-------------
       100        |  100 Guesse    |  7 Guesses log<sub>2</sub>100 = 7
       4 Billion  |  4 Bill Guesse |  32 Guesses


    - you need to know how the running time increases as the list size increases

    - Big O notation tells you how fast an algorithm is. Big O doesn’t tell you the speed in seconds. Big O notation lets you compare the number of operations. It tells you how fast the algorithm grows.

    - running time in Big O notation? It’s O(log n) <--> n = number of opertion. This tells you the number of operations an algorithm will make.

    - Algorithm linear takes O(n) time, and algorithm binary search takes O(log n) time.

