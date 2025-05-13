from typing import List

# Define a class named Solution
class Solution:
    """
    A class containing a method to check for duplicates in a list.

    Methods
    -------
    hasDuplicate(nums: List[int]) -> bool
        Determines if a list contains any duplicate elements.
    """
    
    """
    Checks if the given list of integers contains any duplicate elements.

    Parameters
    ----------
    nums : List[int]
        A list of integers to check for duplicates.

    Returns
    -------
    bool
        True if the list contains duplicates, False otherwise.
    """
    # Define a method to check for duplicates in a list
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Sort the list to bring duplicates next to each other
        nums.sort()
        # Iterate through the list starting from the second element
        for i in range(1, len(nums)):
            # Check if the current element is the same as the previous one
            if nums[i] == nums[i - 1]:
                # If a duplicate is found, return True
                return True
        # If no duplicates are found, return False
        return False

# Define a list of integers with some duplicate values
lista = [2, 3, 4, 5, 4, 3, 5, 6, 8, 4, 6]

# Create an instance of the Solution class
a = Solution()

# Call the hasDuplicate method with the list and store the result
res = a.hasDuplicate(lista)

# Print the result (True if duplicates exist, False otherwise)
print(res)
