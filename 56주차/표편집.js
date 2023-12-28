function solution(n, k, cmd) {
  let deleteBin = []; // 삭제된 노드 정보를 담을 배열

  const Node = function (index, prev) {
    this.index = index;
    this.prev = prev;
    this.next = null;
  };
  // 초기 노드 설정.
  let prevNode = new Node(0);
  let select; // 현재 선택된 노드 변수.

  // 양방향 연결 리스트 만들기
  for (let i = 1; i < n; i++) {
    const current = new Node(i, prevNode);
    prevNode.next = current;
    prevNode = current;
    if (i === k) {
      select = current;
    }
  }
  // U,D 일때 select를 움직이는 함수. => 총합 x번 움직임 횟수는 최대 100만이하이므로 시간 초과 안남.
  const move = (count, direction) => {
    for (let i = 0; i < count; i++) {
      if (!select[direction]) break;

      select = select[direction];
    }
  };
  // 현재 선택된 노드 삭제, 마지막 행이면 바로 윗행, 아니면 아래 행을 가리킴.
  const deleteNode = () => {
    const prev = select.prev;
    const next = select.next;

    deleteBin.push(select);
    select = next ? next : prev;

    if (prev) prev.next = next;
    if (next) next.prev = prev;
  };
  // 다시 복구 시키기.
  const recoverNode = () => {
    const target = deleteBin.pop(); // 가장 최근인 노드를 꺼내기
    const prev = target.prev; // 연결 시켜주기.
    const next = target.next;

    if (prev) prev.next = target;
    if (next) next.prev = target;
  };

  cmd.forEach((c) => {
    switch (c[0]) {
      case "U":
        move(c.split(" ")[1], "prev"); // 대괄호 기법을 이용해서, 앞 뒤로 움직임.
        break;
      case "D":
        move(c.split(" ")[1], "next");
        break;
      case "C":
        deleteNode();
        break;
      case "Z":
        recoverNode();
        break;
    }
  });
  let answer = Array(n).fill("O");
  deleteBin.forEach((node) => {
    answer[node.index] = "X"; // 마지막까지 deleteBin 에 남은 노드는 삭제 되었다는 의미이므로 X할당.
  });

  return answer.join("");
}
// 프로그래머스.
// 자료구조 구현해보기.
