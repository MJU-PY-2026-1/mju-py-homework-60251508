# 파일이름 : main.py
# 작 성 자 : 문예준

# 이름 입력 받기 

user_name = input(' 사용자 이름을 입력하세요! : ')

char_name = input(' 캐릭터 이름을 입력하세요! : ')

char_type = input(' 캐릭터 타입을 입력하세요! (스파르타형/벼락치기형/힐링공부형) : ')

target_time = int(input(' 목표 시간을 입력하세요! : '))

today_goal = float(input(' 하루 목표 시간을 입력하세요 : '))

 # 필요한 변수 만들기 

level = 1

exp = 0

ability = 50

# 잘못된 인풋 방지

if not (char_type == '스파르타형' or char_type == '벼락치기형' or char_type == '힐링공부형'):
  print('잘못된 입력입니다. 힐링공부형으로 설정합니다.')
  char_type = '힐링공부형'
  
if target_time <= 0:
  print('잘못된 목표시간. 1시간으로 설정합니다')
  target_time = 1
  
# 리스트 생성하기 

subjects = []

study_times = []

# 공부시간 입력받기 

for i in range(3) :
  subject = input(f' {i + 1}번째 과목명을 입력하시오 : ')
  study_time =  float(input(f'{subject} 공부시간을 입력하시오 : '))

  subjects.append(subject)
  study_times.append(study_time)

# 변수 계신

total_time = sum(study_times)
rate = total_time / target_time * 100
best_subject = subjects[study_times.index(max(study_times))]

study_times.sort()

# 캐릭터를 성장시키기 

if rate >= 80 :
  level +=1
  exp += 50
  ability += 10
  print('캐릭터 레벨업 성공!')

elif rate >= 50 :
  exp += 30
  ability += 5
  print(' 목표의 절반 이상 달성!')

else :
  ability -= 5
  print('목표 달성률 저조.. 공부량을 증가하세요!')


if rate >= 80 and char_type == '스파르타형' :
  exp += 20
  print('스파르타형 추가 보상 증정!')


# 결과 출력

print(f' 캐릭터 이름 : {char_name} ')
print(f' 캐릭터 타입 : {char_type} ')
print(f' 목표 시간 : {target_time} ')
print(f' 오늘의 목표 시간 : {today_goal} ')
print(f' '='*10')
print(f' 총 공부시간 : {total_time}시간')
print(f' 공부시간 정렬 : {study_times}')

(main) $ ./run.sh





























