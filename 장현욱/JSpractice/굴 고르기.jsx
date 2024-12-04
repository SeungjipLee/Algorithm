function solution(k, tangerine) {
  var answer = 0;
  var now = 0
  var dic = {}
  // 딕셔너리에 정렬
  for (var key of tangerine) {
      if(dic[key]){
          dic[key] += 1 // 키가 없으면 +1
      } else {
          dic[key] = 1 // 키가 있다면 새로 생성
      }
  }
  
  var appleList = Object.entries(dic).sort((a,b) => b[1]-a[1])
  .map(([key,value]) => (value))
  
  for (var apple of appleList) {
      answer += 1  // 한종류당 카운트 1
      now += apple // 갯수 더하기
      if (now >= k) {
          return answer
      } 
  }
  
  return answer;
}