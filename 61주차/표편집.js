function solution(n, k, cmd) {
  const answer = Array(n).fill("O");
  const deleted = [];
  class Node {
    constructor(idx, left, right) {
      this.idx = idx;
      this.left = left;
      this.right = right;
    }
  }
  let select;
  let [prev, next] = [null, null];

  for (let i = 0; i < n; i++) {
    // 0 ~ n-1 노드 까지 양방향 연결 시키기.
    const node = new Node(i, prev, next);
    if (prev) {
      // prev가 존재한다면, prev의 다음노드는 방금 만든 노드.
      prev.right = node;
    }
    prev = node; // 방금 만든 노드가 prev 노드가 됨.

    if (k === i) {
      select = node;
    }
  }

  const move = (cnt, direction) => {
    // 대괄호 기법 이용해서 up, down 구현.
    for (let i = 0; i < cnt; i++) {
      select = select[direction];
    }
  };
  const remove = () => {
    deleted.push(select);
    const prev = select.left;
    const next = select.right;
    if (next) {
      select = next;
    } else {
      select = prev;
    }
    if (prev) {
      prev.right = next;
    }
    if (next) {
      next.left = prev;
    }
  };
  const recover = () => {
    const tmp = deleted.pop(); // 삭제한 노드 꺼내기.
    const prev = tmp.left;
    const next = tmp.right;
    if (prev) {
      prev.right = tmp;
    }
    if (next) {
      next.left = tmp;
    }
  };
  cmd.forEach((v) => {
    const arr = v.split(" ");

    switch (arr[0]) {
      case "D":
        move(+arr[1], "right");
        break;
      case "U":
        move(+arr[1], "left");
        break;
      case "C":
        remove();
        break;
      case "Z":
        recover();
        break;
    }
  });

  deleted.forEach((v) => (answer[v.idx] = "X"));

  return answer.join("");
}
