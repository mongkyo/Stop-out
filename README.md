# Stopout 퀴즈

## 제출방법

- Stop-out제출용 저장소 하나씩 생성
- 파이썬 문제는 하나의 Jupyter Notebook파일에 번호와 답 코드 및 실행결과를 담아 제출
- 장고 문제는 해당 저장소의 `app`폴더에 장고 코드가 들어갈 수 있도록 설정
	- clone받을 경우 해당 폴더 내의 `app`폴더에서 `manage.py`를 실행할 수 있는 구조인지 확인
- 구글 스프레드시트 문서에 각자 주소를 제출

## 파이썬

### 1. 다음 리스트를 사용해 아래와 같은 문자열을 만들어 `girlsday_info`변수에 할당한 후, 콘솔에 내용을 출력하시오. [5점]

리스트

```python
girlsday_members = ['민아', '혜리', '유라', '소진']
```

결과 문자열

```
- 민아
- 혜리
- 유라
- 소진
```

### 2. `fruit_dict`객체를 사용해서 아래와 같은 결과값을 갖는 문자열을 만들어 `fruit_info`변수에 할당 한 후, 콘솔에 내용을 출력하시오. [10점]

- index 미출력시: -2
- 키의 대문자화 미구현시: -2
- 값의 첫 번째 글자 대문자화 미구현시: -2

```
fruit_dict = {
    'red': 'apple',
    'yellow': 'banana',
    'green': 'melon',
}
```

결과 문자열

```
[0] RED: Apple
[1] YELLOW: Banana
[2] GREEN: Melon

# 어렵다면 아래 형태를 만든다

red: apple
yellow: banana
green: melon
```

### 3. list의 `copy()`메서드가 하는 일과, `copy()`를 사용하지 않았을 때 발생할 수 있는 오류에 대한 예제 코드를 작성하시오. [10점]

- `copy()`메서드의 설명이 틀렸을 경우: -4

### 4. 1에서 30까지의 숫자 중, 3부터 시작해서 4번째마다의 숫자를 가지는 리스트를 생성하시오. [5점]

- 기본점수: 3점
- `range`를 사용한 경우: +2

결과

```
[3, 7, 11, 15, 19, 23, 27]
```

### 5. dict형 객체인 `obj`가 있다고 할 때, `obj['key']`와 `obj.get('key')`의 차이를 서술하시오. [5점]

### 6. 튜플 언패킹에 대해 서술하고, `pokemon_info` 객체를 순회할 때 튜플 언패킹을 사용하는 예제 코드를 작성하시오. [10점]

- 틀린서술: -3
- 예제코드 미작성: -7

```
pokemon_info = [
    ('피카츄', '전기 타입'),
    ('파이리', '불 타입'),
    ('꼬부기', '물 타입'),
    ('이상해씨', '풀 타입'),
]
```

### 7. 함수에서 위치인자와 키워드인자의 차이점에 대해 서술하시오. [5점]

### 8. 클래스와 인스턴스의 다음 사항들에 대해 서술하시오.

- 클래스와 인스턴스의 차이점 [2점]
- 클래스의 생성자 함수 이름 [1점]
- 클래스의 생성자 함수가 호출되는 시점은? [2점]
- 인스턴스 메서드의 `self`매개변수의 의미 [4점]

### 9. `property`를 정의하는 방법에 대해 서술하시오. [5점]

- `getter`를 만드는 방법에 대해 서술: 2점
- `setter`를 만드는 방법에 대해 서술: 3점

### 10. 아래와 같은 `User`클래스가 있다. 이 클래스를 상속받은 `Student`클래스를 정의하고, 초기화 메서드에서 `name`과 함께`age`라는 매개변수를 추가로 사용해 인스턴스의 `age`속성을 추가로 정의하도록 한다. [10점]

- (기본구현) User클래스를 상속: 1
- 초기화 메서드 재정의: +3
- 초기화 메서드에서 `super`사용: +6

```
class User:
    def __init__(self, name):
        self.name = name
```

### 11. `url`주소로부터 아래 결과를 출력한다. [10점]

> 공지사항이 추가되면 결과는 달라질 수 있으므로, 실제 게시판의 목록이 출력되는지 확인
> 
> top이라는 텍스트는 포함되어도 무관

```
url = 'http://www.leagueoflegends.co.kr/?m=news&cate=notice'
```

결과 출력

```
top[#2] 격전을 준비하세요! (수정)
top격전 참여시 불건전 행위에 대한 주의사항 안내(수정)
6월 6일(수) 서버 점검 안내
PBE 인사이드 20화(8.12 패치 편) 방송 안내
다시 돌아온 격전! 얼불져스 6/5(화) 방송 일정 안내
1일 격전 테스트에 참여해 주세요
대리 게임 등 적발 현황 262차 안내
부정행위 프로그램 제재 현황 안내
MadLife와 함께하는 입롤의 신 - 파이크편
무작위 총력전 샤코 챔피언 비활성화 안내 (정상화)
얼불져스 성적 예측 이벤트 당첨자 안내
수수께끼 피규어(시리즈 2) 할인 판매!
```

### 12. `url`주소에 있는 공지사항에 해당하는 `Notice`클래스를 만들고, 크롤링시 공지사항 하나마다 `Notice`클래스 인스턴스를 만들어 `notice_list`리스트에 추가한다. [10점]

`notice_list`를 출력한 결과

```
for notice in notice_list:
	print(notice.title)
	print(notice.date)
	print(notice.view)
	print()
```

결과

```
top[#2] 격전을 준비하세요! (수정)
2018-05-18
17,698

top격전 참여시 불건전 행위에 대한 주의사항 안내(수정)
2018-04-26
34,097

일부 클라이언트 오류 현상에 대한 안내
2018-06-06
4,928

6월 6일(수) 서버 점검 안내 (완료)
2018-06-05
38,061

PBE 인사이드 20화(8.12 패치 편) 방송 안내
2018-06-04
7,819

다시 돌아온 격전! 얼불져스 6/5(화) 방송 일정 안내
2018-06-03
13,906
...
...
...
```


### 13. runserver가 `localhost:8000`에서 입력을 받는 상태로 동작 중일 때, 브라우저에서 `http://localhost:8000/abc/` 라는 URL을 입력하면 어떤 절차를 거쳐 사용자에게 다시 화면을 보여주는지 서술하시오. [10점]

## Django [60점]

#### 모델

- 학교
	- 학교명
- 학생
	- 소속 학교 (MTO)
	- 학생 이름
	- 친한 친구 목록 (MTM)
		- 대칭적관계로 구현

#### 뷰

- 학교 목록
	- 모든 학교 목록을 출력
	- 학교 상세보기로의 링크 구현
- 학교 상세보기
	- URL이름으로 `school_id`를 사용, 해당 학교를 출력
	- 속하는 모든 학생 목록을 보여준다
		- 학생 상세보기로의 링크 구현
- 학생 목록
	- 모든 학생 목록을 출력
	- 각 학생이 다니는 학교도 함께 출력해준다
	- 학생 상세보기로의 링크 구현
- 학생 상세보기
	- URL이름으로 `student_id`를 사용, 해당 학생의 정보를 출력
	- 각 학생의 친구 목록을 출력해준다

#### 샘플 데이터

- 학교 2개 및 학생 구현
	- 서울대
		- 박보영
		- 민아
		- 아이유
		- 수지
	- 연세대 (학생 없음)

- 박보영의 친한 친구 목록에 아이유와 수지 추가
- 아이유의 친한 친구 목록에 민아 추가
- 수지의 친한 친구 목록에 아이유 추가
