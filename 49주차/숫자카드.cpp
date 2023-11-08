#include <iostream>
#include <map>

using namespace std;
int main(){
    ios_base::sync_with_stdio(false);// cin, cout 속도 높이기
    cin.tie(0);

    
    int N;
    cin >> N;
    map<int,int> p;
    for (int i = 0; i < N;i++){
        int a;
        cin >> a;
        p[a]++;
        
    }
    int M;
    cin >> M;
    for (int i = 0; i < M; i++){
        int a;
        cin >> a;
        cout << p[a] << ' ';
    }
    return 0;
}

// 풀이2
    vector<int> v;
    int n, m;
 
    cin >> n;
    int num;
    for (int i = 0; i < n; i++)
    {
        cin >> num;
        v.push_back(num);
    }
 
    sort(v.begin(), v.end());
 
    cin >> m;
    for (int i = 0; i < m; i++)// 이분탐색 방법.
    {
        cin >> num;
        cout << upper_bound(v.begin(), v.end(), num) - lower_bound(v.begin(), v.end(), num) << ' ';
    }