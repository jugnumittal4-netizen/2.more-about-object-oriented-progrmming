class pair_elements():
    def two_sum(self,nums,target):
        lookup = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in lookup:
                return (lookup[complement], i)
            lookup[num] = i
value = int(input("Enter the target value: "))
print("index1 = %d, index2 = %d" % pair_elements().two_sum([10,20,30,40,50,60,70], value))