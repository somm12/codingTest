const solution = (str1, str2) => {
  const leng1 = str1.length;
  const leng2 = str2.length;

  let arr = Array(leng1 + 1)
    .fill()
    .map((e) => Array(leng2 + 1).fill(0));

  for (let i = 1; i <= leng1; i++) {
    for (let j = 1; j <= leng2; j++) {
      if (str1[i - 1] == str2[j - 1]) {
        // 값이 같으면 이전 단계까지 비교에서 +1
        arr[i][j] = arr[i - 1][j - 1] + 1;
      } else {
        // 다르면 이전까지 비교 한 것 중에서 더 큰 것.
        arr[i][j] = Math.max(arr[i - 1][j], arr[i][j - 1]);
      }
    }
  }
  console.log(arr[leng1][leng2]);

  return;
};

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let str1 = null;
let str2 = null;

rl.on("line", function (line) {
  if (!str1) {
    str1 = line;
  } else {
    str2 = line;
    rl.close();
  }
}).on("close", () => {
  solution(str1, str2);
  process.exit();
});
// 백준 LCS문제
