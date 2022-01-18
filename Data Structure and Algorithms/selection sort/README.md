SELECTION SORT

    - Array and Linked List

        - Using an array means all your tasks are stored contiguously (right next to each other) in memory. In which if you want to add more to you array and there is no space in memory again so we have to move the whole array to a new space in memory

        - with Linked list your item can be anywhere in the memory. Each item stores the address of the next item in the list.

        - Linked lists are great if you’re going to read all the items one at a time: you can read one item, follow the address to the next item, and so on. But if you’re going to keep jumping around, linked lists are terrible.

        - Elements in an array starts from one.

        - The position of an element is called its index.


                       |    Arrays      |   Linked List
        ---------------|----------------|----------------
           READING     |      0(1)      |    O(n)
        ---------------|----------------|----------------
           INSERTION   |      0(n)      |    0(1)
        ---------------|----------------|----------------
           DELETION    |      0(n)      |    0(1)


    - Example selection Sort

        - You want to sort this list from most to least played, so that you can rank your favorite artists. How can you do it?

            - This takes O(n) time to to search through an asset. So you have an operation that takes O(n) time, and you have to do that n times: The number of Element to check must keep decreasing.

              Existing Array to sort 0(n) | Existing array decreases 0(n) |  Add the new to new Array 0(n)
              ----------------------------|-------------------------------
                                0(n X n) => 0(n<sup>2</sup>) 
                                NOTE: O(n × 1 / 2 × n) -> Constants like 1/2 are neglected in Big 0 notation

        • Names in a phone book
        • Travel dates
        • Emails (newest to oldest)