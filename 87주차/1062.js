const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = () => {
  const init = ["a", "n", "t", "i", "c"];
  const initIdx = [];
  let start = 0;
  for (const v of init) {
    initIdx.push(v.charCodeAt() - 97);
    start += 1 << (v.charCodeAt() - 97);
  }
  let answer = 0;

  for (let i = start; i < 1 << 26; i++) {
    let cnt = 0;
    let flag = true;
    for (const j of initIdx) {
      if (i & (1 << j)) continue;
      else flag = false;
    }

    if (!flag) continue;

    for (let j = 0; j < 26; j++) {
      if (i & (1 << j)) cnt += 1;
    }
    let total = 0;
    if (cnt == k) {
      for (const value of num) {
        if ((value & i) >= value) {
          total += 1;
        }
      }
      answer = Math.max(answer, total);
    }
  }
  console.log(answer);
};

let [n, k] = [null, null];
let arr = [];
const num = [];
let cnt = 0;
rl.on("line", (line) => {
  if (!n) [n, k] = line.split(" ").map((e) => +e);
  else {
    arr.push(line);
    cnt += 1;
    if (cnt == n) rl.close();
  }
});
rl.on("close", () => {
  for (const word of arr) {
    // 단어를 숫자로 바꿔주기.
    let tmp = 0;
    for (const v of word) {
      tmp |= 1 << (v.charCodeAt() - 97);
    }
    num.push(tmp);
  }
  solution2();
  process.exit();
});

// 또 다른 풀이

const counting = (mask) => {
  let cnt = 0;

  for (const word of num) {
    if ((word & mask) == word) {
      // and연산 후에 단어와 같다면! 세기.
      cnt += 1;
    }
  }

  return cnt;
};

const solution2 = () => {
  const dfs = (index, check, mask) => {
    // 깊이, 해당 문자를 포함함 여부 체크, 지금까지의 문자 포함 비트 마스킹.
    if (check > k) return 0; // K개 고르기 끝! k개까지는 couting을 해봐야 하므로, k 보다 크면 return.
    if (index == 26) return counting(mask); // 26개 알파벳 조합 끝!
    let answer = dfs(index + 1, check + 1, mask | (1 << index)); //현재 Index 글자는 포함한다.

    if (
      //  단 ,!!! a,n,t,i,c는 꼭 포함 필수.
      index !== "a".charCodeAt() - 97 &&
      index !== "n".charCodeAt() - 97 &&
      index !== "t".charCodeAt() - 97 &&
      index !== "i".charCodeAt() - 97 &&
      index !== "c".charCodeAt() - 97
    ) {
      //현재 Index글자는 포함 하지 않는다.
      answer = Math.max(answer, dfs(index + 1, check, mask));
    }
    return answer;
  };

  console.log(dfs(0, 0, 0));
};
// 백준 가르침 문제. 비트마스킹 , 완탐 활용
