function solution(fees, records) {
  var answer = [];
  // 마지막에 출차 시간이 없는 것 찾아서 records에 23:59 OUT 추가.
  let tmp = {};
  for (let r of records) {
    let num = r.split(" ")[1];
    if (!tmp[num]) tmp[num] = 1;
    else tmp[num] += 1;
  }

  let arr = Object.keys(tmp);
  for (let num of arr) {
    if (tmp[num] % 2 !== 0) records.push(`23:59 ${num} OUT`);
  }

  let time = {}; // 각 차 번호 별, 총 주차시간
  for (let r of records) {
    let [t, num, io] = r.split(" ");

    let [T, M] = t.split(":");
    T = parseInt(T);
    M = parseInt(M);

    if (io === "IN") {
      if (!time[num]) time[num] = -(T * 60 + M);
      else time[num] = time[num] - (T * 60 + M);
    } else {
      time[num] = time[num] + (T * 60 + M);
    }
  }
  // 요금 계산
  arr = Object.keys(time);
  for (let num of arr) {
    const tt = time[num];
    if (tt <= fees[0]) answer.push([num, fees[1]]);
    else {
      let cost = fees[1] + Math.ceil((tt - fees[0]) / fees[2]) * fees[3];
      answer.push([num, cost]);
    }
  }

  // 차번호가 작은 대로 정렬해주기.
  answer.sort((a, b) => a[0] - b[0]);
  return answer.map((v) => {
    return v[1];
  });
}
