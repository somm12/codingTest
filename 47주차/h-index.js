function solution(citations) {
  var answer = -1;

  const n = citations.length;
  citations.sort((a, b) => a - b);
  for (let i = citations[n - 1]; i >= 0; i--) {
    // 인용된 가장 큰값부터 하나씩 체크하기.
    let h = i;
    let cnt = 0;
    for (let j = n - 1; j >= 0; j--) {
      if (citations[j] >= h) cnt += 1; // h번이상 인용되었다면 +1.
    }
    if (cnt >= h) answer = Math.max(answer, h); // cnt가 h편 이상이라면, answer update.
  }

  return answer;
}
// h번이상 인용된 것이 h편이상, 나머지가 h번이하 인용. h의 최댓값.
// => citiations 중에서 가장 큰 값부터 확인.
