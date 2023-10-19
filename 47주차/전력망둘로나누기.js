function solution(n, wires) {
  var answer = 100; // 두 전력망이 가지는 송전탑 개수 차이 절댓값 구하기.
  let cnt = 0;
  // 배열 초기화.
  var arr = new Array(n + 1);

  for (var i = 0; i < arr.length; i++) {
    arr[i] = new Array(); // n+1 크기로 빈배열 넣기.
  }
  // 노드 연결.
  for (let v of wires) {
    const [a, b] = v;
    arr[a].push(b);
    arr[b].push(a);
  }

  function dfs(start, a, b) {
    visited[start] = 1;
    cnt += 1;
    for (let v of arr[start]) {
      if (
        // a,b번 노드의 연결이 끊어졌을 때,
        !visited[v] &&
        [start, v].toString() !== [a, b].toString() &&
        [v, start].toString() !== [a, b].toString()
      ) {
        visited[v] = 1;
        dfs(v, a, b);
      }
    }
  }

  let visited = new Array(n + 1).fill(0);
  // 하나 끊기
  for (let v of wires) {
    const [a, b] = v;
    let tmp = [];
    // console.log(a,b,"끊기")
    visited = new Array(n + 1).fill(0);
    for (let i = 1; i <= n; i++) {
      if (!visited[i]) {
        cnt = 0;
        dfs(i, a, b);
        tmp.push(cnt);
      }
    }

    answer = Math.min(answer, Math.abs(tmp[0] - tmp[1]));
  }

  return answer;
}
// 프로그래머스 완전 탐색.
