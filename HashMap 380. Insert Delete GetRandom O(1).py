#网上的办法是，多创建一个array,map记录index,要删除某个元素的时候，把index和array最后一个元素交换，pop一下，然后map的key删掉，速度比我的快

#估计是random那里，map的keys() to list速度有点慢吧


class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.m:
            self.m[val] = 1
            return True
        return False
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.m:
            self.m.pop(val, 0)
            return True
        return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        """
        return random.choice(list(self.m.keys()))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
