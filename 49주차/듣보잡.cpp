#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);


    int N;
    int M;
    vector <string> arr;

    cin >> N >> M;
    map<string,int> p;
    for (int i = 0; i < N;i++){
        string a;
        cin >> a;
        p[a]++;
        
    }
    for (int i = 0; i < M; i++){
        string a;
        cin >> a;
        if (p[a] > 0) {
            arr.push_back(a);
        }

    }
    sort(arr.begin(),arr.end());
    cout << arr.size() << '\n';
    for (int i = 0; i < arr.size();i++){
        cout << arr[i] << '\n';
    }
    return 0;
}
