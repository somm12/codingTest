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
  swap(a, b) {
    [this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]];
  }

  remove() {
    if (this.heap.length == 1) return this.heap.pop();
    const value = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.bubbleDown();
    return value;
  }
  bubbleUp() {
    let index = this.heap.length - 1;
    let parentIdx = Math.floor((index - 1) / 2);
    while (this.heap[parentIdx] && this.heap[index] < this.heap[parentIdx]) {
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
      (this.heap[leftIdx] && this.heap[leftIdx] < this.heap[index]) ||
      (this.heap[rightIdx] && this.heap[rightIdx] < this.heap[index])
    ) {
      let smallerIdx = leftIdx;
      if (this.heap[rightIdx] && this.heap[rightIdx] < this.heap[smallerIdx]) {
        smallerIdx = rightIdx;
      }

      this.swap(index, smallerIdx);
      index = smallerIdx;
      leftIdx = index * 2 + 1;
      rightIdx = index * 2 + 2;
    }
  }
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = () => {
  const heap = new MinHeap();
  let j = 0;
  let answer = 0;
  // 보석, 가방 모두 무게 작은순 정렬. 다음 가방에서 고를 때 순차적으로 가능한 보석을 고르기 위함.
  arr.sort((a, b) => a[0] - b[0]);
  bags.sort((a, b) => a - b);

  for (let i = 0; i < k; i++) {
    //현재 가방 무게 이하면 일단 모두 넣기. 그중 제일 큰 값(최대힙) 뽑아서 더하기. 그 다음 가방은 이어서 당연히 이전에 넣었던 보석 모두 넣을 수 있으므로
    // 이어서 진행
    while (j < n && arr[j][0] <= bags[i]) heap.add(arr[j++][1] * -1);

    if (heap.size() > 0) {
      answer += heap.remove() * -1;
    }
  }
  console.log(answer);
};

const bags = [];
let num = 0;
const arr = [];
let cnt = 0;
let [n, k] = [null, null];
rl.on("line", (line) => {
  if (!n) [n, k] = line.split(" ").map((e) => +e);
  else if (cnt < n) {
    arr.push(line.split(" ").map((e) => +e));
    cnt += 1;
  } else {
    bags.push(line.split(" ").map((e) => +e));
    num += 1;
    if (num == k) rl.close();
  }
});
rl.on("close", () => {
  solution();
  process.exit();
});
// 백준 보석도둑
