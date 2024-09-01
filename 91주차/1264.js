const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const arr = ["a", "e", "i", "o", "u"];
const dict = new Set([...arr]);

rl.on("line", (line) => {
  const v = line;
  if (v == "#") rl.close();
  else {
    let answer = 0;
    for (const str of v) {
      if (dict.has(str.toLowerCase())) answer += 1;
    }
    console.log(answer);
  }
});

rl.on("close", () => {
  process.exit();
});
// 백준 모음의 개수.
