function solution(myString) {
    myString = myString.toLowerCase();
    for (let i = 0; i < myString.length; i++) {
        if (myString[i] == 'a') myString[i] == 'A';
    }
    return myString.replaceAll('a', 'A');
}