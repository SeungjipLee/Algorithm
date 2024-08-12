var n = 123;
var answer = 0;

for (i of n.toString()) {
    answer += Number(i);
}

console.log(answer);