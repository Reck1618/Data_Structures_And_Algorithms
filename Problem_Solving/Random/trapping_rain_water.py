"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array 
[0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
"""

def trap(height):
    if not height:
        return 0

    ans = 0
    l, r = 0, len(height) - 1
    maxleft, maxright = height[l], height[r]

    while l < r:
        if maxleft < maxright:
            l += 1
            maxleft = max(maxleft, height[l])
            ans += maxleft - height[l]

        else:
            r -= 1
            maxright = max(maxright, height[r])
            ans += maxright - height[r]

    return ans


def main():
    print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(trap([4,2,0,3,2,5]))

main()