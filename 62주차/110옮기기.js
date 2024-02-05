function solution(s) {
  var answer = [];
  const check = (arr) => {
    // 110 있는지 체크
    if (arr.length < 3) return false;
    const len = arr.length;
    if (arr[len - 1] === "0" && arr[len - 2] === "1" && arr[len - 3] === "1") {
      return true;
    }
    return false;
  };

  const find110 = (str) => {
    let cnt = 0;
    let stack = [];
    str = [...str];
    for (let i = 0; i < str.length; i++) {
      stack.push(str[i]);
      if (check(stack)) {
        stack.pop();
        stack.pop();
        stack.pop();
        cnt += 1;
      }
    }
    return [stack.join(""), cnt]; // 남은 문자열, 110 개수.
  };

  for (let tmp of s) {
    let [remain, cnt] = find110(tmp);
    let idx = remain.lastIndexOf("0"); // 가장 작은 문자열을 만드려면, 0을 되도록 앞으로 보내야함. 따라서 가장 뒤에 있는 0 뒤에 110을 넣음.
    const target = "110";
    if (remain.length === 0) {
      // 빈문자열이 남았다면, 110 반복.
      answer.push(target.repeat(cnt));
      continue;
    }
    if (idx === -1) {
      // 110이 없다면 앞에 추가.
      remain = target.repeat(cnt) + remain;
    } // 110을 추가해도 가장 뒤의 0은 추가한 110 바로 뒤 이므로, 110 개수 만큼 추가하기
    else
      remain =
        remain.substring(0, idx + 1) +
        target.repeat(cnt) +
        remain.substring(idx + 1);

    answer.push(remain);
  }

  return answer;
}
// 프로그래머스 110옮기기
