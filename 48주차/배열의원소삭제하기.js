function solution(arr, delete_list) {
  var answer = [];
  answer = arr.filter((v, idx) => !delete_list.includes(v));
  return answer;
}
// delete_list에 있는 원소는 arr에서 다 삭제.
// 프로그래머스.
