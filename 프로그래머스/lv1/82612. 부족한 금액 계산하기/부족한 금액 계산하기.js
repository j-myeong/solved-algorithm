function solution(price, money, count) {
    let answer = 0;
    let calPrice = price;
    for (let i = 0; i < count; i++) {
        money -= calPrice;
        calPrice += price;
    }
    return money < 0 ? -money : 0;
}