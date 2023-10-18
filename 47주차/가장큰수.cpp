#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(const string &a, const string &b){// 610, 106중 610이 더 크므로, 더 앞으로 정렬 이란뜻
    return (b+a < a+b) ;

}

string solution(vector<int> numbers) {
    string answer = "";
    vector<string> s;
    for (int num:numbers){
        s.push_back(to_string(num));
    };
    sort(s.begin(),s.end(),compare);
    
    for (string v: s){
        answer += v;
    }
    if (answer[0] == '0')//만약 [0,0,0,,] 와 같은 배열이라면 0.
        answer = "0";
    return answer;
}