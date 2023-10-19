function solution(k, dungeons) {
  var answer = -1;

  let n = dungeons.length;
  let visited = new Array(n).fill(0);

  function dfs(k, cnt) {
    //현재 남은 피로도, 최대 개수.
    answer = Math.max(answer, cnt);

    for (let i = 0; i < n; i++) {
      if (!visited[i] && k >= dungeons[i][0]) {
        // 남은 피로도가 필요필요도 이상이고, 방문 안했다면,
        visited[i] = 1;
        dfs(k - dungeons[i][1], cnt + 1);
        visited[i] = 0;
      }
    }
  }
  dfs(k, 0);

  return answer;
} // 프로그래머스 완전탐색 문제
