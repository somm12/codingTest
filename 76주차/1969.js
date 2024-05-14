const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function sortAlphabetically(a, b) {
  // sort에서 비교함수 쓸 때, 알파벳 정렬은 따로 함수를 만들어야한다.
  if (a < b) return -1;
  if (a > b) return 1;
  return 0;
}

const solution = () => {
  let answer = "";
  for (let i = 0; i < M; i++) {
    let tmp = new Map();
    for (const s of arr) {
      if (tmp.has(s[i])) tmp.set(s[i], tmp.get(s[i]) + 1);
      else tmp.set(s[i], 1);
    }
    tmp = [...tmp];
    tmp.sort((a, b) => {
      if (a[1] !== b[1]) return b[1] - a[1]; // 개수가 더 많은 것먼저
      return sortAlphabetically(a[0], b[0]); // 알파벳 사전순
    });

    answer += tmp[0][0]; // HD가 최소가 되려면 가장 많이 나온 유전자를 선택하는 것.
  }

  let count = 0;
  for (let s of arr) {
    for (let i = 0; i < M; i++) {
      if (s[i] !== answer[i]) count += 1;
    }
  }

  console.log(answer);
  console.log(count);
};
let N;
let M;
let arr = [];
let cnt = 0;

rl.on("line", (line) => {
  if (!N) {
    [N, M] = line.split(" ").map((e) => +e);
  } else {
    arr.push(line);
    cnt += 1;
    if (cnt == N) rl.close();
  }
});

rl.on("close", () => {
  solution();
  process.exit();
});
//백준 DNA
