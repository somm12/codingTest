#include <string>
#include <vector>
#include<algorithm>
#include<cmath>
using namespace std;

int solution(vector<int> citations) {
    int answer = 0;
    int n = citations.size();
    sort(citations.begin(),citations.end());
    int maxV = citations[n-1];
    for (int i = maxV; i >= 0; i--){
        int h = i;
        int cnt = 0;
        for (int j = n-1; j >= 0;j--){
            if (citations[j]>=h) cnt += 1;
        }
        if (cnt >= h) answer = max(answer,h);
    }
    
    return answer;
}// 플그머 정렬 파트. c++로 풀기