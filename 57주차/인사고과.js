function solution(scores) {
  var answer = 1;
  let maxScore = 0; // 가장 큰 동료평가점수(2번째 원소)
  let wanhoSum = scores[0][0] + scores[0][1]; // 완호 점수합.
  let wanho = scores[0]; // 완호 점수표

  scores.sort((a, b) => {
    // 정렬 결과, 1번째 원소는 이미 큰게 와있으니, 2번째 원소마저 작은지 알아내어 인센티브X 인지 확인.
    // 1번째 원소 기준, 내림차순 정렬. 2번째 원소기준 오름차순 정렬.
    if (a[0] !== b[0]) return b[0] - a[0];
    return a[1] - b[1];
  });

  for (let score of scores) {
    if (score[1] < maxScore) {
      // 2번째 원소도 작다면,
      if (score === wanho) return -1; // 해당 원소가 완호면 -1(인센티브 못받음.)
    } else {
      // 인센티브 받음.
      maxScore = Math.max(maxScore, score[1]); // 2번째 원소 최댓값 업데이트.
      if (score[0] + score[1] > wanhoSum) {
        // 원소의 합이 완호 보다 크면 등수 +1(같은 점수면 같은 등수)
        answer += 1;
      }
    }
  }
  return answer;
}
