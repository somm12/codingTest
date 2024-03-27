# You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

# Implement the SmallestInfiniteSet class:

# SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
# int popSmallest() Removes and returns the smallest integer contained in the infinite set.
# void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.

# Smallest Number in Infinite Set: leetcode
import heapq
class SmallestInfiniteSet:
    answer = []

    def __init__(self):# contain all positive integers
        self.smallestSet = set([i for i in range(1,1001)])
        self.smallestQ = [i for i in range(1,1001)]
        return None
        

    def popSmallest(self) -> int:# remove and return smallest integer in infinite set
        data = heapq.heappop(self.smallestQ)
        self.smallestSet.remove(data)
        return data
        
        

    def addBack(self, num: int) -> None:
        if num not in self.smallestSet:
            self.smallestSet.add(num)
            heapq.heappush(self.smallestQ,num)
            return None
    


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)


