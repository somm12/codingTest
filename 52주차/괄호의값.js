const isRight = (s) => {
  // 올바른 문자열인지 체크. 각 괄호의 쌍에 맞게 pop되는지 확인.
  const stack = [];
  for (let i = 0; i < s.length; i++) {
    if (s[i] === "(" || s[i] === "[") stack.push(s[i]);
    else {
      if (s[i] === ")") {
        if (stack.length === 0) return false;
        if (stack[stack.length - 1] === "(") stack.pop();
        else stack.push(s[i]);
      } else if (s[i] === "]") {
        if (stack.length === 0) return false;
        if (stack[stack.length - 1] === "[") stack.pop();
        else stack.push(s[i]);
      }
    }
  }

  return stack.length === 0 ? true : false;
};
const solution = (s) => {
  const stack = [];
  s = s.split("");
  if (!isRight(s)) {
    // 올바른 괄호인지 체크.
    console.log(0);
    return;
  }

  while (s.length > 0) {
    const v = s.shift();

    if (v === "(" || v === "[") stack.push(v);
    // 여는 괄호는 push
    else {
      //닫는 괄호
      const eIdx = stack.length - 1; // 스택의 맨 위 값 인덱스.
      if (v === ")") {
        if (stack[eIdx] === "(") {
          // () => 2
          stack.pop();
          stack.push(2);
        } else if (!isNaN(stack[eIdx]) && stack[eIdx - 1] === "(") {
          // (x) => x*2
          const tmp = stack.pop();
          stack.pop();
          stack.push(tmp * 2);
        }
      } else {
        if (stack[eIdx] === "[") {
          // [] => 3
          stack.pop();
          stack.push(3);
        } else if (!isNaN(stack[eIdx]) && stack[eIdx - 1] === "[") {
          // [x] => 3*x
          const tmp = stack.pop();
          stack.pop();
          stack.push(tmp * 3);
        }
      }
      // 스택안에 값이 2개 이상이며 가장 위의 두 값이 숫자라면 더해서 push
      while (
        // 2,3 => 5
        !isNaN(stack[stack.length - 1]) &&
        stack.length > 1 &&
        !isNaN(stack[stack.length - 2])
      ) {
        const a = stack.pop();
        const b = stack.pop();
        stack.push(a + b);
      }
    }
  }

  console.log(stack[0]);
};

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
  solution(s);
  process.exit();
});
//백준 구현 문제
