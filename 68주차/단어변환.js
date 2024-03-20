function solution(begin, target, words) {
  var answer = 50;
  const check = (a, b) => {
    // 한번에 한개만 바꾸기 가능이므로, 확인해주는 함수.
    let cnt = 0;
    for (let i = 0; i < a.length; i++) {
      if (a[i] !== b[i]) cnt += 1;
    }
    return cnt === 1;
  };
  const n = words.length;
  const visited = Array(n).fill(0);
  const dfs = (L, now) => {
    if (answer <= L) return; // 이미 더 짧은 단계가 있다면 멈추기.
    if (now == target) {
      answer = Math.min(answer, L);
      return;
    }
    for (let i = 0; i < n; i++) {
      if (!visited[i] && check(words[i], now)) {
        visited[i] = 1;
        dfs(L + 1, words[i]);
        visited[i] = 0;
      }
    }
  };
  dfs(0, begin);
  answer = answer == 50 ? 0 : answer; // target으로 변환할 수 없다면 0 반환.
  return answer;
}
