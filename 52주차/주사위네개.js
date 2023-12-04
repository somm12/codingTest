const solution = () => {
  let answer = [];

  data.forEach((arr) => {
    let result = {};
    arr.forEach((v) => {
      if (v in result) result[v] += 1;
      else result[v] = 1;
    });
    const tmp = Object.keys(result);

    if (tmp.length === 1) {
      // 모두 같은 눈.
      let m = tmp[0];
      answer.push(50000 + m * 5000);
    } else if (tmp.length === 2) {
      //2개 씩 두쌍 나온 경우
      let pair = false;
      for (let k in result) {
        if (result[k] === 2) {
          pair = true;

          answer.push(2000 + tmp[0] * 500 + tmp[1] * 500);
          break;
        }
      }
      // 3개 1개 나온 경우
      if (!pair) {
        let m = result[tmp[0]] === 3 ? tmp[0] : tmp[1];
        answer.push(10000 + m * 1000);
      }
    } else if (tmp.length === 3) {
      // 2개, 1개, 1개 나온 경우
      let m;
      for (let k in result) {
        if (result[k] === 2) m = k;
      }
      answer.push(1000 + m * 100);
    } else {
      // 전부 다른 경우.

      const maxV = Math.max(...tmp);

      answer.push(maxV * 100);
    }
  });
  console.log(Math.max(...answer));
};
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let n = null;
let cnt = 0;
let data = [];
rl.on("line", (line) => {
  if (!n) {
    n = +line;
  } else {
    data.push(line.split(" ").map((e) => +e));
    cnt += 1;
  }
  if (cnt === n) rl.close();
}).on("close", () => {
  solution();
  process.exit();
});
// 백준
