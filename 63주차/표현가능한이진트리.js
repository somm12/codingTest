function solution(numbers) {
  var answer = [];

  for (let v of numbers) {
    const bin = v.toString(2);
    const len = bin.length;
    const m = len.toString(2).length; // bin을 표현하기 위한 트리의 높이. 2*m -1 => 포화 이진 트리 일때 노드 개수.
    let s = "";
    s = "0".repeat(2 ** m - 1 - len) + bin; // 0을 앞에 채운다.

    if (!checkTree(s, 0, s.length - 1)) {
      // 부모가 0 인데, 자식이 1인경우 찾기.
      answer.push(0);
    } else answer.push(1);
  }
  return answer;
}

const checkTree = (tree, start, end) => {
  const mid = Math.floor((start + end) / 2); // 부모
  const left = Math.floor((start + mid - 1) / 2); // 왼쪽 자식
  const right = Math.floor((mid + 1 + end) / 2); // 오른쪽 자식.

  if (start === end) return true;

  if (tree[mid] === "0" && (tree[left] === "1" || tree[right] === "1")) {
    return false;
  }
  if (!checkTree(tree, start, mid - 1)) return false;
  if (!checkTree(tree, mid + 1, end)) return false;

  return true;
};
