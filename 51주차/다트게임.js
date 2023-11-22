function solution(dartResult) {
  var answer = [];
  let dict = { S: 1, D: 2, T: 3 };
  dartResult = dartResult.replaceAll("10", "A");
  let arr = [];
  let n = dartResult.length;

  let tmp = dartResult[0];
  for (let i = 1; i < n; i++) {
    const v = dartResult[i];

    if (!isNaN(v) || v === "A") {
      //숫자면
      arr.push(tmp);
      tmp = v;
    } else tmp += v;
  }
  arr.push(tmp); //마지막도 넣기, => [1S, 2D*,3T] 나눠짐.
  console.log(arr);
  arr.forEach((s, i) => {
    let num = s[0] === "A" ? 10 : parseInt(s[0]);

    num = num ** dict[s[1]]; // 제곱.
    if (s.length === 3) {
      //옵션 존재
      if (s[2] === "*") {
        if (answer.length > 0) {
          // 이전과 해당 점수 2배.
          answer[i - 1] *= 2;
          num *= 2;
        } else num *= 2;
      } else num *= -1; //#일때.
    }
    answer.push(num);
  });
  answer = answer.reduce((acc, v) => {
    return (acc += v);
  }, 0);

  return answer;
}

// 더 쉬운 풀이
// 각 숫자에 따라서 값을 계산 하면 되므로, 어떤 문자가 나오느냐에 따라서 마지막 answer에 넣은 숫자가 가장 최근
// 숫자이므로 연속해서 계산하는 방식
function solution(dartResult) {
  var answer = [];
  let dict = { S: 1, D: 2, T: 3 };
  dartResult = dartResult.replaceAll("10", "A");
  for (let s of dartResult) {
    let n = answer.length;
    if (s === "A") answer.push(10);
    else if (!isNaN(s)) {
      answer.push(parseInt(s));
    } else if (s in dict) {
      answer[n - 1] = answer[n - 1] ** dict[s];
    } else if (s === "*") {
      if (answer.length > 0) {
        answer[n - 2] *= 2;
        answer[n - 1] *= 2;
      } else answer[n - 1] *= 2;
    } else answer[n - 1] *= -1;
  }
  answer = answer.reduce((acc, v) => {
    return (acc += v);
  }, 0);

  return answer;
}
