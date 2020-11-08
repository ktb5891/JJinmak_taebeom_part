from flask import Flask, render_template, request, redirect, url_for, session
from Function import db3
from Function import spot
from Function import make_candidate_list
from Function import make_info_list
from Function import select_final_route
from Function import find_route
from Function import favoriteTable as ft
# import db3
# import favoriteTable as ft
# import spot
# import make_candidate_list
# import make_info_list
# import select_final_route
# from find_route import find_all_of_route


app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/', methods=["POST", "GET"])
def index():
    session['startpoint'] = None
    session['endpoint'] = None
    session['point'] = None

    if session['startpoint'] or session['endpoint']:
        if session['startpoint'] and (not session['endpoint']):
            print(session)
            startpoint = session['startpoint']
            return render_template('start_page.html', startpoint=startpoint)
        elif session['endpoint'] and (not session['startpoint']):
            print(session)
            endpoint = session['endpoint']
            return render_template('start_page.html', endpoint=endpoint)
        else:
            startpoint = session['startpoint']
            endpoint = session['endpoint']
            return render_template('start_page.html', startpoint=startpoint, endpoint=endpoint)
    # if request.method == "POST":
        # startpoint = request.form['startpoint']
        # endpoint = request.form['endpoint']
    else:
        print(session)
        return render_template('start_page.html')


@app.route('/login')
def login():
    return render_template('loginform.html')


@app.route('/login_pro', methods=['POST'])
def login_pro():
    userid = request.form['userid']
    pwd = request.form['pwd']
    print(session)
    if db3.member(userid) and db3.member(userid)['pwd'] == pwd:
        session['userid'] = userid
        return redirect('/')
    else:
        return render_template('loginform.html')


@app.route('/log_out')
def log_out():
    session.pop('userid', None)

    print(session)
    return redirect('/')


@app.route('/add_member')
def add_member():
    return render_template('add_member.html')


@app.route('/add_member_pro', methods=['POST'])
def add_member_pro():
    userid = request.form['userid']
    userName = request.form['userName']
    pwd = request.form['pwd']

    if db3.member(userid):
        return render_template('layout.html')
    else:
        db3.add_member(userid, userName, pwd)
        return render_template('loginform.html')


@app.route('/list', methods=['POST'])
def list():
    # session['startpoint'] = request.form['startpoint']
    # startpoint = session['startpoint']
    startpoint = request.form['startpoint']
    candidate_list1 = make_candidate_list.find_candidate(startpoint)
    print('aaaa',candidate_list1)
    xy_list=[]
    for i in candidate_list1:
        temp_list=make_info_list.make_info_list(i['title'],i['address'])
        try:
            x,y=make_info_list.find_xy(temp_list)
            xy_list.append([float(y),float(x)])
        except:
            xy_list.append([0.00000000000001,0.00000000000001])
    print(len(xy_list))
    len_list = len(xy_list)
    return render_template('listpage.html', candidate_list1=candidate_list1,xy_list = xy_list, len_list = len_list)


@app.route('/list_pro', methods=['POST'])
def get_list():
    startpoint = request.form['startpoint']
    print(startpoint)
    session['startpoint'] = startpoint
    print(session)
    return render_template('start_page.html', startpoint=startpoint)


@app.route('/list2', methods=['POST'])
def list2():
    endpoint = request.form['endpoint']
    candidate_list2 = make_candidate_list.find_candidate(endpoint)
    xy_list=[]
    for i in candidate_list2:
        temp_list=make_info_list.make_info_list(i['title'],i['address'])
        try:
            x,y=make_info_list.find_xy(temp_list)
            xy_list.append([float(y),float(x)])
        except:
            xy_list.append([0.00000000000001,0.00000000000001])
    print(len(xy_list))
    len_list = len(xy_list)
    return render_template('listpage2.html', candidate_list2=candidate_list2,xy_list = xy_list, len_list = len_list)


@app.route('/list_pro2', methods=['POST'])
def get_list2():
    endpoint = request.form['endpoint']
    session['endpoint'] = endpoint
    print(session)
    return render_template('start_page.html', endpoint=endpoint)

@app.route('/list3', methods=['POST'])
def list3():
    point = request.form['point']
    candidate_list3 = make_candidate_list.find_candidate(point)
    xy_list=[]
    for i in candidate_list3:
        temp_list=make_info_list.make_info_list(i['title'],i['address'])
        try:
            x,y=make_info_list.find_xy(temp_list)
            xy_list.append([float(y),float(x)])
        except:
            xy_list.append([0.00000000000001,0.00000000000001])
    print(len(xy_list))
    len_list = len(xy_list)
    return render_template('listpage3.html', candidate_list3=candidate_list3, xy_list = xy_list, len_list = len_list)


@app.route('/list_pro3', methods=['POST'])
def get_list3():
    point = request.form['point']
    print(point)
    session['point'] = point
    print(session)
    return render_template('add_fav.html', point=point)

@app.route('/start_pop')
def start_pop():
    session.pop('startpoint')
    session['startpoint'] = None
    print(session)
    return render_template('start_page.html')


@app.route('/end_pop')
def end_pop():
    session.pop('endpoint', None)
    session['endpoint'] = None
    print(session)
    return render_template('start_page.html')


@app.route('/route')
def route():
    temp_list1 = make_info_list.make_info_list(" ", session['startpoint'])
    temp_list2 = make_info_list.make_info_list(" ", session['endpoint'])
    start_x, start_y = make_info_list.find_xy(temp_list1)
    end_x, end_y = make_info_list.find_xy(temp_list2)
    total_route_list, stations_from_start, stations_from_end = find_route(start_x, start_y, end_x, end_y)
    print(total_route_list)
    sol = select_final_route.sol(total_route_list)
    print(sol)
    # print(len(sol["stations_from_end"]))
    length=len(sol["stations_from_end"])
    return render_template('routepage.html', sol = sol, length=length)


@app.route('/fav')
def fav():
    show_favorite_list = ft.show_favorite(session['userid'])
    print(show_favorite_list)
    return render_template('favorite.html',show_favorite_list=show_favorite_list)

@app.route('/add_fav')
def add_fav():
    return render_template('add_fav.html')

@app.route('/add_fav_pro', methods=['post'])
def add_fav_pro():
    favoriteTitle = request.form['favoriteTitle']
    temp_list = make_info_list.make_info_list("",session['point'])
    favoriteAddr =temp_list[0][1]
    favoriteX,favoriteY = make_info_list.find_xy(temp_list)
    userID=session['userid']
    ft.add_favorite(favoriteTitle, favoriteAddr, favoriteX, favoriteY, userID)
    show_favorite_list = ft.show_favorite(session['userid'])
    session.pop('point', None)
    return render_template('favorite.html', show_favorite_list = show_favorite_list)

@app.route('/del_fav', methods=['post'])
def del_fav():
    favoriteNo= request.form["favoriteNo"]
    print(favoriteNo)
    ft.delete_favorite(favoriteNo)
    userid=session['userid']
    show_favorite_list = ft.show_favorite(session['userid'])
    # favoriteTitle = request.form['favoriteTitle']
    # userID = request.form['userID']
    return render_template('favorite.html',show_favorite_list=show_favorite_list)


app.run(host='127.0.0.1', port=8080, debug=True)