function solution(a) {
  let answer = 0;
  const m = new Map();
  for (const v of a) {
    if (m.has(v)) {
      m.set(v, m.get(v) + 1);
    } else {
      m.set(v, 1);
    }
  }
  const arr = [...m];
  arr.sort((a, b) => b[1] - a[1]); // 개수가 많은 것 부터.
  for (const [num, cnt] of arr) {
    let tmp = 0;
    for (let i = 0; i < a.length - 1; i++) {
      if (answer >= cnt) break; // 이미 개수가 더 많으면 더이상 실행하지 않음.
      if (a[i] !== num && a[i + 1] !== num) continue; // 하나라도 값이 Num이며,
      if (a[i] === a[i + 1]) continue; // 두 개의 값이 서로 다르다면, 체크하고 넘어가기.
      i += 1; // 다다음 부분 부터 체크( i,i+1 끼리 확인하므로)
      tmp += 1; // 조건에 맞는 수열 쌍 1개 증가.
    }
    answer = Math.max(tmp, answer);
  }
  return answer * 2; // 지금 까지 쌍의 개수를 체크한 것이므로 2배를 해준다.
}
