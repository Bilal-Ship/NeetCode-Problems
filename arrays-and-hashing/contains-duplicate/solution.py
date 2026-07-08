class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Made 2 sets, as I will store the numbers in them
        parsed = set()
        duplicate = set()
        #Assume default their are no repeats 
        repeat = False
        for i in nums:
            #If I is in our parsed set, add to duplicate set
            if i in parsed: 
                duplicate.add(i)
                repeat = True
            else:
                #else keep parsing
                parsed.add(i)
                pass
        #return final status
        return repeat 
