var n = 12345;

var answer = [];

for (i of n.toString()) {
    answer.push(Number(i));
}

answer.reverse();
console.log(answer);