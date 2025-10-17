# 이 파일에 게임 스크립트를 입력합니다.

# 게임에서 사용할 캐릭터를 정의합니다.
define m = Character("승객", color="#3A8DFF")
define n = Character("항공사 직원", color="#1abc9c")

# 여기에서부터 게임이 시작합니다.
label start:

    menu :
        "당신은 누구인가요?"

        "승객":
            m "와! 나의 첫 비행 경험이야"

        "항공사 직원":
            n "여러분의 안전한 비행을 위해 최선을 다하는 에포항공입니다."
           

    return





