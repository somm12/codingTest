#include<bits/stdc++.h>
using namespace std;
int n;
int m;
struct Pos {
    int x,y;
};
vector<Pos> p;
vector<Pos> h;
vector<Pos> c;
int answer = 9999999;

int dist(){// 도시 치킨 거리 구하기.
    int total =0;
    for (auto a: h){
        int d = 999999;
        for (auto b: p){// 가장 최솟값이 치킨 거리.
            d = min(d, abs(a.x-b.x)+abs(a.y-b.y));
        }
        total += d;
    }
    return total;
}

void dfs(int start){
    if (p.size() == m){
        answer = min(answer, dist());
        return;
    }
    for (int i = start; i < c.size();i++){
        p.push_back(c[i]);
        dfs(i+1);
        p.pop_back();
    }
}
int main(){
    
    cin >> n >> m;
       
    for (int i = 0; i < n; i++) {
        
        for (int j = 0; j < n; j++) {
            int tmp;
            cin >> tmp;
            if (tmp == 1){// 집
                h.push_back({i,j});
            }   
            else if (tmp == 2){//치킨집
                c.push_back({i,j});
            }
        }
    }
    
    dfs(0);
    cout << answer;
    return 0;
}