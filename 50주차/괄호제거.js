const combi = (arr, dataArr) => {
  // 괄호 쌍 인덱스를 담을 배열, 원본 문자열
  let res = new Set(); // 서로 다른 식을 출력하므로, set사용.

  const comb = (L, start, tmp) => {
    res.add(tmp.join(""));
    if (L === arr.length) {
      return;
    }
    for (let i = start; i < arr.length; i++) {
      let copied = [...tmp];
      copied[arr[i][0]] = ""; // 괄호 쌍 끼리 없애기!
      copied[arr[i][1]] = "";
      comb(L + 1, i + 1, copied);
    }
  };
  comb(0, 0, [...dataArr]);
  res = [...res];
  res.shift(); // 맨앞 제거.

  return res;
};

const solution = (data) => {
  let pair = [];
  let answer = [];
  data = [...data];
  let stack = [];

  data.forEach((v, i) => {
    // 괄호쌍 끼리 인덱스 묶어서 만들기.
    if (v === "(") {
      stack.push(i);
    } else if (v === ")") {
      const prev = stack.pop();
      pair.push([prev, i]);
    }
  });

  answer = combi(pair, data); // 조합을 통해서 모든 제거 경우를 만든다.

  answer.sort();
  answer.forEach((v) => console.log(v));
};
// 입력 처리 부분.
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = null;
rl.on("line", (line) => {
  if (!data) {
    data = line;
    rl.close();
  }
}).on("close", () => {
  solution(data);
  process.exit();
});
// 입력 처리 부분.

// 백준 자료구조 문제
