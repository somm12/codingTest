#include <bits/stdc++.h>
using namespace std;
int a, b,c;
int t[101];// 최대 100분 이므로, 각 시각일 때 몇대가 주차되었는지 저장.
int  main(){
    cin >> a >> b >> c;
    for (int i =0; i < 3;i++){
        int x,y;
        cin >> x >> y;
        for (int j=x;j < y;j++){// x분에 입차. y분에 출차 이므로 y분은 포함X.
            t[j]++;
        }
    }
    int answer =0;
    for (int i =0;i<100;i++){//1대일 때는 a원,2대는 b,c대는 c원.
        if (t[i]== 1) answer += (t[i]*a);
        else if (t[i]==2) answer += (t[i]*b);
        else if (t[i]==3) answer += (t[i]*c);
    }
    cout << answer;
    return 0;
}
// 백준 트럭 주차.