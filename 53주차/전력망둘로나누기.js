function solution(n, wires) {
  const g = Array(n + 1)
    .fill()
    .map((e) => Array());
  for (const [a, b] of wires) {
    g[a].push(b);
    g[b].push(a);
  }
  const parent = new Array(n + 1).fill(-1); // 각 인덱스 노드에 대한 부모노드 값.
  const leafToRoot = [0, 1]; //자식 -> 부모 순서로 순회.

  for (let i = 1; i < leafToRoot.length; ++i) {
    // 2*wires.length 만큼 실행.
    const u = leafToRoot[i];
    for (const v of g[u]) {
      // u노드와 연결된 노드들.

      if (v != parent[u]) {
        // u와 연결된 v가 u의 부모가 아니면
        parent[v] = u; // v의 부모를 u로 할당.
        leafToRoot.push(v); // 루트에서 점점 자식 쪽으로 아래로 내려가는 순회를 담는다.
      }
    }
  }

  let answer = n;
  const dp = new Array(n + 1).fill(1); //각자 본인 포함이므로 1로 채우기
  // dp[i]: i 노드 까지의 (자식 포함) 총 노드 개수 합
  for (let i = leafToRoot.length - 1; i > 0; i--) {
    // 자식 부터 탐색.
    const v = leafToRoot[i]; // 자식 노드 번호
    dp[parent[v]] += dp[v]; // 현재 자식 노드의 부모 노드에 지금까지의 총 노드 개수 더하기.
    let diff = Math.abs(n - dp[v] - dp[v]);
    answer = Math.min(answer, diff);
  }

  return answer;
}
// 프로그래머스
// 시간 복잡도: O(n^2). n이 100이라 괜찮지만, 10만등 높아진다면?
// dp를 이용해서 문제 풀기.
