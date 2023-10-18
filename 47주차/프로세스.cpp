#include <string>
#include <vector>
#include <deque>
using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    vector<int> res;
    deque<pair<int,int>> q;
    
    for (int i =0 ; i< priorities.size(); i++){
        q.push_back({priorities[i],i});
    }
    int cnt = 0;
    
    while (q.size()> 0) {
        pair<int,int> now = q.front();
        q.pop_front();
        int flag = true;
        for (int i =0; i < q.size(); i++) {
            if (now.first < q[i].first ) {
                q.push_back(now);
                flag = false;
                break;
            }
        }
        if (flag) res.push_back(now.second);
      
    }
    
    for (int i =0; i< res.size();i++){
        if (res[i]== location) return i+1;
    }
    
    return answer;
}