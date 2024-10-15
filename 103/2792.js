const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const search = (num) => {
  // num개씩 나누어 줘도 학생들에게 줄 수 있는지 (단, 못 받는 학생있어도 됨. 그리고 학생은 같은 색상만 가져야함)
  let ret = 0;
  for (const v of arr) {
    ret += parseInt(v / num); // v개를 가진 색상은 num개씩 나누었을 때, 몇 명에게 나누어 줄 수 있는가.
    if (v % num) ret += 1; // 나머지가 있을 때 한 사람에게 또 나눠 줄 수 있음.
  }
  return ret <= n; // 나눠 줄 수 있는 덩어리가 n개 이하라면, 모두가 1가지 색상을 가질 수 있는 것으로 충족되어 true 반환.
};
const solution = () => {
  arr.sort((a, b) => a - b);
  let s = 0;
  let e = arr[arr.length - 1]; // 가장 큰 값. 보석 개수 큰 것.
  let answer = Infinity;
  while (s <= e) {
    const mid = parseInt((s + e) / 2);
    if (search(mid)) {
      // 나눠줄 수 있는 경우라면, 업데이트
      answer = Math.min(answer, mid); // 가장 많이 가진 보석개수인 질투심 최소로 만들기.
      e = mid - 1; // 더 최소가 가능할 수 있으므로 작은 범위로 좁히기.
    } else {
      s = mid + 1; // 조건에 안맞으면 개수량 늘리기(질투심)
    }
  }
  console.log(answer);
};
let [n, m] = [null, null];
const arr = [];
let cnt = 0;
rl.on("line", (line) => {
  if (!n) {
    [n, m] = line.split(" ").map((e) => +e);
  } else {
    if (cnt < m) {
      arr.push(+line);
      cnt += 1;
    }
    if (cnt === m) {
      rl.close();
    }
  }
});

rl.on("close", () => {
  solution();
});
// 백준 보석 상자 문제.
