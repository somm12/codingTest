function solution(n, t, m, timetable) {
  let times = [];
  // 시 -> 분으로 바꾸기.
  for (let v of timetable) {
    const [a, b] = v.split(":").map((v) => Number(v));
    times.push(a * 60 + b);
  }
  // 시간이 빠른 순으로 정렬. 먼저 도착해서 대기한 사람이 탑승을 빨리함.
  times.sort((a, b) => a - b);
  let currentBusTime = 540; // 초기 버스 출발시간 9:00.

  for (let i = 0; i < n; i++) {
    let possible = times.filter((v) => v <= currentBusTime).length; // 현재 버스 출발 시간에서 탈 수 있는 사람 총 수.
    if (i === n - 1) {
      // 마지막 버스라면,
      if (possible >= m) {
        // 이미 m명 이상이나 타는 상황일 때, 그 중 가장 늦는 m 번째 온사람보다 1분빨리 .
        currentBusTime = times[m - 1] - 1;
      }
    } else {
      if (possible > m) times.splice(0, m);
      // m명 보다 많은 사람이 탈 수 있으면 m명 먼저 보내기
      else times.splice(0, possible); // 자리가 남는다면, 탈 수 있는 사람 모두 태워 보내기.
      currentBusTime += t; // 다음 버스 시간 업데이트.
    }
  }

  const hour = Math.floor(currentBusTime / 60);
  const min = currentBusTime % 60;

  return (hour < 10 ? "0" + hour : hour) + ":" + (min < 10 ? "0" + min : min);
}
// 프로그래머스 카카오 기출
