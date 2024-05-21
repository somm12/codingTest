const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = () => {
  let tmp = new Map();
  let [f, b] = ["", ""];
  for (const v of s) {
    if (tmp.has(v)) {
      tmp.set(v, tmp.get(v) + 1);
    } else tmp.set(v, 1);
  }
  let cnt = 0;
  for (const [k, v] of tmp) {
    if (v % 2 == 1) cnt += 1;
  }
  if (cnt > 1) {
    console.log("I'm Sorry Hansoo");
    return;
  }
  tmp = [...tmp];
  tmp.sort((a, b) => {
    return a[0] > b[0] ? 1 : -1; // 사전순. 정렬
  });
  let odd = false; // 홀수개 알파벳이 있는지 체크.
  let a = ""; // 해당 홀수개 알파벳 담기.
  for (const [st, ct] of tmp) {
    const times = st.repeat(parseInt(ct / 2));
    if (ct % 2 == 0) {
      f += times; // 앞
      b = times + b; // 가운데 기준 뒤쪽 부분. 펠린드롬을 만들기 위해 앞에 문자열 추가.
    } else {
      odd = true;
      a = st;
      f += times;
      b = times + b;
    }
  }

  if (odd) f += a; // 홀수개 알파벳이 있다면, 추가.

  console.log(f + b);
};

let s = null;
rl.on("line", (line) => {
  if (!s) {
    s = line;
    rl.close();
  }
});
rl.on("close", () => {
  solution();
  process.exit();
});
// 펠린드롬 만들기.
