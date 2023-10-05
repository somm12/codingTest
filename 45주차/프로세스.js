function solution(priorities, location) {
  var order = [];
  let q = [];
  for (let i = 0; i < priorities.length; i++) {
    q.push([priorities[i], i]);
  }
  while (q.length > 0) {
    var v = q.shift();
    var flag = q.some((x) => x[0] > v[0]);
    if (flag) q.push(v);
    else order.push(v[1]);
  }
  // findIndex: 가장 처음에 조건에 맞는 element의 인덱스 반환
  return order.findIndex((i) => i === location) + 1;
}
// 다른 방법.
let q = priorities.map((p, idx) => {
  return { idx: idx, p: p };
});
let result = [];
while (q.length != 0) {
  v = q.shift();
  let has = q.some((x) => x.p > v.p);
  if (has) q.push(v);
  else result.push(v);
}
