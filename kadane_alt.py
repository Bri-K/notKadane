# This script is a function that finds the largest sum amongst all
# contiguous subarrays in a given array `nums`. It's an alternative
# to Kadane's algorithm. See the comments at the bottom.

# Idea: A contiguous subarray sum, say from index i to index j, is
# the sum from 0 to j, minus the sum from 0 to i-1. So for any given
# 0 to j sum, we'd like to subtract the most negative 0 to i-1 sum unless
# there are no negative such sums, and then the 0 to j sum is the max.
# Basically, we just need to iterate through the list, keeping track of
# 0 to j sums and the most negative 0 to i-1 sum to the left. All the
# while we'll update the result whenever it exceeds our previous record.
# The solution is O(n) time and O(1) space complexity.

def notKadane(nums):
    res = nums[0]
    most_neg_left = 0
    curr_sum = nums[0]

    for i in range(1, len(nums)):
        if curr_sum < most_neg_left:
            most_neg_left = curr_sum
        curr_sum = curr_sum + nums[i]
        if curr_sum - most_neg_left > res:
            res = curr_sum - most_neg_left

    return res

# The solution looks different from the standard one, which is Kadane's
# algorithm. However, there is a similarity. They both turn on the idea
# of identifying in O(1) time, for fixed j, the maximum over i of each i to
# j sum. Kadane does this recursively: An i to j sum is an i to j-1 sum
# plus the j term, except when i=j where we just have the j term. So the
# max over i of i to j sums is the max of (the max over i of i to j-1 sums)
# and (the j term). Kadane's algorithm is thus based on:
# new_max = max(old_max + arr[i]), arr[i]).
