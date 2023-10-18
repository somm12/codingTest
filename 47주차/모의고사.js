function solution(answers) {
  var answer = [];
  let a = [1, 2, 3, 4, 5];
  let b = [2, 1, 2, 3, 2, 4, 2, 5];
  let c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
  let arr = [0, 0, 0];
  for (let i = 0; i < answers.length; i++) {
    if (answers[i] === a[i % 5]) arr[0] += 1;
    if (answers[i] === b[i % 8]) arr[1] += 1;
    if (answers[i] === c[i % 10]) arr[2] += 1;
  }
  let maxV = Math.max(...arr);

  for (let i = 0; i < arr.length; i++) {
    if (maxV === arr[i]) answer.push(i + 1);
  }

  return answer;
} // 플그머 완전탐색.
// c++
// #include <string>
// #include <vector>
// #include <cmath>
// #include <iostream>

// using namespace std;

// vector<int> solution(vector<int> answers) {
//     vector<int> answer;
//     vector<int> arr(3);
//     int a[] = {1,2,3,4,5};
//     int b[] = {2,1,2,3,2,4,2,5};
//     int c[] = {3,3,1,1,2,2,4,4,5,5};

//     for (int i = 0; i < answers.size(); i++){
//         if (answers[i] == a[i%5]) arr[0] +=1;
//         if (answers[i] == b[i%8]) arr[1] +=1;
//         if (answers[i] == c[i%10]) arr[2] +=1;

//     }
//     int maxV = -1;
//     for (int v:arr) {

//         maxV = max(maxV,v);
//     }

//     for (int i = 0; i < arr.size(); i++){
//         if (maxV == arr[i]) answer.push_back(i+1);
//     }
//     return answer;
// }
