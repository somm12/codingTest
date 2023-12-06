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
    // Array 맨 뒤에 값을 추가하고, 부모와 값을 비교에서 값을 swap한다.
    let index = this.heap.length - 1;
    console.log(index, "!!");
    let parentIdx = Math.floor((index - 1) / 2);
    while (
      // 우선순위: 3번째 값 작고 > 2번째 값 작음.
      // 만약 부모의 3번째 값이, 현재의 3번째 값과 다르다면 -> 부모가 값이 크면 swap. 아니면 그대로
      // 3번째 값이 서로 같다면, 2번째 값 비교 -> 부모의 값이 더 크면 swap.아니면 그대로.
      this.heap[parentIdx] &&
      ((this.heap[index][2] !== this.heap[parentIdx][2] &&
        this.heap[index][2] < this.heap[parentIdx][2]) ||
        (this.heap[index][2] === this.heap[parentIdx][2] &&
          this.heap[index][1] < this.heap[parentIdx][1]))
    ) {
      console.log(h, index, parentIdx, "swap!!!");
      this.swap(index, parentIdx);
      index = parentIdx;
      parentIdx = Math.floor((index - 1) / 2);
    }
  }

  bubbleDown() {
    // Array 맨 뒤의 값을 root에 넣고 자식들과 값을 비교하여 아래로 내려가며 swap함
    let index = 0; // root의 인덱스 번호
    let leftIdx = index * 2 + 1; // 부모의 왼쪽 자식의 인덱스 번호.
    let rightIdx = index * 2 + 2; // 부모의 오른쪽 자식의 인덱스 번호.

    while (
      (this.heap[leftIdx] &&
        ((this.heap[leftIdx][2] !== this.heap[index][2] &&
          this.heap[leftIdx][2] < this.heap[index][2]) ||
          (this.heap[leftIdx][2] === this.heap[index][2] &&
            this.heap[leftIdx][1] < this.heap[index][1]))) ||
      (this.heap[rightIdx] &&
        ((this.heap[rightIdx][2] !== this.heap[index][2] &&
          this.heap[rightIdx][2] < this.heap[index][2]) ||
          (this.heap[rightIdx][2] === this.heap[index][2] &&
            this.heap[rightIdx][1] < this.heap[index][1])))
    ) {
      let smallerIdx = leftIdx;
      if (
        this.heap[rightIdx] &&
        ((this.heap[rightIdx][2] !== this.heap[smallerIdx][2] &&
          this.heap[rightIdx][2] < this.heap[smallerIdx][2]) ||
          (this.heap[rightIdx][2] === this.heap[smallerIdx][2] &&
            this.heap[rightIdx][1] < this.heap[smallerIdx][1]))
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
const h = new MinHeap();
// 힙이란 : 완전 이진 트리의 일종으로 우선순위 큐를 위하여 만들어진 자료구조.

// Array를 이용해서 힙을 직접 구현,
// 각 인덱스는 0: 루트, index*2+1(왼쪽 자식), index*2+2(오른쪽 자식.) 구조.

// ✅ 값이 여러개가 있고 각 우선순위가 있다면?
// h 힙은 index: 2인 부분이 우선순위로 작고,
// 그 다음으로 index: 1인 값이 우선순위로 작은 순으로 트리를 구성.
h.add([1, 1, 3]);
h.add([2, 10, 1]);
h.add([3, 9, 1]);
h.add([4, 1, 0]);
console.log("삭제");
console.log(h.remove()); // [4,1,0]
console.log(h.remove()); // [3,9,1]
console.log(h.remove()); // [2,10,1]
console.log(h.remove()); // [1,1,3]
