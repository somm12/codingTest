class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}
class Queue {
  constructor() {
    this.length = 0;
    this.head = 0;
    this.rear = 0;
  }
  enqueue(data) {
    const node = new Node(data);
    if (!this.head) {
      this.head = node;
    } else {
      this.rear.next = node;
    }
    this.rear = node;
    this.length++;
  }
  dequeue() {
    if (!this.head) {
      return false;
    }
    const data = this.head.data;
    this.head = this.head.next;
    this.length--;
    return data;
  }
}
function solution(n, roads, sources, destination) {
  var answer = [];
  let g = new Array(n + 1).fill().map((e) => new Array());
  roads.forEach(([a, b]) => {
    g[a].push(b);
    g[b].push(a);
  });
  const time = new Array(n + 1).fill(Infinity);
  const da = (start) => {
    time[start] = 0;
    const q = new Queue();
    q.enqueue([start, 0]);
    while (q.length) {
      const [now, dist] = q.dequeue();
      if (time[now] < dist) continue;
      for (let v of g[now]) {
        let cost = dist + 1;
        if (cost < time[v]) {
          time[v] = cost;
          q.enqueue([v, cost]);
        }
      }
    }
  };

  da(destination);
  for (let v of sources) {
    time[v] === Infinity ? answer.push(-1) : answer.push(time[v]);
  }
  return answer;
}
// 다익스트라. -> 모두 길이가 1인 경우에서 최단거리 구하기
// js는 큐를 따로 구현해야함.
