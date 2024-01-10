function solution(nodeinfo) {
  const preorderArr = [];
  const postorderArr = [];
  // y좌표 기준으로(level 높은순) 내림차순 정렬(루트부터 차례대로)
  const nodes = nodeinfo
    .map((node, idx) => [idx + 1, node[0], node[1]]) // 노드 번호, x좌표, y좌표
    .sort((a, b) => b[2] - a[2]);
  // 루트를 기준으로 트리 생성
  const bTree = new BinaryTree(nodes[0][0], nodes[0][1]);
  for (let i = 1; i < nodes.length; i++) {
    // 남은 노드들을 insert해주기.
    bTree.insert(nodes[i][0], nodes[i][1]);
  }
  // 전위 순회, 후위 순회 구하기
  preorder(bTree, preorderArr);
  postorder(bTree, postorderArr);

  return [preorderArr, postorderArr];
}

class BinaryTree {
  constructor(value, x_pos) {
    // 노드 번호와, x좌표.
    this.value = value;
    this.x_pos = x_pos;
    this.left = null; // 왼쪽, 오른쪽 서브트리.
    this.right = null;
  }

  insert(value, x_pos) {
    // 현재 노드보다 x좌표가 작다면 left, 아니면 right
    this.x_pos > x_pos
      ? this._toLeft(value, x_pos)
      : this._toRight(value, x_pos);
  }

  _toLeft(value, x_pos) {
    // 이미 왼쪽 부분이 존재하면, 다시 insert 이어서 하기(깊에 내려가서 올바른 위치에 insert)
    this.left
      ? this.left.insert(value, x_pos)
      : (this.left = new BinaryTree(value, x_pos));
  }

  _toRight(value, x_pos) {
    // 이미 오른쪽 부분이 존재하면, 다시 insert
    this.right
      ? this.right.insert(value, x_pos)
      : (this.right = new BinaryTree(value, x_pos));
  }
}

const preorder = (bTree, arr) => {
  // 전위 순회: 루트-> 왼쪽-> 오른쪽
  if (bTree !== null) {
    // 더이상 노드가 없을 때 까지.
    arr.push(bTree.value);
    preorder(bTree.left, arr);
    preorder(bTree.right, arr);
  }
};

const postorder = (bTree, arr) => {
  // 왼쪽-> 오른쪽 -> 루트
  if (bTree !== null) {
    postorder(bTree.left, arr);
    postorder(bTree.right, arr);
    arr.push(bTree.value);
  }
};
// 프로그래머스
