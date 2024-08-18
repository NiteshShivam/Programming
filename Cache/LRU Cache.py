
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


# python
======================

class LRUCache:
     
    
    def __init__(self,cap):
        self.cache = []
        self.cap = cap
        
        
        
    #Function to return value corresponding to the key.
    def get(self, key):
        for i in range(len(self.cache)):
            if self.cache[i][0]==key:
                val = self.cache[i][1]
                temp = self.cache[i]
                self.cache.pop(i)
                self.cache.append(temp)
                return val
        return -1
        
    #Function for storing key-value pair.   
    def set(self, key, value):
        for i in range(len(self.cache)):
            if self.cache[i][0]==key:
                self.cache.pop(i)
                self.cache.append((key,value))
                return
        if len(self.cache)<self.cap:
            self.cache.append((key,value))
        else:
            self.cache.pop(0)
            self.cache.append((key,value))


