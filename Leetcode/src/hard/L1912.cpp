class MovieRentingSystem {
    // movie -> price, shop
    unordered_map<int, priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>>> unrentedmovies;
    // -> price, shop, movie
    priority_queue<vector<int>,vector<vector<int>>,greater<vector<int>>> rentedmovies;
    // shop, movie -> bool
    unordered_map<int, unordered_map<int, bool>> latestStatus;
    // movie, shop -> price
    unordered_map<int, unordered_map<int, int>> moviePrice;
    public:
        MovieRentingSystem(int n, vector<vector<int>>& entries) {
            for (auto &entry : entries) {
                // shop, movie, price
                unrentedmovies[entry[1]].push(make_pair(entry[2], entry[0]));
                latestStatus[entry[0]][entry[1]] = false;
                moviePrice[entry[1]][entry[0]] = entry[2];
            }
        }
        
        vector<int> search(int movie) {
            vector<int>shops;
            for (int i=0;i<5;i++){
                if (unrentedmovies[movie].size() == 0) break;
                pair<int, int> entry = unrentedmovies[movie].top();
                while (unrentedmovies[movie].size() > 0 && latestStatus[entry.second][movie] == true) {
                    entry = unrentedmovies[movie].top();
                    unrentedmovies[movie].pop();
                }
                if (latestStatus[entry.second][movie] == true) break;
                rent(entry.second, movie);
                shops.push_back(entry.second);
            }
            for (int shop : shops) {
                drop(shop, movie);
            }
            return shops;
        }
        
        void rent(int shop, int movie) {
            latestStatus[shop][movie] = true;
            // cout << "rent: " << moviePrice[movie][shop] << " shop: " << shop << " movie: " << movie << endl;
            rentedmovies.push({moviePrice[movie][shop], shop, movie});
        }
        
        void drop(int shop, int movie) {
            latestStatus[shop][movie] = false;
            // cout << "drop: " << moviePrice[movie][shop] << " shop: " << shop << " movie: " << movie << endl;
            unrentedmovies[movie].push(make_pair(moviePrice[movie][shop], shop));
        }
        
        vector<vector<int>> report() {
            vector<vector<int>>result;
            // cout << "---report start---" << endl;
            // cout << "rentedmovies size: " << rentedmovies.size() << endl;
            for (int i=0;i<5;i++) {
                if (rentedmovies.size() == 0) break;
                // price, shop, movie
                vector<int> entry = rentedmovies.top();
                rentedmovies.pop();
                while (rentedmovies.size() > 0 && latestStatus[entry[1]][entry[2]] == false) {
                    // cout << "pop expired: " << moviePrice[entry[2]][entry[1]] << " shop: " << entry[1] << " movie: " << entry[2] << endl;
                    entry = rentedmovies.top();
                    rentedmovies.pop();
                }
                if (latestStatus[entry[1]][entry[2]] == false) break;
                // cout << "price: " << entry[0] << " shop: " << entry[1] << " movie: " << entry[2] << endl;
                drop(entry[1], entry[2]);
                result.push_back({entry[1], entry[2]});
            }
            for (vector<int> entry : result) {
                rent(entry[0], entry[1]);
            }
            // cout << "---report end---" << endl;
            return result;
        }
    };
    
    /**
     * Your MovieRentingSystem object will be instantiated and called as such:
     * MovieRentingSystem* obj = new MovieRentingSystem(n, entries);
     * vector<int> param_1 = obj->search(movie);
     * obj->rent(shop,movie);
     * obj->drop(shop,movie);
     * vector<vector<int>> param_4 = obj->report();
     */