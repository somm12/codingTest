function solution(tickets) {
  var answer = [];
  let n = tickets.length;
  let route = {};
  let visited = {};

  for (let c of tickets) {
    let [a, b] = c;

    if (a in route) {
      route[a].push(b); // 현재 공항에서 갈 수 있는 도시 할당.
      visited[a].push(0); // 각각 티켓의 방문 여부를 나타내는 배열.
    } else {
      route[a] = [b];
      visited[a] = [0];
    }
  }

  for (let c in route) route[c].sort(); // 경로가 여러개일때, 사전순 1개 고르기 위한 정렬.
  console.log(route);
  function dfs(now, res) {
    if (res.length === n + 1) {
      answer.push(res);
      return;
    }
    // 더이상 다음 경로로 갈 수 없는 경우, 딕셔너리에 키가 없어서 발생하는 에러를 막기 위함.
    if (now in route) {
      for (let i = 0; i < route[now].length; i++) {
        let city = route[now][i];
        if (!visited[now][i]) {
          visited[now][i] = 1;
          dfs(city, [...res, city]);
          visited[now][i] = 0;
        }
      }
    }
  }
  dfs("ICN", ["ICN"]);
  // console.log(answer)
  return answer[0];
} // 프로그래머스 dfs.
