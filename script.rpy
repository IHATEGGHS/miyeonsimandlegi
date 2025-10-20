# 캐릭터 정의
define m = Character("승객", color="#3A8DFF")
define n = Character("항공사 직원", color="#1abc9c")
define c = Character("기장", color="#F5A623")
define s = Character("승무원", color="#FF6B6B")

# 시작
label start:

    menu:
        "당신은 누구인가요?"

        "승객":
            m "와! 나의 첫 비행 경험이야."
            m "내가 비행기를 타게 되다니..."
            m "너무 설렌다."
            jump passenger_start

        "항공사 직원":
            n "여러분의 안전한 비행을 위해 최선을 다하는 에포항공입니다."
            jump forn_won


# 항공사 직원 루트
label forn_won:
    n "에포항공 직원 최모씨이다."
    n "오랜만의 출근이라 그런지 약간 들떠보인다."
    scene bg_airport_office with fade
    narrator "관제실 안, 항공사 직원은 오늘의 기상 데이터를 확인하고 있다."
    n "바람이 조금 거세지만, 기준치 이내야. 예정대로 출발 가능."
    n "엔진 점검만 마치면 탑승 절차 시작!"
    jump flight_scene


# 승객 루트
label passenger_start:
    scene bg_airport_gate with fade
    play music "bgm_airport.mp3"

    narrator "민제씨는 설레는 마음으로 탑승 게이트를 지나 비행기에 오른다."
    m "드디어 출발이네... 이번 여행은 꼭 성공적이어야 해."
    narrator "비행은 순조로워 보였다. 하지만 곧 하늘의 표정이 달라지기 시작했다..."
    jump weather_chapter


#----------------------------
# Chapter 1 : 기상 악화
#----------------------------
label weather_chapter:
    scene bg_airplane_cabin with fade
    play music "bgm_weather.mp3"

    narrator "갑자기 비행기가 크게 흔들리기 시작한다."
    c "현재 항로 상에 강한 난기류가 형성되었습니다. 승객 여러분께서는 모두 좌석에 앉아 안전벨트를 착용해 주시기 바랍니다."
    m "으악! 엄청 흔들리잖아..."
    m "이럴 땐… 침착해야 해. 안전벨트부터 확인하자."

    menu:
        "기상 악화 상황, 당신의 행동은?"

        "창밖을 바라본다":
            m "창밖이 거의 안 보여… 구름 사이로 번개가 번쩍인다."
            narrator "불안이 서서히 퍼져간다."

        "옆자리 승객에게 말을 건다":
            m "괜찮으세요? 이런 일이 자주 있대요."
            narrator "그는 억지로 미소를 짓지만 손끝이 떨리고 있었다."

    narrator "몇 분 후, 기체가 안정되며 방송이 다시 나온다."
    c "기상 악화 구역을 벗어났습니다. 불편을 드려 죄송합니다."
    narrator "잠시 안도의 숨을 내쉰 민제씨. 하지만 불안은 완전히 가시지 않았다."
    jump mechanical_chapter


#----------------------------
# Chapter 2 : 기계 결함
#----------------------------
label mechanical_chapter:
    scene bg_airplane_cabin with fade
    play music "bgm_warning.mp3"

    narrator "기내 불빛이 깜빡인다. 이어서 금속 마찰음 같은 소리가 들린다."
    m "이게 무슨 소리지...? 방금 뭔가 부딪힌 소리 같은데."
    c "승객 여러분, 현재 엔진 일부 점검 중입니다. 안전에는 문제가 없으니 침착하게 기다려 주십시오."

    menu:
        "엔진 이상 상황, 어떻게 대처할까?"

        "승무원을 불러 상황을 묻는다":
            m "혹시 무슨 일인가요?"
            s "확실하진 않지만, 작은 기계 결함으로 보입니다. 곧 확인될 거예요."
            narrator "그녀의 목소리는 침착했지만, 눈빛은 흔들리고 있었다."

        "그냥 조용히 앉아 상황을 지켜본다":
            m "괜히 소란 피우는 게 더 위험할 수도 있겠지…"
            narrator "하지만 이 불안한 정적이 너무 길게 느껴진다."

    narrator "잠시 후, 엔진음이 안정된다."
    c "이상 신호가 해제되었습니다. 비행을 계속하겠습니다."
    narrator "안도 섞인 박수가 터져 나왔다. 그러나 민제씨의 가슴속엔 어딘가 불길한 예감이 남아 있었다."
    jump crash_chapter


#----------------------------
# Chapter 3 : 추락
#----------------------------
label crash_chapter:
    scene bg_airplane_cabin_dark with fade
    play music "bgm_emergency.mp3"

    narrator "이륙 후 세 시간이 지났을 때였다."
    narrator "갑자기 기체가 급격히 하강하기 시작했다."
    c "긴급상황입니다! 엔진 출력이 떨어지고 있습니다!"
    m "뭐야, 이건 진짜 심상치 않은데?!"

    menu:
        "당신의 마지막 선택은?"

        "몸을 숙이고 머리를 보호한다":
            m "이럴 땐… 이렇게 해야 한다고 들었지!"
            narrator "민제씨는 떨리는 손으로 머리를 감싸며 의자 밑으로 몸을 웅크렸다."

        "휴대폰을 쥐고 가족에게 메시지를 남긴다":
            m "…엄마, 아빠… 사랑해요."
            narrator "손끝이 미세하게 떨리며 화면이 흐릿해진다."

    scene bg_white with fade
    stop music fadeout 2.0
    narrator "강한 충격과 함께 모든 게 멈췄다."
    pause 2.0
    jump aftermath


#----------------------------
# Chapter 4 : 사고 후 - 에어포렌식
#----------------------------
label aftermath:
    scene bg_hospital with fade
    play music "bgm_calm.mp3"

    narrator "눈을 떴을 때, 낯선 병실 천장이 보였다."
    m "여긴… 어디지…?"
    s "정신이 드세요? 구조팀이 바로 도착했어요."
    narrator "민제씨는 머릿속이 멍했지만, 어렴풋이 사고의 순간을 떠올렸다."
    m "왜 그런 사고가 난 걸까… 무슨 원인이었을까?"

    narrator "며칠 후,






