const isPrime = (num) => {
  if (num <= 1) return false;
  if (num == 2) return true;
  for (let i = 2; i < Math.sqrt(num) + 1; i++) {
    if (num % i === 0) return false;
  }
  return true;
};
function solution(n, k) {
  var answer = 0;
  let s = [];
  while (n > 0) {
    s.push((n % k).toString());
    n = parseInt(n / k);
  }
  s.reverse();
  s = s.join("");
  console.log(s);

  let arr = s.split("0");
  console.log(arr);
  for (let v of arr) {
    if (v !== "") {
      if (isPrime(parseInt(v))) answer += 1;
    }
  }

  return answer;
}
