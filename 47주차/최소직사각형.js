function solution(sizes) {
  var answer = 0;
  let maxW = 0;
  let maxH = 0;
  for (let v of sizes) {
    v.sort((a, b) => a - b);
    maxW = Math.max(maxW, v[0]);
    maxH = Math.max(maxH, v[1]);
  }
  return maxW * maxH;
}

//c ++
// #include <string>
// #include <vector>
// #include <algorithm>
// #include <cmath>
// using namespace std;

// int solution(vector<vector<int>> sizes) {
//     int answer = 0;
//     int maxW = 0;
//     int maxH = 0;
//     for (int i= 0; i < sizes.size();i++) {

//         sort(sizes[i].begin(),sizes[i].end(), less<>());
//         maxW = max(maxW, sizes[i][0]);
//         maxH = max(maxH, sizes[i][1]);

//     }
//     return maxW*maxH;
// }
