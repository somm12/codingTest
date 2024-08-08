// 최소힙 구현.
class MinHeap {
  constructor() {
    this.heap = [];
  }
  size() {
    return this.heap.length;
  }
  add(value) {
    this.heap.push(value);
    this.bubbleUp();
  }
  remove() {
    if (this.heap.length == 1) return this.heap.pop();

    const value = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.bubbleDown();
    return value;
  }
  bubbleUp() {
    let idx = this.heap.length - 1;
    let parentIdx = Math.floor((idx - 1) / 2);
    while (this.heap[parentIdx] && this.heap[parentIdx] > this.heap[idx]) {
      this.swap(parentIdx, idx);
      idx = parentIdx;
      parentIdx = Math.floor((idx - 1) / 2);
    }
  }
  bubbleDown() {
    let idx = 0;
    let leftIdx = idx * 2 + 1;
    let rightIdx = idx * 2 + 2;
    while (
      (this.heap[leftIdx] && this.heap[leftIdx] < this.heap[idx]) ||
      (this.heap[rightIdx] && this.heap[rightIdx] < this.heap[idx])
    ) {
      let smallerIdx = leftIdx;
      if (this.heap[rightIdx] && this.heap[smallerIdx] > this.heap[rightIdx])
        smallerIdx = rightIdx;
      this.swap(idx, smallerIdx);
      idx = smallerIdx;
      leftIdx = idx * 2 + 1;
      rightIdx = idx * 2 + 2;
    }
  }
  swap(a, b) {
    [this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]];
  }
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const solution = () => {
  arr.sort((a, b) => a[0] - b[0]); // 마감이 빠른순으로 정렬.
  const heap = new MinHeap();

  for (const [d, num] of arr) {
    heap.add(num);
    if (heap.size() > d) {
      // x번째 날까지 기준으로, 가장 큰 개수만 남기기.
      heap.remove();
    }
  }
  let answer = 0;
  while (heap.size() > 0) {
    // 힙에 남은 컵라면 수(데드라인 안에 가능한 경우의 수 중 최대)들을 합하여 답을 구한다.
    answer += heap.remove();
  }
  console.log(answer);
};
let n = null;
const arr = [];
let cnt = 0;

rl.on("line", (line) => {
  if (!n) n = +line;
  else {
    arr.push(line.split(" ").map((e) => +e));
    cnt += 1;
    if (cnt == n) rl.close();
  }
});
rl.on("close", () => {
  solution();
  process.exit();
});
// 백준 컵라면
