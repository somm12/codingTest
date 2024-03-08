function solution(priorities, location) {
  let answer = 1;
  const arr = priorities.map((v, i) => ({ p: v, idx: i }));

  while (arr.length > 0) {
    const tmp = arr.shift();
    if (arr.some((value) => value.p > tmp.p)) {
      // 하나라도 우선순위가 더 높은 것이 있다면. 다시 큐에 넣기.
      arr.push(tmp);
    } else {
      if (tmp.idx === location) return answer; // 현재 처리되는 프로세스가 찾고자하는 프로세스라면 반환.
      answer += 1;
    }
  }
}
