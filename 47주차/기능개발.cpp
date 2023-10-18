#include <string>
#include <vector>
#include <cmath>
#include <deque>
#include<iostream>
using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    deque<int> q;
    for (int i =0; i< progresses.size(); i++){
        
        q.push_back(ceil( (float)(100-progresses[i]) / (float) speeds[i]));
    } 
   
    int prev = q.front();
    int cnt = 0;
  
    while (!q.empty()) {
        int now = q.front();
        q.pop_front();
        if (prev >= now) cnt += 1;
        else {
            answer.push_back(cnt);
            cnt = 1;
            prev = now;
        }
    }
    answer.push_back(cnt);
    return answer;
}// 플그머 c++로 풀어보기. ** c++은 두 숫자 중에 하나는 실수여야 나누기에서 소수점이 나옴.
// 따라서 형변환 필수.