class Solution {
public:
    bool testStartTime(long long testStart, vector<int>& skill, int& mana, vector<long long>& currentTime, vector<long long>& testTime, int& n, int&m) {
        bool ret=true;
        testTime.clear();
        for(int j=0;j<n-1;j++){
            testStart+=skill[j]*mana;
            // cout<<'c'<<currentTime[j]<<currentTime.size()<<':'<<mana<<endl;
            if(testStart<currentTime[j+1]){
                ret=false;
                break;
            }
            testTime.push_back(testStart);
        }
        // for (int i=0;i<testTime.size();i++) cout<< testTime[i]<<' ';
        // cout<<endl;
        // cout<<ret<<endl;
        testTime.push_back(testStart+skill[n-1]*mana);
        return ret;
    }
    long long minTime(vector<int>& skill, vector<int>& mana) {
        // record time done
        vector<long long>init;
        int n=skill.size(),m=mana.size();
        long long curStart=0;
        for(int i=0;i<n;i++){
            curStart+=skill[i]*mana[0];
            init.push_back(curStart);
        }
        for (int i = 1; i < m; i++){
            // bisect for min start time
            long long lo=init.front(),hi=init.back();
            vector<long long>ninit;
            while (lo<hi){
                long long mid=(lo+hi)>>1;
                if(testStartTime(mid,skill,mana[i],init,ninit, n,m)){
                    hi=mid;
                }else{
                    lo=mid+1;
                }
            }testStartTime(lo,skill,mana[i],init,ninit, n,m);
            // cout<<lo<<':'<<mana[i]<<endl;
            swap(init,ninit);
        }
        return init.back();
    }
};