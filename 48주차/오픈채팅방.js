function solution(record) {
  var answer = [];
  let dict = {};
  for (let v of record) {
    const arr = v.split(" ");
    if (arr[0] !== "Leave") dict[arr[1]] = arr[2]; // uid에 해당하는 닉네임 할당.
  }

  record.map((v) => {
    const arr = v.split(" ");
    const [w, id] = [arr[0], arr[1]];
    if (w === "Enter") answer.push(`${dict[id]}님이 들어왔습니다.`);
    else if (w === "Leave") answer.push(`${dict[id]}님이 나갔습니다.`);
  });
  return answer;
}
// 프로그래머스
