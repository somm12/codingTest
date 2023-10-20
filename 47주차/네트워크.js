function solution(n, computers) {
  var answer = 0;
  let visited = new Array(n).fill(0);
  function dfs(x) {
    visited[x] = 1;

    for (let i = 0; i < n; i++) {
      // x번 노드와 연결된 0~n-1번 노드 중에서 값이 1인것 찾기.
      if (!visited[i] && computers[x][i]) dfs(i);
    }
  }

  for (let i = 0; i < n; i++) {
    if (!visited[i]) {
      dfs(i);
      answer += 1;
    }
  }
  return answer;
}
// 노드끼리 연결여부를 나타낸 2차원 배열을 가지고 네트워크가 몇 개 인지 맞추기.
// 프로그래머스 dfs.
