function solution(cacheSize, cities) {
  var answer = 0;
  if (cacheSize === 0) return 5 * cities.length;
  let cache = [];
  for (let c of cities) {
    c = c.toLowerCase();
    if (cache.includes(c)) {
      //LRU 기반.
      answer += 1;
      let idx = cache.indexOf(c); // 해당 도시 의 인덱스 반환.
      cache.splice(idx, 1); // 삭제하기.
      cache.push(c); // 다시 맨 뒤로 추가.
    } else {
      answer += 5;
      if (cache.length < cacheSize) cache.push(c);
      else {
        cache.shift();
        cache.push(c);
      }
    }
  }
  return answer;
} // 프로그래머스 카카오 - 캐시.
