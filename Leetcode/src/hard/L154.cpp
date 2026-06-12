class Solution {
public:
    int findMin(vector<int>& nums) {
        int lo=0;
        for (int hi=1;hi<nums.size();hi++){
            if (nums[lo]==nums[hi]){
                continue;
            }
            lo+=1;
            nums[lo]=nums[hi];
        }
        // the array is partially sorted, thus, binary search based on high element..
        int low=0,high=lo;
        while (low<high){
            int mid=low+(high-low)/2;
            // if middle element is lower than high element, the start of array is before mid.
            if(nums[mid]<nums[high]){
                high=mid;
            }else{
                low=mid+1;
            }
        }
        return nums[low];
    }
};