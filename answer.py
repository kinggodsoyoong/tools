import math
##################################################
#             물리학 실험 계산기v1.0             #
#          Made by 소융과 17학번 박성욱          #
##################################################

print('#' * 50)
print('#' + ' ' * 13 + '물리학 실험 계산기v1.0' + ' ' * 13 + '#')
print('#' + ' ' * 10 + 'Made by 소융과 17학번 박성욱' + ' ' * 10 + '#')
print('#' * 50 + '\n')

option = input('실험 번호를 입력하시오(1~11): ')

if option == '1':
    print('#' * 50)
    print('#' + ' ' * 14 + '자유낙하 실험 계산기' + ' ' * 14 + '#')
    print('#' * 50 + '\n')
    h = float(input('높이 h를 입력하시오: '))
    m = float(input('구슬의 무게를 입력하시오: '))
    r = float(input('구슬의 반지름을 입력하시오: '))
    t1 = float(input('1회 측정값을 입력하시오: '))
    t2 = float(input('2회 측정값을 입력하시오: '))
    t3 = float(input('3회 측정값을 입력하시오: '))
    print('t 평균값은',str((t1+t2+t3)/3)+'입니다.')

elif option == '2':
    print('#' * 50)
    print('#' + ' ' * 14 + '에어트랙 실험 계산기' + ' ' * 14 + '#')
    print('#' * 50 + '\n')
    D = float(input('포토게이트 사이의 거리 D를 입력하시오: '))
    h = float(input('받침목의 높이 h를 입력하시오: '))
    d = float(input('Air Track 다리 사이의 길이 d를 입력하시오: '))
    print('sinΘ =',str(h/d))


elif option == '3':
    print('#' * 50)
    print('#' + ' ' * 15 + '포물선 실험 계산기' + ' ' * 15 + '#')
    print('#' * 50 + '\n')

    ang = float(input('각도를 입력하시오(원래 값 라디안 X): '))  # 각도값 입력
    v0 = float(input('V0 값을 입력하시오: '))  # 초기 속도 입력
    angle = ang / 180 * math.pi  # ang에서 받은 각도값 라디안으로 변환
    print('t = ' + str(2 * v0 * round(math.sin(angle), 3) / 9.8))  # t값 계산 및 출력
    print('x = ' + str(v0 * v0 * round(math.sin(2 * angle), 3) / 9.8))  # x값 계산 및 출력
    print('y = ' + str(v0 * v0 * round(math.sin(angle), 3) * round(math.sin(angle), 3) / 2 / 9.8))  # y값 계산 및 출력

elif option == '4':
    print(' ')

elif option == '5':
    print(' ')

elif option == '6':
    print(' ')

elif option == '7':
    print(' ')

elif option == '8':
    print(' ')

elif option == '9':
    print(' ')

elif option == '10':
    print(' ')

elif option == '11':
    print(' ')

else :
    print('올바른 값을 입력하시오.')