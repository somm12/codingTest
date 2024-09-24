function solution(k, dungeons) {
  var answer = 0;
  const n = dungeons.length;
  const visited = Array(n).fill(0);

  const dfs = (now, L) => {
    answer = Math.max(answer, L);
    for (let i = 0; i < n; i++) {
      if (!visited[i] && now >= dungeons[i][0]) {
        visited[i] = 1;
        dfs(now - dungeons[i][1], L + 1);
        visited[i] = 0;
      }
    }
  };
  dfs(k, 0);
  return answer;
}
// 프로그래머스 문제 피로도.js
