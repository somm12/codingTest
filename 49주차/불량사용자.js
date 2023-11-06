const check = (a, b) => {
  // 두 문자열 일치하는지 체크
  if (a.length !== b.length) return false;
  const N = a.length;
  for (let i = 0; i < N; i++) {
    if (b[i] === "*") continue; // * 이면 넘어가기
    if (a[i] === b[i]) continue;
    else {
      return false;
    }
  }
  return true;
};
function solution(user, bann) {
  var answer = {};

  const n = user.length;
  const m = bann.length;

  const perm = () => {
    // 모든 경우의 수 구하기 (순열)
    let arr = [];
    let visited = new Array(m).fill(0);
    const per = (res) => {
      if (res.length === m) {
        arr.push(res);
        return;
      }
      for (let i = 0; i < n; i++) {
        if (!visited[i]) {
          visited[i] = 1;
          per([...res, user[i]]);
          visited[i] = 0;
        }
      }
    };
    per([], 0);

    return arr;
  };
  let arr = perm();

  for (let tmp of arr) {
    let idx = 0;
    let cnt = 0;
    for (let v of tmp) {
      if (check(v, bann[idx])) {
        cnt += 1;
      }
      idx += 1;
    }
    if (cnt === m) {
      // 해당 경우가 bann과 같다면, answer에 경우 추가.
      tmp.sort();
      answer[tmp] = 1;
    }
  }

  answer = Object.keys(answer);
  return answer.length;
}
// 프로그래머스
