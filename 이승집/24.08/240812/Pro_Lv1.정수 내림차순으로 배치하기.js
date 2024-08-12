var n = 118372;
var answer = "";
var mid = [];

for (i of n.toString()) {
    mid.push(Number(i));    
}

mid.sort().reverse()
console.log(mid);

for (i of mid) {
    answer += i;
}

console.log(answer);