function solution(nums) {
  const cnt = new Set([...nums]).size;
  return Math.min(cnt, parseInt(nums.length / 2));
}
// 프로그래머스 폰켓몬 문제
