#include <bits/stdc++.h>
using namespace std;
int n = 9;
int r = 7;
int a[9];
void check(){
    int sum = 0;
    for (int i = 0; i < r;i++){
        sum += a[i];
    }
    if( sum == 100){
        sort(a,a+7);
        for (int i =0; i< r;i++){
            cout << a[i] << "\n";
        }

        exit(0);
    }
}
void makePermutation(int depth){
    if (depth == r){
        check();
        return;
    }
    for (int i = depth; i < n;i++){
        swap(a[i],a[depth]);
        makePermutation(depth+1);
        swap(a[i],a[depth]);
    }

}
int main(){
    
    for (int i=0;i<n;i++){
        cin >> a[i];
    }

    makePermutation(0);

    return 0;
}