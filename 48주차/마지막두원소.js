function solution(num_list) {
  var answer = [];
  let length = num_list.length;
  const prev = num_list[length - 2];
  const last = num_list[length - 1];
  if (last > prev) answer = [...num_list, last - prev];
  else answer = [...num_list, last * 2];
  return answer;
}
// 프로그래머스.
