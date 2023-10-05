function solution(nums) {
  let dict = {};
  for (var v of nums) {
    if (v in dict) dict[v] += 1;
    else dict[v] = 0;
  }

  return Math.min(Object.keys(dict).length, nums.length / 2);
}
// 방법2
function sol(nums) {
  var answer = 0;
  let a = new Set(nums);
  console.log(a);
  console.log(nums.length / 2);
  answer = Math.min(a.size, nums.length / 2);

  return answer;
}
// 플그머 해시 문제
