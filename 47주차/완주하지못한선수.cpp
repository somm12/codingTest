#include <string>
#include <vector>
#include <map>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    map<string,int> p;
    int n = participant.size();
    for (int i = 0; i < n; i++) {
        string name = participant[i];
        if (p.find(name) == p.end()) p[name] = 1;
        else p[name] += 1;
    }
    
    for (int i = 0; i < n-1; i++) {
        string name = completion[i];
        p[name] -= 1;
    }
    
    for (int i = 0; i < n; i++) {
        string name = participant[i];
        if (p[name] == 1) return name;
    }
    
    return answer;
}// 플그머 문제 - 해시