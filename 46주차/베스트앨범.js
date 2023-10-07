function solution(genres, plays) {
  var dict = {};
  // 장르 별로 재생된 횟수 만들기.
  genres.forEach((genre, i) => {
    dict[genre] = dict[genre] ? dict[genre] + plays[i] : plays[i];
  });
  var temp = {}; // 각 장르별 2곡씩 자르기 위한 임시 딕셔너리
  return genres
    .map((v, i) => ({ genreCnt: dict[v], cnt: plays[i], index: i })) // 장르별 재생횟수, 노래 재생 횟수, 고유번호 를 필드로 객체 생성.
    .sort((a, b) => {
      // 장르 재생, 재생, 고유번호 작은 순으로 정렬.
      if (a.genreCnt !== b.genreCnt) return b.genreCnt - a.genreCnt;
      if (a.cnt !== b.cnt) return b.cnt - a.cnt;
      return a.index - b.index;
    })
    .filter((v) => {
      // temp에 장르cnt를 key값으로 써서(각 장르당 재생 회수 다 다름), 각 장르별로 2개씩 자르기.
      if (temp[v.genreCnt] >= 2) return false;
      temp[v.genreCnt] = temp[v.genreCnt] ? temp[v.genreCnt] + 1 : 1;
      return true;
    })
    .map((v) => v.index); // 고유 번호 반환.
}
//플그머 고득점 kit 해시 문제
