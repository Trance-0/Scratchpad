class Solution {
public:
    int trapRainWater(vector<vector<int>>& heightMap) {
        int m=heightMap.size(),n=heightMap[0].size();
        int res=0;
        int dir[5]={0,1,0,-1,0};
        for (int i=1;i<n-1;i++){
            for(int j=1;j<m-1;j++){
                d=0;
                int lo=heightMap[i+dir[d]][j+dir[d]];
                for (d=1;d<4;d++){
                    lo=min(lo,heightMap[i+dir[d]][j+dir[d]]);
                }
                if lo<heightMap
            }
        }
        return res;
    }
};