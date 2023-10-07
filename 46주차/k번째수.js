function solution(array, commands) {
  var answer = [];
  for (let i = 0; i < commands.length; i++) {
    const [s, e, k] = commands[i];
    let arr = array.slice(s - 1, e);
    arr.sort((a, b) => a - b);
    console.log(arr);
    answer.push(arr[k - 1]);
  }
  return answer;
}
// 플그머 정렬 문제
