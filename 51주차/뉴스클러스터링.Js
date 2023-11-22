const set = (s) => {
  // 알파벳으로만 이루어진, 2글자씩 끊어서, 모든 문자를 대문자로 변환한 형태로 반환.
  let res = [];
  let regex = /^[a-z|A-Z]+$/;
  for (let i = 0; i < s.length - 1; i++) {
    res.push(s[i] + s[i + 1]);
  }
  res = res.filter((v) => regex.test(v));
  res = res.map((v) => v.toUpperCase());
  return res;
};
function solution(str1, str2) {
  var answer = 0;

  let [arr1, arr2] = [set(str1), set(str2)];
  if (arr1.length === 0 && arr2.length === 0) return 65536; // 공집합일경우 유사도는 1, *65536.

  let dict1 = {};
  let dict2 = {};
  let cross = 0;
  arr1.forEach((v) => {
    if (v in dict1) dict1[v] += 1;
    else dict1[v] = 1;
  });
  arr2.forEach((v) => {
    if (v in dict2) dict2[v] += 1;
    else dict2[v] = 1;
  });

  for (let v in dict1) {
    if (v in dict2) cross += Math.min(dict1[v], dict2[v]); // 개수가 더 작은 것이 교집합에 해당.
  }
  answer = cross / (arr1.length + arr2.length - cross);
  return Math.floor(answer * 65536);
}
// 프로그래머스
