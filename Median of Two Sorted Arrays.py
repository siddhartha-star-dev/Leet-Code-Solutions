class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) < len(nums2):
            A,B = nums1, nums2 
        else:
            A,B = nums2,nums1
        total = len(nums1) + len(nums2)
        half = total//2
        l, r = 0, len(A)-1
        
        while True:
            i = (l+r)//2
            j = half - i - 2
            
            Aleft = float(A[i]) if i >=0 else float("-infinity")
            Aright = float(A[i+1]) if i+1 < len(A) else float("infinity")
            Bleft = float(B[j]) if j>=0 else float("-infinity")
            Bright = float(B[j+1]) if j+1 < len(B) else float("infinity")

            if Aleft<=Bright and Bleft <= Aright:
                if total%2:
                    return min(Aright,Bright)
                
                return (min(Aright, Bright) + max(Aleft, Bleft)) / 2            
            
            elif Aleft>Bright:
                r = i-1
            else:
                l = i+1
