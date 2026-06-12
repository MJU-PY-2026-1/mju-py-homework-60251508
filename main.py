# 파일이름 : main.py
# 작 성 자 : 문예준

import random

char_name = ""
char_type = "느긋냥이형"
level = 1

study_records = []

analysis_done = False
file_name = 'study_records.txt'

reward_quotes = [
    '나를 무너뜨리지 못하는 고난은 나를 더 강하게 만든다',
    '높이 오르려는 사람은 먼저 자기 자신을 이겨내야 한다',
    '오늘의 어려움은 더 단단한 나를 만드는 과정이다',
    '자기 자신을 믿는 사람은 쉽게 흔들리지 않는다',
    '성장은 편안함이 아니라 극복에서 시작된다',
    '포기하지 않는 사람은 결국 자기만의 길을 만든다',
]

def show_menu():
    print('\n'+'='*60)
    print('고양이와 함꼐하는 공부 성장 프로그램')
    print('='*60)
    print('1. 나의 캐릭터 만들기')
    print('2. 오늘의 공부 기록 추가')
    print('3. 내 캐릭터 및 기록 조회')
    print('4. 내 달성률 보기 및 보상 받기')
    print('5. 공부 기록 파일 저장')
    print('6. 프로그램 종료')

def input_basic_info():
    global char_name,char_type

    print('\n[캐릭터 생성]')
    char_name = input('캐릭터 이름을 입력하세요:')

    print('\n[고양이 공부 타입 선택]')
    print('1. 몰입냥이형 - 한 과목 오래 깊게 하는 타입')
    print('2. 닌자냥이형 - 짧은 시간 동안 집중하는 타입')
    print('3. 스파르타냥이형 - 강하게 밀어붙이는 타입')
    print('4. 느긋냥이형 - 무리하지않고 공부하는 타입')

    choice = input('공부타입 번호를 입력하세요 : ')

    if choice == '1':
        char_type = '몰입냥이형'
    elif choice == '2':
        char_type = '닌자냥이형'
    elif choice == '3':
        char_type = '스파르타냥이형'
    elif choice == '4':
        char_type = '느긋냥이형'
    else:
        print('잘못된 입력입니다. 기본타입인 느긋냥이형으로 설정합니다.')
        char_type = '느긋냥이형'

    print('\n 캐릭터 생성이 완료되었습니다.')
    print('캐릭터 이름 :',char_name)
    print('공부타입 :',char_type)

def get_result(rate):
    if rate >= 100:
        return '성공'
    elif rate >=70:
        return '보통'
    elif rate >= 0:
        return '부족'
    else:
        return '미실시'
    
def input_study_record():
    global analysis_done

    if char_name == '':
        print('\n캐릭터를 먼저 생성해야합니다.')
        return
    print('\n[오늘의 공부 기록 추가]')

    date = input('날짜를 입려하세요 예) 6/12 : ')
    subject = input('공부한 과목명을 입력하세요 :')
    today_goal = input('오늘의 공부 목표를 입력하세요 :')

    try:
        goal_time = float(input(subject+ '과목 목표 시간을 입력하세요 :'))
        study_time = float(input(subject + '실제 공부 시간을 입력하세요 :'))

        if goal_time <=0:
            print('목표 시간은 0보다 커야 합니다. 기본값 1시간으로 설정합니다.')
            goal_time = 1.0

        if study_time <0:
            print('목표 시간은 0보다 커야합니다. 기본값 1시간으로 설정합니다.')
            study_time = 0.0
        rate = study_time / goal_time*100
        result = get_result(rate)

        record = [date,subject,today_goal,goal_time,study_time,round(rate,1),result]
        study_records.append(record)

        analysis_done = False

        print('\n 공부 기록이 저장되었습니다.')
        print('저장된 기록:',record)

    except ValueError:
        print('숫자를 입력해야 하는 곳에 문자를 입력했습니다.')
        print('공부 기록 추가에 실패했습니다.')

def show_character_art():
    if char_type == '몰입냥이형':
        print("       /\\_/\\")
        print("       ( -.- )")
        print("       / >[책]")
        print("       몰입냥이")

    elif char_type == '닌자냥이형':
        print("       /\\_/\\")
        print("       ( o_o )")
        print("       / >[별]")
        print("       닌자냥이")

    elif char_type == "스파르타냥이형":
        print("       /\\_/\\")
        print("       ( >_< )")
        print("       / >[불]")
        print("     스파르타냥이")

    else:
        print("       /\\_/\\")
        print("       ( o.o )")
        print("       / >[휴식]")
        print("       느긋냥이")

def show_records():
    print('\n'+'='*100)
    print('캐릭터 상태창 및 전체 공부 기록')
    print('='*100)

    if char_name != '' :
        show_character_art()
        print('\n[캐릭터 정보]')
        print('캐릭터 이름:',char_name)
        print('공부 타입:',char_type)
        print('레벨:',level)
    else:
        print('아직 생성된 캐릭터가 없습니다.')

    print('\n[전체 공부 기록]')

    if len(study_records) == 0:
        print('아직 입력된 공부 기록이 없습니다.')
        return 
    
    print('-'*100)
    print('번호\t날짜\t\t과목명\t\t오늘의 목표\t\t목표시간\t공부시간\t달성률\t결과')
    print('-'*100)

    for i in range(len(study_records)):
        print(i+1,end='\t')

        for j in range(len(study_records[i])):
            print(study_records[i][j],end='\t\t')

        print()

    print('-'*100)

    print('총 공부시간 :',round(calculate_total_time(),1),'시간')
    print('평균 달성률:',round(calculate_average_rate(),1),'%')

