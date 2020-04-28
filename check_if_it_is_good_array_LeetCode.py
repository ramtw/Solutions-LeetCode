class Solution:
    def isGoodArray(self, nums):
        """
        Using the conept of the GCD highest common factor if the array has highest common factor of one then we can say
        somehow we can obtain the sum 1 by multiplying the appropriate value.
        :param nums: An array of the Positive numbers
        :return: Boolean values
        """
        # Intial Condition if empty string
        if len(nums) == 0:
            return False
        # If Array has one element then it must be true if the value is 1
        if len(nums) == 1:
            if nums[0] == 1:
                return True
            else:
                return False
        # Intial value for the GCD value
        good_value = self.gcd(nums[0], nums[1])
        # Looping from the second value till the end
        # example [2, 26,6,10, 3] ==> 2,26 = 2 ==> 2, 6 => 2 ==> 2, 10 ==> 2 and 2,3 ==> 1
        # so True in the above example
        for num in nums[2:]:
            good_value = self.gcd(good_value, num)
        # Checking if the good_value is equal to 1 according to the question
        if good_value == 1:
            return True
        else:
            return False
    # normal GCD function
    def gcd(self, m, n):
        """

        :param m: The interger value
        :param n: The integer value
        :return: The Highest common factor of the two number as a integer value
        """
        if m > n:
            m, n = n, m
        if n % m == 0:
            return m
        else:
            return self.gcd(n % m, m)

solve = Solution()
bool=solve.isGoodArray([12,5,7,23])
print(bool)