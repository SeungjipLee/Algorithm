// 자연수 n이 주어졌을 때, n의 다음 큰 숫자는 다음과 같이 정의 합니다.

// 조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
// 조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
// 조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.
// 예를 들어서 78(1001110)의 다음 큰 숫자는 83(1010011)입니다.

// 자연수 n이 매개변수로 주어질 때, n의 다음 큰 숫자를 return 하는 
// solution 함수를 완성해주세요.

// 제한 사항
// n은 1,000,000 이하의 자연수 입니다.


function solution(n) {
  var answer = 0;
  const count = (num) => num.toString(2).split('').filter((number) => number === '1').length  // 2진수로 바꾸기
  let next = n+1
  const jinsu = count(n)
  // 문자열을 하나씩 비교하며 1인것만 찾아서 넣기
  // const oneCount = jinsu.split('').filter((number) => number === '1').length
  // console.log(one)
  // const check = 0
  while (count(next) !== jinsu) {
    next += 1
  }
  
  return next;
}
solution(78)