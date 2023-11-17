class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}
class Queue {
  constructor() {
    this.head = null;
    this.rear = null;
    this.length = 0;
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
    const data = this.head.data;
    if (!this.head) {
      return false;
    }
    this.head = this.head.next;
    this.length--;
    return data;
  }
}

const inRange = (nx, ny) => {
  return 0 <= nx && nx < N && 0 <= ny && ny < N;
};
const removeBigG = (group) => {
  group.forEach(([x, y]) => {
    g[x][y] = -2;
  });
  answer += group.length ** 2;
  return;
};

const gravity = () => {
  for (let x = N - 1; x >= 0; x--) {
    for (let y = 0; y < N; y++) {
      if (g[x][y] >= 0) {
        let color = g[x][y];
        let [nx, ny] = [x, y];
        while (1) {
          nx += 1;
          if (!inRange(nx, ny) || g[nx][ny] !== -2) {
            nx -= 1;
            break;
          }
        }
        if (x === nx) continue;
        g[x][y] = -2;
        g[nx][ny] = color;
      }
    }
  }
};

const rotate = () => {
  let newG = Array(N)
    .fill()
    .map((e) => Array(N).fill(0));
  for (let x = 0; x < N; x++) {
    for (let y = 0; y < N; y++) {
      newG[N - 1 - y][x] = g[x][y];
    }
  }
  g = newG;
};
const bfs = (color, x, y) => {
  const visited = Array(N)
    .fill()
    .map((e) => Array(N).fill(0));
  visited[x][y] = 1;
  const q = new Queue();
  q.enqueue([x, y]);
  let group = [];
  while (q.length) {
    const [x, y] = q.dequeue();
    group.push([x, y]);
    for (let i = 0; i < 4; i++) {
      const [nx, ny] = [x + dx[i], y + dy[i]];
      if (
        inRange(nx, ny) &&
        !visited[nx][ny] &&
        (g[nx][ny] === color || g[nx][ny] === 0)
      ) {
        visited[nx][ny] = 1;

        q.enqueue([nx, ny]);
      }
    }
  }

  let zCnt = 0; //무지개 개수 세기
  let stands = []; // 기준블록 후보배열.
  group.forEach(([i, j]) => {
    if (g[i][j] === 0) {
      zCnt += 1;
    } else {
      stands.push([i, j]);
    }
  });
  stands.sort((a, b) => {
    if (a[0] !== b[0]) return a[0] - b[0];
    return a[1] - b[1];
  });
  return [zCnt, stands[0][0], stands[0][1], group]; // 무지개 블록 개수, 기준블록 행인덱스,기준 열인덱스, 그룹배열
};

const findBigGroup = () => {
  const cand = []; //그룹들을 담을 배열

  for (let x = 0; x < N; x++) {
    for (let y = 0; y < N; y++) {
      if (g[x][y] > 0) {
        const color = g[x][y];
        const group = bfs(color, x, y);
        if (group[3].length >= 2) cand.push(group);
      }
    }
  }
  if (cand.length === 0) return -1;

  cand.sort((a, b) => {
    if (a[3].length !== b[3].length) return b[3].length - a[3].length;
    else if (a[0] !== b[0]) return b[0] - a[0];
    else if (a[1] !== b[1]) return b[1] - a[1];
    return b[2] - a[2];
  });
  return cand[0][3];
};

const solution = () => {
  let num = 1;
  while (1) {
    num++;
    let bigGroup = findBigGroup();
    if (bigGroup === -1) break;
    removeBigG(bigGroup);

    gravity();

    rotate();
    gravity();
  }
  console.log(answer);
  return;
};

const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let answer = 0;
let N = null;
let M = null;

let g = [];
let count = 0;
let data = null;

rl.on("line", (line) => {
  if (!N) {
    [N, M] = line.split(" ").map((e) => +e);
  } else if (!data) {
    g.push(line.split(" ").map((e) => +e));
    count += 1;
  }
  if (count === N) rl.close();
}).on("close", () => {
  solution();
  process.exit();
});
// 가장 큰 그룹찾기.
// 무지개 블록은 그룹에 포함되어도 상관없음.
// 백준 - js로 구현 문제 풀기
