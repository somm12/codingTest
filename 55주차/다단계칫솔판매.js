function solution(enroll, referral, seller, amount) {
  const n = enroll.length;
  var answer = Array(n + 1).fill(0);

  let dict = {};
  enroll.forEach((name, i) => (dict[name] = i + 1)); // 딕셔너리에 이름과 인덱스 매칭.
  let parent = Array(n + 1).fill(0); // 부모 노드 번호를 저장할 배열.
  parent[0] = -1;
  for (let i = 0; i < n; i++) {
    const d = enroll[i]; //자식
    const p = referral[i]; //부모

    if (p === "-") {
      // - 표시는 민호 이자 곧 루트.
      parent[dict[d]] = 0;
    } else {
      parent[dict[d]] = dict[p];
    }
  }

  seller.forEach((name, i) => {
    let node = dict[name];
    let earn = amount[i] * 100;
    while (parent[node] >= 0) {
      const tmp = parseInt(earn * 0.1);

      if (tmp >= 1) {
        // 10% 했을 때 1미만은 반복문 그만.
        answer[node] += earn - tmp;
        node = parent[node];
      } else {
        answer[node] += earn;
        break;
      }
      earn = tmp;
    }
  });
  answer = answer.slice(1, n + 1);
  return answer;
}
// 프로그래머스

// 아래는 더 쉬운 풀이.
function solution(enroll, referral, seller, amount) {
  // 숫자 번호로 매칭은 건너 뛰고, Map을 이용해서 value를 객체 형태로,
  // {referral: 부모, profit: 이익} 만들기.
  const members = new Map();
  enroll.forEach((member, i) => {
    //referral[i]는 i번째 enroll의 부모 노드라고 볼 수 있음.
    members.set(member, { referral: referral[i], profit: 0 });
  });
  seller.forEach((member, i) => {
    let curAmount = amount[i] * 100; // 번돈.
    let curMember = members.get(member); // 해당 사람의 {부모와, 이익} 객체 반환.
    while (curAmount && curMember) {
      // 더이상 부모가 없거나, 10% 뗀 이익이 1미만이면 종료.
      div = Math.floor(curAmount / 10);
      curMember.profit += curAmount - div;
      curAmount = div;
      curMember = members.get(curMember.referral); // 부모 전달.
    }
  });
  return enroll.map((member) => members.get(member).profit);
}
