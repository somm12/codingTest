function solution(a) {
  let answer = 0;
  const m = new Map();
  for (let v of a) {
    if (!m.has(v)) m.set(v, 1);
    else m.set(v, m.get(v) + 1);
  }
  const arr = [];
  for (let [k, v] of m) {
    arr.push([k, v]);
  }
  arr.sort((a, b) => b[1] - a[1]); //[[숫자,횟수]] 횟수 기준 내림차순 정렬.

  for (let i = 0; i < arr.length; i++) {
    if (answer >= arr[i][1]) continue; // 개수보다 answer 가 이상이면 넘어감.

    let count = 0;
    for (let j = 0; j < a.length - 1; j++) {
      if (a[j] === a[j + 1]) continue; // 같으면 안됨.
      if (a[j] !== arr[i][0] && a[j + 1] !== arr[i][0]) continue; // 하나는 값을 가지고 있어야함.

      count++; // 한 개 경우 생김.
      j++; // 만약 집합 하나가 만들어진다면 다다음 부터.
    }

    answer = Math.max(answer, count);
  }

  return answer * 2; // 쌍 개수여서 2배.
}
