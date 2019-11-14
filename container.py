def maxArea(height):
    if height is None or len(height) <= 2:
        return 0

    maximum,left,right = 0,0,len(height)-1

    while left < right:
        maximum = max(maximum, min(height[left],height[right])*(right - left))

        if height[left] < height[right]:
            left+=1
        else:
            right-=1

    return maximum

def trap(height):
    if height is None:
        return 0

    result,left_max,right_max,lo,hi = 0,0,0,0,len(height)-1

    while lo <= hi:
        if height[lo] < height[hi]:
            if height[lo] > left_max:
                left_max = height[lo]
            else:
                result += left_max - height[lo]

            lo+=1
        else:
            if height[hi] > right_max:
                right_max = height[hi]
            else:
                result += right_max - height[hi]

            hi-=1

    return result
    

H = [1,8,6,2,5,4,8,3,7]
print(maxArea(H))
print(trap(H))