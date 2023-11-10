function solution(survey, choices) {
  let dict = {};
  const types = ["RT", "CF", "JM", "AN"];

  types.forEach((v) => v.split("").forEach((v) => (dict[v] = 0))); //딕셔너리에 초기화.

  choices.forEach((v, i) => {
    dict[v > 4 ? survey[i][1] : survey[i][0]] += Math.abs(v - 4);
  }); // 567 은 오른쪽 유형에 점수 획득, 123은 왼쪽 유형에 점수 획득.

  // 점수가 더 높은 유형이 선택되고, 같다면 사전순. 이미 types에서 사전순이므로, a반환.
  return types.map(([a, b]) => (dict[b] > dict[a] ? b : a)).join("");
}
// 프로그래머스 카카오 인턴십문제.
