# templates

## layout
- bootstrap을 이용해 모든 페이지에서 사용될 layout을 작성
- session['userid']에 따라 즐겨찾기 메뉴 활성화
- 지도 출력을 위한 네이버 지도 open Api키를 저장


## start_page
- session['startpoint'], session['endpoint']가 충족할 때 경로탐색이 활성화
- 네이버 지도 open API를 이용하여 출발지와 도착지가 어딘지 파악가능하도록 지도 활성화
- 텍스트를 이용한 검색기능과 지도를 직접 클릭하여 출발 도착지 설정 가능
- 경로 탐색에 필요한 정확한 위치의 주소를 session에 저장

## listpage
- 크롤링으로 받아온 출발 위치 리스트 중 선택을 하여 session['startpoint']에 저장
- 위치 리스트의 좌표로 지도에 pin으로 표시

## listpage2
- 크롤링으로 받아온 도착 위치 리스트 중 선택을 하여 session['endpoint']에 저장
- 위치 리스트의 좌표로 지도에 pin으로 표시

## listpage3
- 크롤링으로 받아온 즐겨찾기 검색 리스트 중 선택을 하여 session['point']에 저장
- 위치 리스트의 좌표로 지도에 pin으로 표시

## loginform
- form형식을 사용하여 login과 logout기능 작성
- login에 필요한 userid와 pwd가 각각 일치하는지 확인 과정

## add_member
- form형식을 사용하여 일반적인 회원가입 창을 구현
- 회원정보인 name, userid, pwd를 받아와 연결된 DB에 저장

## add_fav
- session['userid']가 None이 아닌 어떤 값이 저장되어 있을 때 활성화 되며 listpage3에서 검색한 session['point']를 가지고와 favoriteTable에 저장

## favorite
- userid와 함께 저장된 table에서 favorite_list를 불러와 빠르게 출발지나 도착지로 설정 가능하도록 구현

## routepage
- find_route에서 알아낸 경로들을 통해 버스, 지하철을 언제 어디서 탑승하여 환승 경로와 최종적인 도착시간까지 알려줄 수 있도록 구현