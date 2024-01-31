function solution(info, edges) {
  const n = info.length;
  let answer = 1;
  const g = Array(n) // 각 노드들과의 연결 정보 셋팅. [i: [i노드와 연결된 노드 번호(자식만)]]
    .fill()
    .map((e) => Array());
  for (const [a, b] of edges) {
    g[a].push(b);
  }
  const visited = Array(n).fill(0); // 방문처리
  visited[0] = 1; // 루트 노드가 시작으로, 미리 방문.
  const dfs = (a, b, res) => {
    if (a <= b) return;
    answer = Math.max(answer, a);
    if (res.length === n) return;

    for (let i = 0; i < n; i++) {
      // 방문 했던 노드 들 중에서, 아직 방문 안한 연결된 노드로 이동.
      if (visited[i]) {
        for (const v of g[i]) {
          if (!visited[v]) {
            visited[v] = 1;
            if (info[v] === 0) dfs(a + 1, b, [...res, i]);
            // 0 이라면 a+1(양.)
            else dfs(a, b + 1, [...res, i]); // 1 이라면 b+1 (늑대.)
            visited[v] = 0;
          }
        }
      }
    }
  };
  dfs(1, 0, []);

  return answer;
}
