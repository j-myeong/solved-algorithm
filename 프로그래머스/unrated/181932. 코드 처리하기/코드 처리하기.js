function solution(code) {
    let answer = '';
    let mode = false; // false = 0; true = 1;
    
    for (let i = 0; i < code.length; i++) {
        if (code[i] == 1) {
            mode = !mode;
            continue;
        }
        if (!mode && i % 2 == 0) answer += code[i];
        else if (mode && i % 2 != 0) answer += code[i];
    }
    return answer || "EMPTY";
}