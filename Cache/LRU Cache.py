'''
https://www.geeksforgeeks.org/problems/lru-cache/1
https://youtu.be/81h8O-0U5oo
'''

# python given time limit in gfg
from collections import deque
class LRUCache:
      
    #Constructor for initializing the cache capacity with the given value.  
    def __init__(self,cap):
        self.dll = deque()
        self.cache = {}
        self.capacity = cap
    #Function to return value corresponding to the key.
    def makerentlyUsed(self,key):
        self.dll.remove(key)
        self.dll.appendleft(key)
    def get(self, key):
        if key not in self.cache:
            return -1
        self.makerentlyUsed(key)
        return self.cache[key]
        
    #Function for storing key-value pair.   
    def set(self, key, value):
        if key in self.cache:
            self.cache[key]=value
            self.makerentlyUsed(key)
        else:
            self.dll.appendleft(key)
            self.cache[key]=value
            self.capacity -=1
        if self.capacity<0:
            del self.cache[self.dll.pop()]
            self.capacity +=1
            



==============
class LRUCache
{
    private:

    public:
    list<int> dll;
    map<int,pair<list<int>::iterator,int>>mp;
    int n;
    //Constructor for initializing the cache capacity with the given value.
    LRUCache(int cap)
    {
       n=cap;
        // code here
    }
    
    void makerecentUsed(int key){
        dll.erase(mp[key].first);
        dll.push_front(key);
        mp[key].first = dll.begin();
    }
    int GET(int key)
    {
        if(mp.find(key)==mp.end()){
            return -1;
        }
        makerecentUsed(key);
        return mp[key].second;
    }
    
    //Function for storing key-value pair.
    void SET(int key, int value)
    {
        if(mp.find(key)!=mp.end()){
            mp[key].second = value;
            makerecentUsed(key);
            
        } 
        else{
            dll.push_front(key);
            mp[key]={dll.begin(),value};
            n--;
        }
        if(n<0){
            int key_del = dll.back();
            mp.erase(key_del);
            dll.pop_back();
            n++;

        }
    }
};
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


