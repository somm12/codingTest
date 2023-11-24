function solution(gems) {
  var answer = [];
  let n = gems.length; // 배열 길이
  let set = new Set();
  gems.forEach((v) => set.add(v));
  let kind = set.size; // 전체 종류.

  let map = new Map();
  let reduce = false;

  let minLength = Infinity;
  let [s, e] = [0, 0]; // 시작점.

  while (s <= n && e <= n) {
    if (map.size < kind) {
      // 아직 종류가 적으면, map에 추가하고 e+1
      const v = gems[e];
      if (map.has(v)) map.set(v, map.get(v) + 1);
      else map.set(v, 1);
      e += 1;
    } else {
      // 종류가 모두 포함 되었다면, answer에 후보 추가.
      const l = e - s; //구간 길이
      if (l < minLength) {
        answer.push([l, s + 1, e]); // 보석 번호는 1부터 시작이므로, 인덱스 형태 때문에 +1.
        reduce = true; // 이제 범위를 줄여나간다.
      }
      if (reduce) {
        // 줄여나간다면,
        const v = gems[s]; // 첫 원소를 1개씩 제거.
        map.set(v, map.get(v) - 1);

        if (map.get(v) === 0) {
          // 0개가 되버리면, map에서 삭제하고 또다시 이어서 추가할 준비.
          map.delete(v);
          reduce = false; // 이어서 다른 범위 탐색을 위해서 false
        }
        s += 1; // 첫 원소 다음부터 map에 포함
      }
    }
  }

  answer.sort((a, b) => {
    if (a[0] !== b[0]) return a[0] - b[0]; // 구간이 더 짧고
    if (a[1] !== b[1]) return a[1] - b[1]; // 출발 번호가 더 작은 순.
  });

  answer = [answer[0][1], answer[0][2]];
  return answer;
}
// 더 짧은 풀이.
// map을 이용해서 탐색하다가 길이가 최대 종류 개수가 되면 그 때의 시작번호와 끝번호를 체크하는 방법.
function solution(gems) {
  const gemVarietyCounts = new Set(gems).size;

  const gemMap = new Map();
  const gemLengths = [];
  gems.forEach((gem, i) => {
    gemMap.delete(gem); // 이전꺼 삭제
    gemMap.set(gem, i); // 현재 보석의 위치 인덱스 할당.
    if (gemMap.size === gemVarietyCounts) {
      // 최대 종류 개수가 되었다면,
      // values는 iterator 반환. .next().value를 하면서 순회할 수 있음.!!
      gemLengths.push([gemMap.values().next().value + 1, i + 1]); // 첫 번호와 현재 마지막 인덱스 번호 할당.
    }
  });

  gemLengths.sort((a, b) => {
    if (a[1] - a[0] === b[1] - b[0]) {
      // 구간이 같다면
      return a[1] - b[1]; // 시작 번호가 짧은 순
    }
    return a[1] - a[0] - (b[1] - b[0]); // 같지 않으면 구간이 짧은순
  });

  return gemLengths[0];
}
// 프로그래머스
