function solution(dice) {
  let answer = [];
  let big = 0;
  const n = dice.length;
  const combi = () => {
    // 주사위 조합.
    const arr = [];
    const dfs = (res, start) => {
      if (res.length === n / 2) {
        arr.push(res);
        return;
      }
      for (let i = start; i < n; i++) {
        dfs([...res, i], i + 1);
      }
    };
    dfs([], 0);
    return arr;
  };

  const aCombi = combi();
  const bCombi = [];
  for (let arr of aCombi) {
    //b 조합 구하기
    let tmp = [];
    for (let i = 0; i < n; i++) {
      if (!arr.includes(i)) {
        tmp.push(i);
      }
    }
    bCombi.push(tmp);
  }

  let [aMap, bMap] = [new Map(), new Map()]; // 각 경우에서 나올 수 있는 [총 합, 합의 개수] 구하기.

  const calc = (arr) => {
    // arr 의 경우(주사위 번호)에 나올 수 있는 총합에 대한 개수 Map 반환.
    const tmp = new Map();
    const cal = (L, total) => {
      if (L === n / 2) {
        if (tmp.has(total)) {
          tmp.set(total, tmp.get(total) + 1);
        } else {
          tmp.set(total, 1);
        }
        return;
      }
      for (let v of dice[arr[L]]) {
        cal(L + 1, total + v);
      }
    };
    cal(0, 0);
    return tmp;
  };

  for (let i = 0; i < aCombi.length; i++) {
    aMap = calc(aCombi[i]);
    bMap = calc(bCombi[i]);

    let cnt = 0;
    for (let a of aMap) {
      const [aValue, aCnt] = a;
      for (let b of bMap) {
        const [bValue, bCnt] = b;
        if (aValue > bValue) {
          //A 의 경우 합이 더  크다면, 나올수 있는 가지수 = acnt*bcnt
          cnt += aCnt * bCnt;
        }
      }
    }
    if (big < cnt) {
      // 개수가 더 크다면 주사위 조합 업데이트.
      big = cnt;
      answer = aCombi[i];
    }
  }
  answer = answer.map((v) => v + 1); // 주사위 번호 0부터 시작이라  +1하기.
  return answer.sort((a, b) => a - b); // 오름차순 정렬
}
