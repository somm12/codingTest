#include <vector>
#include <map>
#include <cmath>
using namespace std;

int solution(vector<int> nums)
{
    map<int,int> p;
    
    int answer = 0;
    
    for (int i = 0; i< nums.size(); i++) {
        p[nums[i]] = 1;
    }

    answer = min(p.size(),nums.size()/2);
    return answer;
}
//플그머 c++ 고득점 kit 문제