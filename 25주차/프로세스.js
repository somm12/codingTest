function solution(priorities, location) {

    let q = priorities.map((p,idx) => { 
        return { idx: idx, p: p }
    })
    let result = [];
    while (q.length != 0){
        v = q.shift() // pop 역할.
        let has = q.some(x => x.p > v.p);// 적어도 하나라도 통과하는지 테스트
        if (has) q.push(v)
        else result.push(v)// 가장 큰 우선 순위라면 결과 배열에 push
    }
   
    return result.findIndex(x => x.idx === location) + 1;
}