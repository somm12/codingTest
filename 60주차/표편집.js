function solution(n, k, cmd) {
  let answer;
  let trashCan = [];
  const Node = function (index, prev) {
    this.index = index;
    this.prev = prev;
    this.next = null;
  };

  let p;
  let select;
  for (let i = 0; i < n; i++) {
    if (i === 0) {
      const node = new Node(i, null);
      p = node;
    } else {
      const node = new Node(i, p);
      p.next = node;
      p = node;
    }
    if (i === k) select = p;
  }

  const move = (num, direction) => {
    for (let i = 0; i < num; i++) {
      select = select[direction];
    }
  };

  const deleteRow = () => {
    trashCan.push(select);
    const sp = select.prev;
    const sn = select.next;
    if (!select.next) {
      // 마지막 행 삭제면 윗행 선택.
      select = sp;
    } else {
      // 마지막 행 삭제가 아니라면 아래 행 선택.
      select = sn;
    }
    if (sp) {
      // 삭제 노드가 맨앞일 수 있으니, 확인.
      sp.next = sn;
    }
    if (sn) {
      // 삭제 노드가 맨 뒤 일 수 있으니, 있는지 확인 후 처리.
      sn.prev = sp;
    }
  };
  const recover = () => {
    const target = trashCan.pop();
    if (target.prev) {
      target.prev.next = target;
    }
    if (target.next) {
      target.next.prev = target;
    }
  };
  cmd.forEach((v) => {
    const c = v.split(" ");
    switch (c[0]) {
      case "D":
        move(+c[1], "next");
        break;
      case "U":
        move(+c[1], "prev");
        break;
      case "C":
        deleteRow();
        break;
      case "Z":
        recover();
        break;
    }
  });

  answer = Array(n).fill("O");
  trashCan.forEach((v) => (answer[v.index] = "X"));
  return answer.join("");
}
