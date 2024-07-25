const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = () => {
  let answer = Infinity;
  let selectedFoods = [];

  for (let i = 0; i < 1 << n; i++) {
    let temp = [];
    let [p, f, s, v] = [0, 0, 0, 0];
    let cost = 0;

    for (let j = 0; j < n; j++) {
      if (i & (1 << j)) {
        p += food[j][0];
        f += food[j][1];
        s += food[j][2];
        v += food[j][3];
        cost += food[j][4];
        temp.push(j + 1);
      }
    }

    if (p >= minp && f >= minf && s >= mins && v >= minv) {
      if (answer >= cost) {
        if (answer > cost) selectedFoods = [];
        answer = cost;
        const f = temp.join(" ");
        selectedFoods.push(f);
      }
    }
  }

  if (answer == Infinity) console.log(-1);
  else {
    console.log(answer);

    console.log(selectedFoods.sort()[0]);
  }
};

let n = null;
let [minp, minf, mins, minv] = [null, null, null, null];
let food = [];
let cnt = 0;

rl.on("line", (line) => {
  if (!n) n = +line;
  else if (!minp) {
    [minp, minf, mins, minv] = line.split(" ").map((e) => +e);
  } else {
    food.push(line.split(" ").map((e) => +e));
    cnt += 1;
    if (cnt == n) rl.close();
  }
});

rl.on("close", () => {
  solution();
  process.exit();
});
