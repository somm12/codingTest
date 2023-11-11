class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}
// 큐 클래스
class Queue {
  constructor() {
    this.head = null; // 제일 앞 노드
    this.rear = null; // 제일 뒤 노드
    this.length = 0; // 노드의 길이
  }

  enqueue(data) {
    // 노드 추가.
    const node = new Node(data); // data를 가진 node를 만들어준다.
    if (!this.head) {
      // 헤드가 없을 경우 head를 해당 노드로
      this.head = node;
    } else {
      this.rear.next = node; // 아닐 경우 마지막의 다음 노드로
    }
    this.rear = node; // 마지막을 해당 노드로 한다.
    this.length++;
  }

  dequeue() {
    // 노드 삭제.
    if (!this.head) {
      // 헤드가 없으면 한 개도 없는 것이므로 false를 반환.
      return false;
    }
    const data = this.head.data; // head를 head의 다음 것으로 바꿔주고 뺀 data를 return
    this.head = this.head.next;
    this.length--;
    return data;
  }

  // head를 반환하는 함수
  front() {
    // head가 있을 경우 head의 data를 반환.
    return this.head && this.head.data;
  }
}
// 문제 풀이 부분 : solution.
const solution = (N) => {
  const q = new Queue();
  for (let i = 1; i <= N; i++) {
    q.enqueue(i);
  }
  if (q.length === 1) {
    console.log(q.front());
    return;
  }

  while (q.length > 1) {
    q.dequeue();
    if (q.length === 1) {
      console.log(q.front());
      return;
    }
    const data = q.dequeue();
    q.enqueue(data);
  }
};

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let N = null;

rl.on("line", function (line) {
  if (!N) {
    // N이 null이면
    N = +line;
  }
  rl.close();
}).on("close", function () {
  // rl.close()를 호출하면 이 콜백함수로 들어오고
  solution(N); // solution을 호출 한 후
  process.exit(); // 프로세스를 종료한다.
});
// 백준 자료구조 문제.
