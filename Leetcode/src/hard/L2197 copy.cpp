class Solution {
    
    public:
        vector<int> replaceNonCoprimes(vector<int>& nums) {
            vector<int>res;
            res.push_back(nums[0]);
            for (int i=1;i<nums.size();i++){
                int cur=nums[i];
                while (res.size()>0 && __gcd(res.back(),cur)!=1){
                    cur=res.back()/__gcd(res.back(),cur)*cur;
                    res.pop_back();
                }
                res.push_back(cur);
            }
            return res;
        }
    };