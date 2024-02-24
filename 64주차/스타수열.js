function solution(a) {
  let answer = 0;
  let info = new Map();
  for (const v of a) {
    if (info.has(v)) {
      info.set(v, info.get(v) + 1);
    } else {
      info.set(v, 1);
    }
  }
  info = [...info];
  info.sort((a, b) => b[1] - a[1]); // 개수가 많은 순으로 정렬.

  for (let [value, cnt] of info) {
    // 최대 cnt *2 만큼의 스타 수열을 만들 수 있음.
    if (answer >= cnt) continue; // 이미 answer가 그 이상으로 많으면 패스.
    let total = 0;
    for (let i = 0; i < a.length - 1; i++) {
      if (a[i] === a[i + 1]) continue; // 값이 다르고
      if (a[i] !== value && a[i + 1] !== value) continue; // value가 하나라도 있다면 개수 세기.
      total += 1;
      i += 1;
    }
    answer = Math.max(answer, total);
  }
  return answer * 2; // 개수*2 => 수열 길이
}
