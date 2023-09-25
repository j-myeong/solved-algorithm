function solution(s) {
    const tmp = s.split(" ");
    let max = +tmp[0];
    let min = +tmp[0];
    
    tmp.forEach(item => {
        if (+item < min) min = +item;
        if (+item > max) max = +item;
    })
    
    return `${min} ${max}`;
    // ["1", "2", ...]
}