function solution(s, skip, index) {
  var answer = "";
  const filtered = [];
  let alpha = 97;
  const arr = new Array(26).fill(0);
  arr.forEach((v) => {
    const str = String.fromCharCode(alpha);
    if (!skip.includes(str)) filtered.push(str);
    alpha += 1;
  });

  const strArr = [...s];
  strArr.forEach((v) => {
    const idx = filtered.findIndex((value) => value === v);
    const targetIdx = (idx + index) % filtered.length;
    answer += filtered[targetIdx];
  });

  return answer;
}
// 프로그래머스 둘만의 암호
