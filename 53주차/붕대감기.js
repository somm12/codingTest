function solution(bandage, health, attacks) {
  let [t, x, y] = bandage;
  const maxV = health;
  let now = maxV;
  let time = 1;
  let cnt = 0;
  while (attacks.length > 0 && now > 0) {
    if (time === attacks[0][0]) {
      let [w, minus] = attacks.shift();
      now -= minus;
      cnt = 0;
    } else {
      now += x;
      cnt += 1;
      if (cnt === t) {
        //연속 시전 성공
        cnt = 0;
        now += y;
      }
      now = now < maxV ? now : maxV;
    }
    time += 1;
  }
  return now <= 0 ? -1 : now;
}
// 다른 방법.
function solution(bandage, health, attacks) {
  let [t, x, y] = bandage;
  let now = health;
  let time = 0;
  for (let i = 0; i < attacks.length; i++) {
    const diff = attacks[i][0] - time - 1; // 공격시간 전까지 붕대감기 기술로 +x 체력 회복
    now += diff * x + Math.floor(diff / t) * y;

    if (now > health) now = health;
    now -= attacks[i][1];
    if (now <= 0) return -1;
    time = attacks[i][0];
  }
  // 0 이하가 되면 -1 return
  return now;
}
// 프로그래머스 문제
