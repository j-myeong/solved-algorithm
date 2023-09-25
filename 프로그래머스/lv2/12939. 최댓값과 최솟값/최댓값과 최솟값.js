function solution(s) {
    let max;
    let min;
    s.split(" ").forEach((data, idx) => {
        if (idx == 0) {
            max = +data;
            min = +data;
        }
        else if (max < +data) max = +data;
        else if (min > +data) min = +data;
    });
    return min + " " + max
}