function solution(n, arr1, arr2) {
  var answer = [];

  for (let i = 0; i < n; i++) {
    let a = (arr1[i] | arr2[i]).toString(2).padStart(n, "0");
    // 지도를 합치고, 2진수로 바꾸고, 자리수 맞춰서 0 넣기.
    a = a.replaceAll("1", "#");
    a = a.replaceAll("0", " ");
    answer.push(a);
  }

  return answer;
}
// 2진수 바꾸기 메소드 toString(2)
// 문자열 자릿수 맞추기 padStart
// 프로그래머스
