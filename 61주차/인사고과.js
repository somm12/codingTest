function solution(scores) {
  var answer = 1;
  const wanho = scores[0];
  const wanhoSum = scores[0][0] + scores[0][1];
  scores.sort((a, b) => {
    if (a[0] !== b[0]) return b[0] - a[0];
    return a[1] - b[1];
  });

  let maxV = 0;
  for (let i = 0; i < scores.length; i++) {
    if (scores[i][1] < maxV) {
      if (scores[i] === wanho) {
        return -1;
      }
    } else {
      if (wanhoSum < scores[i][0] + scores[i][1]) {
        answer += 1;
      }
      maxV = Math.max(maxV, scores[i][1]);
    }
  }

  return answer;
}
// 위의 코드에서 정렬 기준을 첫번째 인덱스에만 맞춘다고 했을 때, 정렬 이후 아래와 같은 경우라면.
// [3,2] [3,1] [2,8][2,3] => 이 경우에 만약 2,3이 완호면 완호는 인센티브를 못 받게 되버림.
// 따라서 두번째 값도 오름차순 기준 정렬을 한다.
// 이미 앞의 사람보다 첫번째 점수는 작거나 같기 때문에, 두번째 점수마저 작은 경우가 생기면 제외.
// maxScore에는 두번째 점수 최댓값을 넣는다.
//
