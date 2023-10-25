function solution(str1, str2) {
  var answer = 0;
  const regex = /^[a-z|A-Z]+$/; // 영어만 있는지 확인
  let arr1 = [];
  let arr2 = [];

  for (let i = 0; i < str1.length - 1; i++) {
    let tmp = str1[i] + str1[i + 1];
    tmp = tmp.toUpperCase();
    if (regex.test(tmp)) arr1.push(tmp);
  }

  for (let i = 0; i < str2.length - 1; i++) {
    let tmp = str2[i] + str2[i + 1];
    tmp = tmp.toUpperCase();
    if (regex.test(tmp)) arr2.push(tmp);
  }
  // 두개씩 끊어서 저장.

  if (arr1.length === 0 && arr2.length == 0) return 65536;

  let visited2 = new Array(arr2.length).fill(0);

  let same = [];
  for (let i = 0; i < arr1.length; i++) {
    for (let j = 0; j < arr2.length; j++) {
      if (arr1[i] === arr2[j] && visited2[j] === 0) {
        visited2[j] = 1;
        same.push(arr1[i]);
        break; // 동일한 문자열이 있을 수 있으니 break
      }
    }
  }
  const sameSize = same.length;
  const totalSize = arr1.length + arr2.length - sameSize;
  console.log(sameSize, totalSize);

  return parseInt((sameSize / totalSize) * 65536);
}
//프로그래머스.
