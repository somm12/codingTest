var fs = require("fs");
var input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

var n = parseInt(input[0]);
var maps = input.slice(1);

var visited = [];
var dx = [-1, 1, 0, 0],
  dy = [0, 0, 1, -1];
var result = "";

let answer = [];
let total = 0;
let row = maps.length;
let col = maps.length;

for (let x = 0; x < row; x++) {
  let tmp = [];
  for (let y = 0; y < col; y++) {
    tmp.push(0);
  }
  visited.push(tmp);
}

function counting(x, y) {
  let q = [[x, y]];
  visited[x][y] = 1;
  let cnt = 1;
  while (q.length > 0) {
    let [x, y] = q.shift();
    for (let i = 0; i < 4; i++) {
      let nx = x + dx[i];
      let ny = y + dy[i];
      if (
        0 <= nx &&
        nx < n &&
        0 <= ny &&
        ny < n &&
        !visited[nx][ny] &&
        maps[nx][ny] === "1"
      ) {
        visited[nx][ny] = 1;
        q.push([nx, ny]);
        cnt += 1;
      }
    }
  }
  return cnt;
}
for (let x = 0; x < n; x++) {
  for (let y = 0; y < n; y++) {
    if (!visited[x][y] && maps[x][y] === "1") {
      let cnt = counting(x, y);
      answer.push(cnt);
      total += 1;
    }
  }
}

result = answer
  .sort(function (a, b) {
    return a - b;
  })
  .reduce(function (acc, v) {
    return acc + v + "\n";
  }, "");
console.log(total + "\n" + result);
