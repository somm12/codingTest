#include<string>
#include <iostream>

using namespace std;

bool solution(string s)
{
    bool answer = true;
    int cnt = 0;
    for (int i =0;i < s.size(); i++){
        if (s[i] == ')'){
            cnt -= 1;
            if (cnt < 0) return false;
        }
        else {
            cnt += 1;
        }
    }

    return cnt==0;
}