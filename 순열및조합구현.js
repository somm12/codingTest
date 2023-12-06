const permut = (arr, n) => {
  let res = [];
  let visited = new Array(arr.length).fill(0);
  const perm = (temp) => {
    if (temp.length === n) {
      res.push(temp);
      return;
    }
    for (let i = 0; i < arr.length; i++) {
      if (!visited[i]) {
        visited[i] = 1;
        perm([...temp, arr[i]]);
        visited[i] = 0;
      }
    }
  };
  perm([]);
  return res;
};

const combi = (arr, n) => {
  let res = [];

  const comb = (start, temp) => {
    if (temp.length === n) {
      res.push(temp);
      return;
    } else {
      for (let i = start; i < arr.length; i++) {
        comb(i + 1, [...temp, arr[i]]);
      }
    }
  };
  comb(0, []);
  return res;
};

// console.log(permut([1, 2, 3,4], 2));

arr = combi([1, 2, 3, 4], 2);
let res = [];
for (let i = 0; i < arr.length / 2; i++) {
  let [a, b] = [arr[i], arr[arr.length - 1 - i]];
  res.push([a, b]);
  res.push([b, a]);
}
console.log(res);
