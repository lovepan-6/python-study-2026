# 2주차 Day 1: 문자열 기초 (String Basics)

print("=" * 50)
print("문자열 기초 및 연결 (String Basics)")
print("=" * 50)

# [1] 문자열 연결 - 3가지 방법
print("\n[1] 문자열 연결 - 3가지 방법")
print("-" * 50)

first_name = "김"
last_name = "철수"
age = 25

# 방법 1: + 연산자
name1 = first_name + last_name
print(f"방법 1 (+): {name1}")

# 방법 2: f-string (가장 권장)
intro2 = f"제 이름은 {first_name}{last_name}이고, 나이는 {age}살입니다."
print(f"방법 2 (f-string): {intro2}")

# 방법 3: format() 메서드
intro3 = "제 이름은 {}{}이고, 나이는 {}살입니다.".format(first_name, last_name, age)
print(f"방법 3 (format()): {intro3}")

# [2] 문자열 길이
print("\n[2] 문자열 길이")
print("-" * 50)

text = "Python은 쉽고 강력합니다"
print(f"텍스트: {text}")
print(f"길이: {len(text)}")

# [3] 인덱싱 (특정 문자 접근)
print("\n[3] 인덱싱 (특정 문자 접근)")
print("-" * 50)

word = "Python"
print(f"단어: {word}")
print(f"첫 번째 문자 (인덱스 0): {word[0]}")
print(f"세 번째 문자 (인덱스 2): {word[2]}")
print(f"마지막 문자 (인덱스 -1): {word[-1]}")
print(f"끝에서 두 번째 문자 (인덱스 -2): {word[-2]}")

# [4] 슬라이싱 (여러 문자 추출)
print("\n[4] 슬라이싱 (여러 문자 추출)")
print("-" * 50)

sentence = "Hello World"
print(f"문장: {sentence}")
print(f"[0:5]: {sentence[0:5]}")        # 인덱스 0부터 4까지
print(f"[6:]: {sentence[6:]}")          # 인덱스 6부터 끝까지
print(f"[:5]: {sentence[:5]}")          # 처음부터 인덱스 4까지
print(f"[::2]: {sentence[::2]}")        # 2칸씩 간격

# [5] 문자열 반복
print("\n[5] 문자열 반복")
print("-" * 50)

print("=" * 10)
print("★" * 5)
print("Ha" * 3)

# [6] 문자열 포함 여부 확인 (in 연산자)
print("\n[6] 문자열 포함 여부 확인")
print("-" * 50)

text = "I love Python programming"
print(f"텍스트: {text}")
print(f"'Python' in text: {'Python' in text}")
print(f"'Java' in text: {'Java' in text}")
print(f"'love' in text: {'love' in text}")

# [7] 문자 하나하나 출력하기
print("\n[7] 문자 하나하나 출력하기 (반복문)")
print("-" * 50)

word = "HELLO"
print(f"단어: {word}")
print("각 문자:")
for char in word:
    print(f"  - {char}")

# [8] 문자열 비교
print("\n[8] 문자열 비교")
print("-" * 50)

str1 = "Python"
str2 = "Python"
str3 = "python"

print(f"'{str1}' == '{str2}': {str1 == str2}")    # True (같음)
print(f"'{str1}' == '{str3}': {str1 == str3}")    # False (대소문자 다름)
print(f"'{str1}' > '{str3}': {str1 > str3}")      # 사전식 순서 비교

# [9] 실습: 사용자 정보 조합
print("\n[9] 실습: 사용자 정보 조합")
print("-" * 50)

# 주석을 풀어서 직접 입력받아보세요!
# user_name = input("이름을 입력하세요: ")
# user_age = input("나이를 입력하세요: ")
# user_city = input("도시를 입력하세요: ")

# 임시 데이터 사용
user_name = "이순신"
user_age = 30
user_city = "서울"

profile = f"""
======= 사용자 프로필 =======
이름: {user_name}
나이: {user_age}
도시: {user_city}
===========================
"""
print(profile)

# [10] 여러 줄 문자열 (삼중 따옴표)
print("\n[10] 여러 줄 문자열 (삼중 따옴표)")
print("-" * 50)

poem = """
파이썬은 아름답다.
명시적인 것이 암시적인 것보다 낫다.
이것이 파이썬의 철학이다.
"""
print(poem)

print("=" * 50)
print("1주차 Day 1 완료! 다음 파일로 이동하세요.")
print("=" * 50)
