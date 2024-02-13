function solution(play_time, adv_time, logs) {
  const pt = calculateTime(play_time);
  const at = calculateTime(adv_time); // 광고 시간 초로 변환.
  const times = new Array(pt).fill(0);

  logs.forEach((log) => {
    // 각 시간대 별로 시작 종료 시간 표시. -> 누적합을 통해서 각 시간대별로 시청자수를 구할 수 있음.
    const [start, end] = log.split("-");
    const ws = calculateTime(start);
    const we = calculateTime(end);
    times[ws]++;
    times[we]--;
  });

  for (
    let i = 1;
    i <= pt;
    i++ // 매 초당, 시청자 수 계산
  )
    times[i] += times[i - 1];

  for (
    let i = 1;
    i <= pt;
    i++ // 누적 재생 횟수 계산
  )
    times[i] += times[i - 1];
  // times 배열은 인덱스 0부터 시작하므로 -1 해주기.
  let sum = times[at - 1]; // 0이 시작시간일 때, 누적재생횟수
  let idx = 0;

  for (let i = at - 1; i < pt; i++) {
    if (sum < times[i] - times[i - at]) {
      // 구간별 재생횟수. 더 큰 누적 재생횟수라면 Update

      sum = times[i] - times[i - at];
      idx = i - at + 1;
    }
  }

  return formatterTime(idx);
}

const calculateTime = (time) => {
  // 시간 - > 초
  const HHMMSS = time.split(":");
  const amount = HHMMSS[0] * 3600 + HHMMSS[1] * 60 + HHMMSS[2] * 1;
  return amount;
};

const formatterTime = (time) => {
  // 초 - > 시간
  let HH = (time / 3600) >> 0;
  let MM = ((time / 60) >> 0) % 60;
  let SS = time % 60;

  HH = HH > 9 ? HH : "0" + HH;
  MM = MM > 9 ? MM : "0" + MM;
  SS = SS > 9 ? SS : "0" + SS;

  return `${HH}:${MM}:${SS}`;
};
