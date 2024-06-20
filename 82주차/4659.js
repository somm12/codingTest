const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const check = (s) => {
  const vowel = new Set(["a", "e", "i", "o", "u"]);
  let flag = true;
  let isVowel = false;
  // 모음 하나는 포함하는가.
  let [vCnt, lCnt] = [0, 0];
  for (let i = 0; i < s.length; i++) {
    if (vowel.has(s[i])) {
      vCnt += 1;
      lCnt = 0;
      isVowel = true;
    } else {
      lCnt += 1;
      vCnt = 0;
    }
    if (vCnt == 3 || lCnt == 3) flag = false; // 모음이나 자음이 연속 3개면 false.
    if (i >= 1 && s[i - 1] == s[i] && s[i] !== "e" && s[i] !== "o")
      flag = false;
  }
  if (!isVowel) flag = false;
  if (flag) {
    console.log(`<${s}> is acceptable.`);
  } else {
    console.log(`<${s}> is not acceptable.`);
  }
};
rl.on("line", (line) => {
  if (line === "end") rl.close();
  else check(line);
});
rl.on("close", () => {
  process.exit();
});
// 백준 비밀번호 발음하기.
