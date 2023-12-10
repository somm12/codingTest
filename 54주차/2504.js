const solution = () => {
  const stack = [];
  let answer = 0;
  const check = (tmp) => {
    let stack = [];
    for (let v of tmp) {
      let last = stack.length - 1;
      if (v === "(" || v === "[") {
        stack.push(v);
      } else {
        if (stack.length === 0) return false;
        if (v === ")") {
          if (stack[last] === "(") stack.pop();
        } else {
          // 닫는 대괄호 일때. 맨 위 문자가 여는 괄호라면 pop
          if (stack[last] === "[") stack.pop();
        }
      }
    }
    return stack.length === 0 ? true : false;
  };
  if (!check(s)) {
    console.log(0);
    return;
  }
  for (let v of s) {
    const last = stack.length - 1;
    if (v === "(" || v === "[") stack.push(v);
    else {
      // 닫는 괄호.
      if (v === ")") {
        if (stack[last] === "(") {
          stack.pop();
          stack.push(2);
        } else if (typeof stack[last] === "number") {
          let num = stack.pop();
          stack.pop();
          stack.push(num * 2);
        }
      } else {
        // 닫는 대괄호
        if (stack[last] === "[") {
          stack.pop();
          stack.push(3);
        } else if (typeof stack[last] === "number") {
          let num = stack.pop();
          stack.pop();
          stack.push(num * 3);
        }
      }

      // 마지막 부분이 숫자라면,
      let total = 0;
      for (let i = stack.length - 1; i >= 0; i--) {
        if (typeof stack[i] === "number") {
          total += stack[i];
          stack.pop();
        } else break;
      }
      if (total > 0) stack.push(total);
    }
  }
  console.log(stack[0]);
};

const { type } = require("node:os");
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let s = null;

rl.on("line", (line) => {
  if (!s) {
    s = line;
    rl.close();
  }
}).on("close", () => {
  solution();
  process.exit();
});
// 백준 문제 다시 복습.
