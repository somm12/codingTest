function solution(numbers) {
  var answer = "5";
  answer = numbers
    .map((c) => String(c))
    .sort((a, b) => b + a - (a + b))
    .join("");

  return answer[0] === "0" ? "0" : answer; // 000..이 될 경우를 생각해서 0 반환.
}
