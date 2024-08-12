function solution(s){
    var answer = true;
    var cnt = 0;
    
    for (i of s) {
        if (i === "p" || i === "P") {
            cnt += 1
        } else if (i === "y" || i === "Y") {
            cnt -=1
        }
        console.log(cnt)
    }
    
    if (cnt !== 0) {
        answer = false 
    }

    return answer;
}