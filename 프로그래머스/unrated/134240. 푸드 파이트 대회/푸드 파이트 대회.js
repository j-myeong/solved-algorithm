function solution(food) {
    let answer = '';
    for (let i = 1; i < food.length; i++) {
        if (food[i] < 2) continue;
        for (let j = 0; j < Math.floor(food[i] / 2); j++) answer += i;
    }
    answer += 0;
    for (let i = food.length - 1; i >= 1; i--) {
        if (food[i] < 2) continue;
        for (let j = 0; j < Math.floor(food[i] / 2); j++) answer += i;
    }
    return answer;
}