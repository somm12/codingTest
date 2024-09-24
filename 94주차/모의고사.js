function solution(answers) {
  var answer = [];
  const n = answers.length;
  const score = Array(4).fill(0);

  const pat = [
    [],
    [1, 2, 3, 4, 5],
    [2, 1, 2, 3, 2, 4, 2, 5],
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
  ];

  for (let i = 0; i < n; i++) {
    if (pat[1][i % pat[1].length] == answers[i]) {
      score[1] += 1;
    }
    if (pat[2][i % pat[2].length] == answers[i]) {
      score[2] += 1;
    }
    if (pat[3][i % pat[3].length] == answers[i]) {
      score[3] += 1;
    }
  }
  const maxValue = Math.max(...score);

  score.forEach((v, i) => {
    if (v === maxValue) {
      answer.push(i);
    }
  });
  return answer;
}
// 프로그래머스 모의고사 문제
