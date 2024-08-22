const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = () => {
  let s = 0;
  let e = 0;
  const cnt = Array(10 * 10000 + 1).fill(0);
  let answer = 0;
  while (e < n) {
    if (cnt[arr[e]] == 0) {
      // 현재 e번째 숫자 개수가 0개면 증가시켜서 수열에 포함시킨다.
      // 새로운 수면 증가시키기.
      cnt[arr[e]] += 1;
      e += 1;
    } else {
      // 중복이 생기게 된다면, 이미 숫자를 세었다면, 개수를 더하고, s 번째 숫자의 개수를 -1, s +=1 한다.(중복이 없을 때 까지.)
      answer += e - s;
      cnt[arr[s]] -= 1;
      s += 1;
    }
  }

  answer += ((e - s) * (e - s + 1)) / 2; // 마지막 수열은 전체 부분집합 개수인 n*n+1/2로 구하기.
  console.log(answer);
};
let n = null;
let arr = null;

rl.on("line", (line) => {
  if (!n) n = +line;
  else {
    arr = line.split(" ").map((e) => +e);
    rl.close();
  }
});
rl.on("close", () => {
  solution();
  process.exit();
});
// 백준List of Unique Numbers
