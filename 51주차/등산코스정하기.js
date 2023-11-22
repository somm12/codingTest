class MinHeap {
  constructor() {
    this.heap = [];
  }

  size() {
    return this.heap.length;
  }

  swap(idx1, idx2) {
    [this.heap[idx1], this.heap[idx2]] = [this.heap[idx2], this.heap[idx1]];
  }

  add(value) {
    this.heap.push(value);
    this.bubbleUp();
  }

  remove() {
    if (this.heap.length === 1) {
      return this.heap.pop();
    }

    const value = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.bubbleDown();
    return value;
  }

  bubbleUp() {
    let index = this.heap.length - 1;
    let parentIdx = Math.floor((index - 1) / 2);
    while (
      this.heap[parentIdx] &&
      this.heap[index][0] < this.heap[parentIdx][0]
    ) {
      this.swap(index, parentIdx);
      index = parentIdx;
      parentIdx = Math.floor((index - 1) / 2);
    }
  }

  bubbleDown() {
    let index = 0;
    let leftIdx = index * 2 + 1;
    let rightIdx = index * 2 + 2;

    while (
      (this.heap[leftIdx] && this.heap[leftIdx][0] < this.heap[index][0]) ||
      (this.heap[rightIdx] && this.heap[rightIdx][0] < this.heap[index][0])
    ) {
      let smallerIdx = leftIdx;
      if (
        this.heap[rightIdx] &&
        this.heap[rightIdx][0] < this.heap[smallerIdx][0]
      ) {
        smallerIdx = rightIdx;
      }

      this.swap(index, smallerIdx);
      index = smallerIdx;
      leftIdx = index * 2 + 1;
      rightIdx = index * 2 + 2;
    }
  }
}
function solution(n, paths, gates, summits) {
  var answer = [];
  summits = new Set([...summits]);

  let g = Array(n + 1)
    .fill()
    .map((e) => Array());

  paths.forEach(([a, b, c]) => {
    g[a].push([b, c]);
    g[b].push([a, c]);
  });
  let dist = Array(n + 1).fill(Infinity); // i번 노드까지 오는데, 최소의 intensity 담을 배열.
  // 각 노드 까지의 최소의 intensity를 구한다.
  const di = () => {
    let heap = new MinHeap();
    for (let v of gates) {
      heap.add([0, v]); // 출입구 노드 넣기.
      dist[v] = 0; // 출발점이므로, 비용은 0
    }

    while (heap.size() > 0) {
      const [intensity, now] = heap.remove();
      // 산봉우리 도착했거나, 현재까지의 intensity가 dist에 저장된 것 보다 크다면 넘기기.
      if (summits.has(now) || dist[now] < intensity) continue;

      for (let v of g[now]) {
        const [next, cost] = v;
        const maxV = Math.max(intensity, cost); // intensity 업데이트ㅡ.
        if (maxV < dist[next]) {
          // dist에 저장할 때, 더 최소인 intensity를 저장.
          dist[next] = maxV;
          heap.add([maxV, next]);
        }
      }
    }
  };

  di();
  for (let v of summits) {
    answer.push([v, dist[v]]);
  }

  answer.sort((a, b) => {
    if (a[1] !== b[1]) return a[1] - b[1];
    return a[0] - b[0];
  });

  return answer[0];
}
// 다익스트라 응용.
// 프로그래머스
