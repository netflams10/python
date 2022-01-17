Data Structure and Algorithm

    - An algorithm is a set of instructions for accomplishing a task. Every piece of code could be called an algorithm

    - Generally you want to choose the most efficient algorithm whether you’re trying to optimize for time or space.
    
    - Big O notation is special notation that tells you how fast an algorithm is.

    - Big O notation tells you how fast an algorithm is. Big O doesn’t tell you the speed in seconds. Big O notation lets you compare the number of operations. It tells you how fast the algorithm grows.

    -Big O notation is about the worst-case scenario

    - Examples of Big
        • O(log n), also known as log time. Example: Binary search.
        • O(n), also known as linear time. Example: Simple search.
        • O(n * log n). Example: A fast sorting algorithm, like quicksort (coming up in chapter 4).
        • O(n 2 ). Example: A slow sorting algorithm, like selection sort (coming up in chapter 2).
        • O(n!). Example: A really slow algorithm, like the traveling salesperson (coming up next!).


    - Takeaways
        • Algorithm speed isn’t measured in seconds, but in growth of the number of operations.
        • Instead, we talk about how quickly the run time of an algorithm increases as the size of the input increases.
        • Run time of algorithms is expressed in Big O notation.
        • O(log n) is faster than O(n), but it gets a lot faster as the list of items you’re searching grows.

    - travalling salesman <----> n! (n factorial)