import heapq
# in python no concept of max heap , only min heap
# so insert elements by multiply with -1 and call heapify
class stream:
    def __init__(self,Right_hp ,Left_hp):
        self.Left_hp = Left_hp
        self.Right_hp = Right_hp
    

    def insert_elements(self, A):
        

        if len(self.Left_hp) < len(Right_hp)   : # to make the L tree  and R tree balanced
            ele = heapq.heappop(self.Right_hp)  # pop from right and move to left
            heapq.heappush(self.Left_hp ,-1 * ele)

        elif len(self.Left_hp)   > len(self.Right_hp)  :
            ele = heapq.heappop(self.Left_hp)  # pop from left and move to right
            heapq.heappush(self.Right_hp ,-1 * ele)

        if len(self.Left_hp) > 0 and self.Left_hp[0]*-1 < A :  # elements > than the top of max heap LEFT TREE is pushed to RIGHT tree
            heapq.heappush(self.Right_hp , A)
        else:
            heapq.heappush(self.Left_hp , -1 * A)

    def get_median(self):
        if len(self.Left_hp) == len(self.Right_hp) :
            return (-1 * self.Left_hp[0] + self.Right_hp[0]) /2
        else:
            if len(self.Left_hp) > len(self.Right_hp):
                return self.Left_hp[0]  #  in python no pop needed in constant time minimum element in shown here it is negative
            else:
                return self.Right_hp[0]  # in python no pop needed in constant time minimum element in shown  
    

    def insert_list_of_elements(self,L): # to insert a stream of elements using a list
        for ele in L:
            self.insert_elements(ele)

Left_hp = []  # max heap
heapq.heapify(Left_hp)  # making a heap of left tree
Right_hp = [] # min heap
heapq.heapify(Right_hp) # making a heap of right tree     
ob = stream(Right_hp,Left_hp) # object of class stream



List_A = [1,2,34,1,2,67,12,13,14]
List_B = [87,34,23,34,13,1356,64,98,45]
ob.insert_list_of_elements(List_A)
print(ob.Left_hp)
print(ob.Right_hp)
print("median = " ,ob.get_median() )


ob.insert_list_of_elements(List_B)
print(ob.Left_hp)
print(ob.Right_hp)
print("median = " ,ob.get_median() )

'''



Time Complexity :  
Read median = O(1)  # No need to pop the elements as I am using Python and heap is maintained in a List .

Write a element =
If both the left and right heap has same size ,
    O(log n) , here n is the size of the heap either left or right as it is balanced .

If both the left and right heap has different size ,
    Pop from the left or right = O(log n) # to rearrange
    Push in another side = O(log n ) #to rearrange
    Now the tree is balanced
    O(log n) , here n is the size of the heap either left or right as it is balanced .
    
    total tle = 3 * O(log n) = O(log n) '''