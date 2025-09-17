class Solution {

    vector<int>ps(int n){
        // generate prime sieves
        vector<bool>isPrime(n+1,true);
        for (int i=2;i*i<=n;i++){
            if (isPrime[i]){
                for (int j=i*i;j<=n;j+=i){
                    isPrime[j]=false;
                }
            }
        }
        vector<int>primes;
        for (int i=2;i<=n;i++){
            if (isPrime[i]){
                primes.push_back(i);
            }
        }
        return primes;
    }
    void merge(vector<int>&a,vector<int>&b){
        for (int i=0;i<a.size();i++){
            a[i]=max(a[i],b[i]);
        }
    }
    
    public:
        vector<int> replaceNonCoprimes(vector<int>& nums) {
            vector<vector<int>> buf;
            vector<int>primes=ps(1000000);
            int pn=primes.size();
            buf.push_back(vector<int>(pn,0));
            for (int i:nums){
                bool merge=false;
                vector<int>nxt=vector<int>(pn,0);
                for (int j=0;j<pn;j++){
                    while (i%primes[j]==0){
                        nxt[j]++;
                        i/=primes[j];
                    }
                }
                if (merge) merge(buf.back(),nxt);
                else buf.push_back(nxt);
            }
            ps=1;
            for (int j=0;j<pn;j++){
                ps*=pow(primes[j],cur[j]);
            }
            res.push_back(ps);
            res.erase(res.begin());
            return res;
        }
    };