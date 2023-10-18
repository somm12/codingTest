function solution(arr) {
  var s = [];
  for (let v of arr) {
    if (s.length === 0) s.push(v);
    // 빈 배열 일때,
    else {
      if (s[s.length - 1] !== v) s.push(v);
    }
  }

  return s;
}
// c++ 코드
// #include <vector>
// #include <iostream>

// using namespace std;

// vector<int> solution(vector<int> arr)
// {
//     vector<int> answer;
//     for (int i = 0; i < arr.size(); i++) {
//         if (answer.size()==0) answer.push_back(arr[i]);
//         else {
//             if (answer[answer.size()-1] != arr[i])
//                 answer.push_back(arr[i]);
//         }
//     }

//     return answer;
// }
