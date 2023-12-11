const solution = () => {
  const dfs = (t) => {
    if (t.length === S.length) {
      if (t === S) {
        console.log(1);
        process.exit();
      }

      return;
    }
    // 마지막 문자가 A면 A를 추가한 경우이므로, A제거.
    if (t[t.length - 1] === "A") dfs(t.slice(0, t.length - 1));
    // 맨 앞 문자가 B면 B를 추가하고 뒤집은 경우이므로, 맨앞 B제거 하고 뒤집은 채로 dfs
    if (t[0] === "B") dfs(t.slice(1, t.length).split("").reverse().join(""));
  };
  dfs(T);
  console.log(0);
};

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let S = null;
let T = null;

rl.on("line", (line) => {
  if (!S) {
    S = line;
  } else if (!T) {
    T = line;
    rl.close();
  }
}).on("close", () => {
  solution();
  process.exit();
});
// 백준 문제
// T -> S로 만드는 방식으로 불필요한 경우를 제거하는 방식으로 dfs수행.
// S -> T로 만들면 시간 초과 가능.
