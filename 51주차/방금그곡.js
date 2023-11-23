function solution(m, musicinfos) {
  var answer = [];
  let arr = ["C#", "D#", "F#", "G#", "A#"];

  for (let v of arr) {
    m = m.replaceAll(v, v[0].toLowerCase());
  }

  musicinfos.forEach((v, idx) => {
    let [st, et, title, music] = v.split(",");
    let [sh, sm] = st.split(":").map((e) => +e);
    let [eh, em] = et.split(":").map((e) => +e);
    let time = eh * 60 + em - (sh * 60 + sm);

    for (let tmp of arr) {
      music = music.replaceAll(tmp, tmp[0].toLowerCase());
    }
    let str =
      music.repeat(parseInt(time / music.length)) +
      music.slice(0, time % music.length);
    if (str.includes(m)) answer.push([title, time, idx]);
  });

  if (answer.length === 0) return "(None)";

  answer.sort((a, b) => {
    if (a[1] !== b[1]) return b[1] - a[1];
    return a[2] - b[2];
  });
  return answer[0][0];
}
// 프로그래머스
// #을 다른 문자열로 치환.
