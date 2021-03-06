import pygame as pg

def 스프라이트생성(이미지, 위치):
    스프라이트 = pg.sprite.Sprite()
    스프라이트.image = 이미지
    스프라이트.rect = 스프라이트.image.get_rect()
    스프라이트.rect.x, 스프라이트.rect.y = 위치[0], 위치[1]
    return 스프라이트

pg.init()

실행여부 = True
화면가로길이, 화면세로길이 = 874, 987
화면 = pg.display.set_mode([화면가로길이, 화면세로길이])
pg.display.set_caption('부족들의 마음을 요리로 사로잡아라!')

#색지정
흰색 = (255, 255, 255)
검은색 = (0,0,0)

#글꼴설정
글꼴 = pg.font.SysFont('malgungothic', 25)

#게임 요소 초기화
경과시간 = 0
점수 = 0
시계 = pg.time.Clock()
현재챕터 = 1
최종챕터 = 10

요리초기위치 = [424, 248]
요리위치 = [요리초기위치[0] - 53, 요리초기위치[1] - 30]

손님가로숫자, 손님세로숫자 = 4,2

요리상태리스트 = ['전', '후']
요리리스트 = ['사료', '뼈다귀', '물']

배경이미지 = pg.image.load('img/배경.png')
배경이미지 = pg.transform.scale(배경이미지, (화면가로길이, 화면세로길이))

챕터바이미지크기 = (358, 61)
챕터바이미지 = pg.image.load('img/챕터바.png')
챕터바이미지 = pg.transform.scale(챕터바이미지, 챕터바이미지크기)

자바독이미지크기 = (238, 238)
자바독이미지 = pg.image.load('img/자바독_기본자세.png')
자바독이미지 = pg.transform.scale(자바독이미지, 자바독이미지크기)

주방테이블이미지크기 = (668, 173)
주방테이블이미지 = pg.image.load('img/주방-테이블.png')
주방테이블이미지 = pg.transform.scale(주방테이블이미지, 주방테이블이미지크기)

요리이미지크기딕셔너리 = {'사료':(106, 61), '뼈다귀':(106, 61), '물':(106, 61)}

요리이미지딕셔너리 = {}

for 요리상태 in 요리상태리스트:
    요리이미지딕셔너리[요리상태] = {}
    for 요리 in 요리리스트:
        요리이미지딕셔너리[요리상태][요리] = pg.image.load(f'img/{요리}_요리{요리상태}.png')
        요리이미지딕셔너리[요리상태][요리] = pg.transform.scale(요리이미지딕셔너리[요리상태][요리], 요리이미지크기딕셔너리[요리])

요리스프라이트 = 스프라이트생성(요리이미지딕셔너리['전']['사료'], 요리위치)

동족이미지크기 = (196, 314)
동족음식생각중이미지 = pg.image.load('img/동족_음식-생각-중.png')
동족음식생각중이미지 = pg.transform.scale(동족음식생각중이미지, 동족이미지크기)

동족스프라이트리스트 = [스프라이트생성(동족음식생각중이미지, (50+동족이미지크기[0] * j, 350+동족이미지크기[1] * i)) for i in range(손님세로숫자) for j in range(손님가로숫자)]

while 실행여부:

    if 현재챕터 <= 최종챕터:
        화면.blit(배경이미지, (0, 0))
        흐른시간 = 시계.tick(60) / 1000
        경과시간 += 흐른시간
        시간문자열 = '%02d:%02d'%(경과시간/60, 경과시간%60)
        경과시간글자 = 글꼴.render(시간문자열, True, 검은색)
        화면.blit(챕터바이미지, ((화면가로길이 - 챕터바이미지크기[0]) // 2, 7))
        화면.blit(경과시간글자, (20, 20))

        챕터문자열 = f'{현재챕터}챕터'
        챕터글자 = 글꼴.render(챕터문자열, True, 흰색)
        화면.blit(챕터글자, ((화면가로길이 - 14 * len(챕터문자열)) // 2 - 10, 20))

        점수문자열 = f'{점수}점'
        점수글자 = 글꼴.render(점수문자열, True, 검은색)
        화면.blit(점수글자, ((화면가로길이 - 14 * len(점수문자열)) - 30, 20))

        화면.blit(자바독이미지, (321, 85))
        화면.blit(주방테이블이미지, (100, 192))

        for 동족스프라이트 in 동족스프라이트리스트:
            화면.blit(동족스프라이트.image, 동족스프라이트.rect)

        for 인덱스, 요리 in enumerate(요리리스트):
            화면.blit(요리이미지딕셔너리['후'][요리], (460 + 90 * 인덱스, 280 - 요리이미지딕셔너리["후"][요리].get_height()))


        요리스프라이트.image = 요리이미지딕셔너리["전"]["사료"]

        요리스프라이트.rect.x, 요리스프라이트.rect.y = 요리위치[0], 요리위치[1]
        화면.blit(요리스프라이트.image, 요리스프라이트.rect)


    else:
        화면.fill(흰색)


    pg.display.update()
    for 이벤트 in pg.event.get():
        if 이벤트.type == pg.QUIT:
            실행여부 = False

    
pg.display.quit()