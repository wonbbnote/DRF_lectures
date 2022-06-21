# DRF_lectures


## 0615_1일차 과제
### 1. args, kwargs를 사용하는 예제 코드


    def kakao(*args, **kwargs):
        for arg in args:
            print(arg, end=", ")

        for key, value in kwargs.items():
            print(f"{key} -> {value}")


    #kakao("Ryan", "Apeach", "Tube", "Muzi", "Neo")
    #kakao(friend1="Ryan", friend2="Apeach", new_friend="Chunsik")
    kakao("Ryan", "Apeach", new_friend="Chunsik")



### 2. mutable과 immutable은 어떤 특성이 있고, 어떤 자료형이 어디에 해당하는지 서술
- immutable한 객체: 다른 객체에 변수를 할당해줄때 값(value)을 집어넣음 → string, tuple, int
- mutable한 객체: 변수할당 시 주소값을 집어넣음 -> 한 변수에만 값을 넣어도 mutable도 바뀜 → set, list, dictionary

### 3. DB Field에서 사용되는 Key 종류와 특징 서술
- Primary key (PK, 기본키): 후보키에서 선택된 키, 기본키로 선택된 속성(attribute)은 동일한 값이 들어갈 수 없다. (테이블의 각 행을 구별하는 역할)
  → NULL 값이 들어갈 수 없으며, 오직 한개만 지정할 수 있다.    
- Unique key:  테이블 내 항상 유일해야 하는 값. 중복을 허용하지 않는다. 해당 칼럼에 입력되는 데이터가 각각 유일하다는 것을 보장하기 위한 제약조건 NULL 값도 허용됨
- Foreign key(외래키): 어떤 테이블(relation)간의 기본키를 참조하는 속성. 테이블 간의 관계를 나타내기 위해서 사용  
  → 참조될 테이블이 먼저 만들어지고 참조하는 테이블에 값이 입력됨 (참조될 열의 값은 참조될 테이블에서 기본키(PK)로 설정되어 있어야 함)

<그외?!>
- Candidate key(후보키): 유일성과 최소성을 만족하는 키, 기본키가 될 수 있는 후보가 됨.
- Alternate key (대체키): 후보 키 중 기본 키로 선택되지 않은 키
- Super key: 유일성 만족하는 키

### 4. django에서 queryset과 object는 어떻게 다른지 서술
    
Queryset이란 Django ORM에서 제공하는 데이터 타입으로, 데이터베이스에서 전달받은 객체 목록 (list)이다. (DB에서는 row를 의미한다)
(구조는 list와 같지만, 파이썬의 기본 자료구조가 아니기 때문에 파이썬 파일에서 읽고 쓰기 위해서는 자료형 변환을 해줘야 함)
> A `QuerySet` represents a collection of objects from your database
    
objects는 ModelManager이며 Database와 Model 사이의 인터페이스 역할을 하고 이때 반환되는 객체가 QuerySet이다. (추가되는 데이터를 레코드, 오브젝트라고도 함)
>`objects`is a reference to the model's Manager, whose sole purpose is to handle the database queries to retrieve the required data from a database.


