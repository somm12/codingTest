function solution(begin, target, words) {
  var answer = 50;
  //변환이 안된다면 0 반환.
  let visited = {};
  for (let w of words) visited[w] = 0;
  function dfs(L, now) {
    if (now === target) {
      answer = Math.min(answer, L);
      return;
    }
    for (let w of words) {
      let cnt = 0;
      for (let i = 0; i < w.length; i++) {
        if (w[i] !== now[i]) cnt += 1;
      }
      if (cnt === 1 && visited[w] === 0) {
        visited[w] = 1;
        dfs(L + 1, w);
        visited[w] = 0;
      }
    }
  }
  dfs(0, begin);
  return answer === 50 ? 0 : answer;
}
// 한글자만 다른 방향으로 뻗어나가기. 최소 거칠 수 있는 단계 구하기
// 프로그래머스 dfs
