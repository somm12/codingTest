function solution(n, wires) {
  let answer = Infinity;
  const g = Array(n + 1)
    .fill()
    .map((e) => Array());
  for (const [a, b] of wires) {
    g[a].push(b);
    g[b].push(a);
  }
  const parent = Array(n + 1).fill(-1);
  const arr = [1];
  for (let v of arr) {
    for (let node of g[v]) {
      if (parent[v] !== node) {
        parent[node] = v;
        arr.push(node);
      }
    }
  }

  arr.reverse();
  const leafToRoot = [...arr]; // 리프노드부터 부모까지 순회한 배열.
  const dp = Array(n + 1).fill(1); // 자신을 포함한  자식부터 자신까지의 노드 개수 dp.
  for (let v of leafToRoot) {
    if (parent[v] !== -1) {
      dp[parent[v]] += dp[v];
      const diff = Math.abs(n - 2 * dp[v]); // n-dp[i] - dp[i] : 두 송전탑 개수 차이.
      answer = Math.min(answer, diff);
    }
  }

  return answer;
}
