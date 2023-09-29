#include<vector>
#include<iostream>
#include<queue>

using namespace std;

int check[100][100];
int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};

int solution(vector<vector<int> > maps)
{
    int n, m;
    n = maps.size();
    m = maps[0].size();
    queue<pair<int, int>> q;
    q.push(make_pair(0, 0));
    check[0][0] = true;

    while(!q.empty()){
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for(int i=0; i<4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(0<=nx && nx<n && 0<=ny && ny<m){
                if(check[nx][ny] == false && maps[nx][ny] > 0){
                    check[nx][ny] = true;
                    maps[nx][ny] = maps[x][y] + 1;
                    q.push(make_pair(nx, ny));
                }
            }
        }
    }



    int answer = 0;
    if(maps[n-1][m-1] == 1){
        answer = -1;
    }else{
        answer = maps[n-1][m-1];
    }
    return answer;
}
// 프로그래머스 BFS c++로 풀어보기.
// n행 m열에 도착할 수 있다면 최단거리 반환(값이 1인 칸으로만 이동가능)
// 도착 불가능 하면 -1 반환.