function solution(word) {
  var answer = 0;
  const dict = {};
  let cnt = 1;
  const arr = ["A", "E", "I", "O", "U"];

  const dfs = (res) => {
    if (res.length > 5) return;
    if (res.length > 0) {
      dict[res] = cnt;
      cnt += 1;
    }
    for (const v of arr) {
      dfs(res + v);
    }
  };
  dfs("");

  return dict[word];
}