def calculate_total_time():
    total=0

    for record in study_records:
        total+=record[4] 

    return total

def calculate_average_rate():
    if len(study_records)==0:
        return 0 

    total_rate = 0

    for record in study_records:
        total_rate += record[5]

    return total_rate/len(study_records)

def get_reward_message(avg_rate):
    if avg_rate >= 100:
        return '최종 퀘스트 성공! 오늘의 보상은 맛있는 식사와 충분한 휴식입니다.'
    elif avg_rate >= 80:
        return '목표 달성에 거의 성공했습니다! 디저트 또는 30분 자유시간을 보상으로 주세요'
    elif avg_rate >= 50:
        return ' 절반 이상 달성했습니다! 좋아하는 음료 한 잔을 보상으로 주세요.'

    elif avg_rate >0:
        return '오늘은 목표에 부족했습니다. 내일 다시 도전해보세요'
    else:
        return '아직 공부 기록이 부족합니다.'

def grow_character(avg_rate):
    global level

    if avg_rate >= 100:
        level += 2
        print('캐릭터가 크게 성장했습니다! 레벨이 2 증가했습니다.')
    elif avg_rate >= 70:
        level +=1
        print('캐릭터가 성장했습니다! 레벨이 1 증가했습니다.')
    else:
        print('이번에는 레벨이 오르지 않았습니다.')   

def analyze_study():
    global analysis_done

    print('\n[공부 달성률 분석 및 보상 받기]')

    if char_name == '':
        print('캐릭터를 먼저 생성해주세요.')
        return
    
    if len(study_records) == 0:
        print('공부한 기록을 먼저 입력해주세요.')
        return
    
    total_time = calculate_total_time()
    avg_rate = calculate_average_rate()
    reward = get_reward_message(avg_rate)
    quote = random.choice(reward_quotes)
    
    print('캐릭터 이름 :', char_name)
    print('공부 타입:',char_type)
    print('총 공부 시간:',round(total_time,1),'시간')
    print('평균 목표 달성률:',round(avg_rate,1),'%')

    if analysis_done == False:
        grow_character(avg_rate)
        analysis_done = True

    else:
        print('이미 분석을 완료했습니다. 새 공부 기록을 입력하면 다시 분석할 수 있습니다.')

    print('\n[보상 메세지]')
    print(reward)

    print('\n[오늘의 니체 공부 명언]')
    print(quote)
    
    print('\n[현재 레벨]')
    print('레벨:',level)

def save_records():
    print('\n[공부 기록 파일 저장]')

    if len(study_records)==0:
        print('저장할 공부 기록이 없습니다.')
        return
    
    with open(file_name,'w',encoding = 'utf-8') as file:
        file.write('날짜|과목명|오늘의 목표|과목 목표 시간|공부시간|달성률|결과\n')

        for record in study_records:
            line = ''

            for i in range(len(record)):
                line += str(record[i])

                if i != len(record)-1:
                    line += '|'

            file.write(line+'\n')

    print(file_name,'파일로 저장되었습니다.')

def load_records_auto():
    global study_records

    try:
        with open(file_name,'r',encoding = 'utf-8') as file:
            lines = file.readlines()

        study_records = []

        for i in range(1,len(lines)):
            line = lines[i].strip()

            if line != '':
                data = line.split('|')

                if len(data)==7:
                    record = [
                        data[0],
                        data[1],
                        data[2],
                        float(data[3]),
                        float(data[4]), 
                        float(data[5]),
                        data[6]

                    ]

                    study_records.append(record)

        if len(study_records)>0:
            print('이전에 저장된 공부기록', len(study_records),'개를 자동으로 불러왔습니다.')

    except FileNotFoundError:
        pass
    except ValueError:
        print('저장된 파일의 형식이 올바르지 않아 자동으로 불러오기에 실패했습니다.')


print('='*65) 
print('고양이와 함꼐하는 공부 성장 프로그램')
print('고양이 캐릭터와 함께 공부 기록을 입력하고 성장시킬 수 있습니다.')
print('='*65)

load_records_auto()

while True:
    show_menu()

    choice = input('메뉴를 선택하세요 :')

    if choice == '1':
        input_basic_info()

    elif choice == '2':
        input_study_record()

    elif choice == '3':
        show_records()
    
    elif choice == '4':
        analyze_study()

    elif choice == '5':
        save_records()

    elif choice == '6':
        if len(study_records)>0:
            print('\n 종료 전 공부 기록을 자동 저장합니다.')
            save_records()

        print('프로그램을 종료합니다. 오늘도 공부하느라 수고하셨습니다.')
        break

    else:
        print('잘못된 입력입니다. 1~6중에서 선택하세요.') 


















