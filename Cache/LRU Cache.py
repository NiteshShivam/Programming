
# Brute Force
class LRUCache
{
    private:

    public:
    vector<pair<int,int>> cache;
    int n;
    //Constructor for initializing the cache capacity with the given value.
    LRUCache(int cap)
    {
        n=cap;
        // code here
    }
    
    //Function to return value corresponding to the key.
    int GET(int key)
    {
        for(int i=0;i<cache.size();i++){
            if(cache[i].first==key){
                int val = cache[i].second;
                pair<int,int>temp = cache[i];
                cache.erase(cache.begin()+i);
                cache.push_back(temp);
                return val;
            }
        }
        return -1;
    }
    
    //Function for storing key-value pair.
    void SET(int key, int value)
    {
        for(int i=0;i<cache.size();i++){
            if(cache[i].first==key){
                pair<int,int>temp = {key,value};
                cache.erase(cache.begin()+i);
                cache.push_back(temp);
                return;
            }
        }
        if(cache.size()<n){
            cache.push_back({key,value});
        }
        else{
            cache.erase(cache.begin());
            cache.push_back({key,value});
        }
    }
};

