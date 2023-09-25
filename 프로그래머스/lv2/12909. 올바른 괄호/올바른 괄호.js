function solution(s){
    let answer = true;
    let open = 0;
    s.split('').forEach(char => {
        if (char === '(') open++;
        else open--;
        
        if (open < 0) {
            answer = false
            return;
        }
    })
    return answer && open == 0;
}