'''
Problem Statement: The weight of N items and their corresponding values are given. We have to put these items in a knapsack of weight W 
such that the total value obtained is maximized.
Note: We can either take the item as a whole or break it into smaller units.
'''

# ^ The greedy method to maximize our answer will be to pick up the items with higher values. 
# ^ Since it is possible to break the items as well we should focus on picking up items having higher value /weight first. 
# ^ To achieve this, items should be sorted in decreasing order with respect to their value /weight. 
# ^ Once the items are sorted we can iterate. Pick up items with weight lesser than or equal to the current capacity of the knapsack. 
# ^ In the end, if the weight of an item becomes more than what we can carry, break the item into smaller units. 
# ^ Calculate its value according to our current capacity and add this new value to our answer.

class Item:
    def __init__(self, value, weight):
        self.weight = weight
        self.value = value

def fractionalKnapsack(W, items, n):
    items.sort(key=lambda x: x.value/x.weight, reverse=True)
    currWeight = 0.0
    finalValue = 0.0

    for i in range(n):
        if currWeight + items[i].weight <= W:
            currWeight += items[i].weight
            finalValue += items[i].value
        
        else:
            remaining = W - currWeight
            finalValue += remaining * (items[i].value / items[i].weight)
            break
    
    return finalValue

n = 3
W = 50
items = [Item(60, 10), Item(100, 20), Item(120, 30)]
print("The maximum value is ")
print(fractionalKnapsack(W, items, n))