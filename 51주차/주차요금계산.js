function solution(fees, records) {
  let answer = [];
  const parkingTime = {};
  records.forEach((v) => {
    let [time, num, io] = v.split(" ");
    let [h, m] = time.split(":");
    time = h * 1 * 60 + m * 1;
    if (!parkingTime[num]) parkingTime[num] = 0;
    // 1439는 23:59 을 분으로 바꾼것.
    if (io === "IN") parkingTime[num] += 1439 - time;
    else parkingTime[num] -= 1439 - time;
  });
  for (let [num, time] of Object.entries(parkingTime)) {
    if (time <= fees[0]) answer.push([num, fees[1]]);
    else
      answer.push([
        num,
        Math.ceil((time - fees[0]) / fees[2]) * fees[3] + fees[1],
      ]);
  }
  return answer.sort((a, b) => a[0] - b[0]).map((v) => v[1]);
}
// 프로그래머스
// 각각 출/입차 시간과 1439를 이용하면 총 주차시간을 쉽게 구할 수 있다.
