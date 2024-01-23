//조합 구하기
const calc = (dices, dict, dice) => {
  const dfs = (L, total) => {
    if (L === dices.length) {
      if (dict.has(total)) dict.set(total, dict.get(total) + 1);
      else dict.set(total, 1);
      return;
    }
    for (let v of dice[dices[L]]) {
      dfs(L + 1, total + v);
    }
  };
  dfs(0, 0);
};

const combi = (n) => {
  const tmp = [];
  const com = (res, start) => {
    if (res.length === n / 2) {
      tmp.push(res);
      return;
    }
    for (let i = start; i < n; i++) {
      com([...res, i], i + 1);
    }
  };
  com([], 0);
  return tmp;
};
function solution(dice) {
  let total = 0;
  let vic = [];

  const n = dice.length;
  const all = [];
  for (let i = 0; i < n; i++) all.push(i);
  const arr = combi(n);

  for (const aCase of arr) {
    const bCase = all.filter((v) => !aCase.includes(v));
    const aMap = new Map();
    const bMap = new Map();

    // 함수 호출
    // 나오는 숫자 합의 중복을 이용해서 Map 자료형 이용하기.

    calc(aCase, aMap, dice); // A가 가질 수 있는 경우의 합.
    calc(bCase, bMap, dice); // B가 가질 수 있는 경우의 합.

    let aWin = 0;
    for (const [aKey, aCnt] of aMap) {
      for (const [bKey, bCnt] of bMap) {
        if (aKey > bKey) {
          //a가 더 크면, a경우 * b경우.
          aWin += aCnt * bCnt;
        }
      }
    }
    if (total < aWin) {
      vic = [...aCase];
      total = aWin;
    }
  }

  vic.sort((a, b) => a - b);
  // 주사위 번호(1~n) 오름차순으로 정렬.
  return vic.map((v) => v + 1); // 주사위 숫자번호를 0부터 해서 +1 해주기
}
