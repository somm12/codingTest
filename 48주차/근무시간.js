const solution = (data) => {
  // 데이터를 정제하고 이 함수에서 로직 작성.
  let answer = 0;

  for (let arr of data) {
    const [at, am] = arr[0].split(":").map((el) => +el);
    const [bt, bm] = arr[1].split(":").map((el) => +el);
    answer += bt * 60 + bm - (at * 60 + am);
  }

  console.log(answer);
};

/// 기본 선언
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
}); /// 기본 선언

let count = 0;
const data = [];

rl.on("line", function (line) {
  data.push(line.split(" "));
  count += 1; // data를 입력받으면 count를 증가시켜주기.

  if (count === 5) {
    // count가 5일때 rl.close()를 호출.
    rl.close();
  }
}).on("close", function () {
  // rl.close()를 호출하면 이 콜백함수로 들어오고
  solution(data); // solution을 호출 한 후
  process.exit(); // 프로세스를 종료.
});
// js로 데이터 입력받아서 풀어보기.
// 소프티어 문제.
