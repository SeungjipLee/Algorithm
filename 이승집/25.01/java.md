# 파이썬 -> 자바 언어 확장!

## in

st1 = "abcdefg"
st2 = "def"

```python
if st2 in st1:
    ...
```
```java
if (st1.contains(st2)) {
  ...
}
```
java에서는 타입이 같을 때에만 contains를 사용가능하다
int[] 와 ArrayList<>()끼리는 사용 못함.
```java
import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr, int[] delete_list) {
        // delete_list를 List로 변환
        ArrayList<Integer> deleteList = new ArrayList<>();
        for (int num : delete_list) {
            deleteList.add(num);
        }

        // temp에 arr[i]가 deleteList에 포함되지 않은 경우만 추가
        ArrayList<Integer> temp = new ArrayList<>();
        for (int num : arr) {
            if (!deleteList.contains(num)) {
                temp.add(num);
            }
        }

        // ArrayList를 int 배열로 변환
        int[] answer = temp.stream().mapToInt(i -> i).toArray();
        return answer;
    }
}
```

## range

1 4 7 10 13 출력력

```python
for i in range(1, 14, 3):
  print(i, end=" ")
```
```java
for (int i=1; i<14, i+=3) {
  System.out.print(i);
}
```