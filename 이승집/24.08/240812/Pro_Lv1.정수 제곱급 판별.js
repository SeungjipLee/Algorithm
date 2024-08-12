var n = 121;

var answer;
var m = n**(1/2);

if (parseInt(m) - m === 0) {
    answer = (m+1)**2;
} else {
    answer = -1;
}
