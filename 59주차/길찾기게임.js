function solution(nodeinfo) {
  const pre = [];
  const post = [];
  // 이진트리 만들 때 순차적으로 insert하기 위해 y좌표가 큰 순으로 정렬.
  // [노드 번호, x,y]
  const info = nodeinfo.map((node, idx) => [idx + 1, node[0], node[1]]);
  info.sort((a, b) => b[2] - a[2]);

  const tree = new bTree(info[0][0], info[0][1]); // 루트 노드 생성.
  for (let i = 1; i < info.length; i++) {
    tree.insert(info[i][0], info[i][1]);
  }
  const preOrder = (tree) => {
    // 전위 순회
    if (tree !== null) {
      pre.push(tree.num);
      preOrder(tree.left);
      preOrder(tree.right);
    }
  };

  const postOrder = (tree) => {
    // 후위 순회.
    if (tree !== null) {
      postOrder(tree.left);
      postOrder(tree.right);
      post.push(tree.num);
    }
  };
  preOrder(tree);
  postOrder(tree);

  return [pre, post];
}

class bTree {
  constructor(num, x) {
    // 노드번호, x좌표와, 왼쪽 서브트리, 오른쪽 서브트리 생성.
    this.num = num;
    this.x = x;
    this.left = null;
    this.right = null;
  }
  insert(num, x) {
    if (this.x > x) {
      // 현재 노드의 x가 더 크면 왼쪽으로 보내기.
      this.toLeft(num, x);
    } else this.toRight(num, x);
  }

  toLeft(num, x) {
    // 왼쪽 서브트리에 노드가 존재한다면, 다시 위치를 찾아야 하므로, insert로 보낸다.
    if (this.left) this.left.insert(num, x);
    // 메소드로서 호출 했으므로, insert에서는 this가 this.left를 가리킴.
    else this.left = new bTree(num, x); // null 이라면, 삽입.
  }

  toRight(num, x) {
    // 오른쪽 서브트리에 노드가 존재한다면, 다시 위치를 찾아야 하므로, insert로 보낸다.
    if (this.right) this.right.insert(num, x);
    else this.right = new bTree(num, x);
  }
}
// 프로그래머스 문제
// 이진트리.
