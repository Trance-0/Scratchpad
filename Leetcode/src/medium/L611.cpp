class Solution {
    public:
        int triangleNumber(vector<int>& nums) {
            // sort(nums.begin(),nums.end());
            // int n=nums.size();
            // int res=0;
            // for(int i=0;i<n-2;i++){
            //     for(int j=i+1;j<n-1;j++){
            //         int k = lower_bound(nums.begin()+j+1,nums.end(),nums[i]+nums[j])-nums.begin();
            //         res+=k-j-1;
            //     }
            // }
            // return res;
            // two pointer
            sort(nums.begin(),nums.end());
            int n=nums.size();
            int res=0;
            for (int i=0;i<n-2;i++) cout<<nums[i]<<" ";
            for(int i=0;i<n-2;i++){
                int k=i+2;
                for (int j=i+1;j<n-1;j++){
                    while(k<n&&nums[i]+nums[j]>nums[k]){
                        k++;
                    }
                    cout<<i<<" "<<j<<" "<<k<<endl;
                    if (k<=j) break;
                    res+=k-j-1;
                }
            }
            return res;
        }
    };