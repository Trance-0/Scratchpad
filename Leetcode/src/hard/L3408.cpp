class TaskManager {
    public:
        unordered_map<int,int>tskpri;
        unordered_map<int,int>tskusr;
        priority_queue<vector<int>,vector<vector<int>>>pq;
    
        TaskManager(vector<vector<int>>& tasks) {
            for(vector t : tasks){
                add(t[0],t[1],t[2]);
            }
        }
        
        void add(int userId, int taskId, int priority) {
            tskpri[taskId]=priority;
            tskusr[taskId]=userId;
            pq.push({priority,taskId,userId});
        }
        
        void edit(int taskId, int newPriority) {
            tskpri[taskId]=newPriority;
            pq.push({newPriority,taskId,tskusr[taskId]});
        }
        
        void rmv(int taskId) {
            tskpri.erase(taskId);
            tskusr.erase(taskId);
        }
        
        int execTop() {
            int result=-1;
            while(!pq.empty()){
                auto t=pq.top();
                pq.pop();
                if(tskusr.find(t[1])==tskusr.end() || tskpri[t[1]]!=t[0]) continue;
                cout<<t[0]<<" "<<t[1]<<" "<<t[2]<<endl;
                rmv(t[1]);
                result=t[2];
                break;
            }
            return result;
        }
    };
    
    /**
     * Your TaskManager object will be instantiated and called as such:
     * TaskManager* obj = new TaskManager(tasks);
     * obj->add(userId,taskId,priority);
     * obj->edit(taskId,newPriority);
     * obj->rmv(taskId);
     * int param_4 = obj->execTop();
     */