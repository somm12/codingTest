function solution(s) {
  var answer = [];
  s.forEach((v) => {
    const stack = [];
    const st2 = [];
    const arr = [];
    for (let i = 0; i < v.length; i++) {
      //110 찾기.
      stack.push(v[i]);
      if (stack.length >= 3) {
        if (
          stack[stack.length - 1] === "0" &&
          stack[stack.length - 2] === "1" &&
          stack[stack.length - 3] === "1"
        ) {
          stack.pop();
          stack.pop();
          stack.pop();
          arr.push("110");
        }
      }
    }
    // 최대한 0이 앞으로 오도록하기. => 가장 뒤의 0찾기.
    while (stack.length) {
      const e = stack.length - 1;
      if (stack[e] === "0") {
        break;
      } else {
        st2.push(stack.pop());
      }
    }

    const result = stack.join("") + arr.join("") + st2.join("");
    answer.push(result);
  });

  return answer;
}

//----------- 함수로 쪼개기.
const check = (arr) => {
  const n = arr.length;
  if (n < 3) return false;
  if (arr[n - 1] === "0" && arr[n - 2] === "1" && arr[n - 3] === "1") {
    return true;
  }
  return false;
};

const find110 = (v) => {
  const stack = [];
  let cnt = 1;
  for (let i = 0; i < v.length; i++) {
    //110 찾기.
    stack.push(v[i]);
    if (check(stack)) {
      stack.pop();
      stack.pop();
      stack.pop();
      cnt += 1; //110 개수세기
    }
  }
  return [stack.join(""), cnt];
};
function solution2(s) {
  var answer = [];
  s.forEach((v) => {
    const [remain, cnt] = find110(v);

    // 최대한 0이 앞으로 오도록하기. => 가장 뒤의 0찾기.
    const idx = remain.lastIndexOf("0");
    let result;
    if (idx === -1) {
      result = "110".repeat(cnt) + remain;
    } else {
      result =
        remain.substring(0, idx + 1) +
        "110".repeat(cnt) +
        remain.substring(idx + 1);
    }

    answer.push(result);
  });

  return answer;

  return answer;
}
