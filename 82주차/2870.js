const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let arr = [];
let n = null;
let cnt = 0;

rl.on("line", (line) => {
  if (!n) n = +line;
  else {
    let tmp = "";
    for (const v of line) {
      const num = v.charCodeAt();
      if (97 <= num && num <= 122) {
        if (tmp.length > 0) {
          arr.push(BigInt(tmp));
          tmp = "";
        }
      } else tmp += v;
    }
    if (tmp.length > 0) arr.push(BigInt(tmp)); //최대 100자리수 이므로 BigInt 사용.
    cnt += 1;

    if (cnt == n) rl.close();
  }
});
rl.on("close", () => {
  arr.sort((a, b) => (a < b ? -1 : a > b ? 1 : 0)); // bigInt 자료형은 sort에서 a-b로 정렬 불가.
  console.log(arr.join("\n").trim()); // 끝에 공백 제거.
  process.exit();
});
