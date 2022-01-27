from flask import redirect, url_for, request, Response, render_template
from utils import get_user_id_by_cookie
users = [
    {'username': 'admin', 'password': '1', 'bdate': '', 'key': None}
]


# @app.route('/hi')
def say_hello(name):
    user_id = get_user_id_by_cookie(request, users)
    user = users[user_id] if user_id else None

    names = request.cookies['name'].split(',') if request.cookies.get('name', None) else []
    resp = Response(render_template('say_hello.html', name=name, names=names, user=user))
    if name not in names:
        names.append(name)
        from datetime import datetime as dt
        from datetime import timedelta as td
        resp.set_cookie("name", ",".join(names), expires=dt.utcnow() + td(minutes=30))
    return resp


# @app.route('/hi?name=alireza')
def say_hello_by_query():
    # name = "Kokab"
    # if request.args['name']:
    #     name = request.args['name']

    # name = request.args['name'] if request.args['name'] else "Kokab"

    name = request.args.get('name', 'Kokab')
    print(name)
    return f"<center><h1 style='color: orangered'>Hi {name} ^_^</h1></center>"


# sum/num1/num2
def summary(num1, num2):
    return f"<center><h1 style='color: green'>Sum of {num1} + {num2} = {num1 + num2} !</h1></center>"


# pow/num1/num2
def power(num1, num2):
    return f"<center><h1 style='color: blue'>Power of {num1} ** {num2} = {num1 ** num2} !</h1></center>"


def google_search(text):
    return redirect(f"https://www.google.com/search?q={text}")


# def home():
#     return f"""
#     <center>
#     <ul style='color: black'>
#         <li><a href='{url_for('home')}'>Home</a></li>
#         <li><a href='{url_for('hi')}'>Say hello</a></li>
#         <li><a href='{url_for('search', text="iran")}'>Search it !</a></li>
#         <li><a href='{url_for('method_detector')}'>Method finder</a></li>
#     </ul>
#     </center>
# """


def detector():
    # return f"Resquest by {request.method} method!"
    if request.method == "POST":
        return f"Resquest by POST method!"
    elif request.method == "GET":
        return f"Salaaaaaaam !"


def request_info():
    return f"""
<ul>
    <li><b>method</b> : {request.method}</li>
    <li><b>url</b> : {request.url}</li>
    <li><b>args</b> : {request.args}</li>
    <li><b>headers</b> : {request.headers}</li>
</ul>
    """


post_data = [
    {'id': 0, 'title': 'Iran',
     'description': '''Iran is home to one of the world's oldest civilizations,[13][14] beginning with the formation of the Elamite kingdoms in the fourth millennium BC. It was first unified by the Iranian Medes in the seventh century BC,[15] and reached its territorial height in the sixth century BC, when Cyrus the Great founded the Achaemenid Empire, which became one of the largest empires in history and has been described as the world's first superpower.[16] The empire fell to Alexander the Great in the fourth century BC and was divided into several Hellenistic states. An Iranian rebellion established the Parthian Empire in the third century BC, which was succeeded in the third century AD by the Sasanian Empire, a major world power for the next four centuries.[17][18] Arab Muslims conquered the empire in the seventh century AD, which led to the Islamization of Iran. It subsequently became a major center of Islamic culture and learning, with its art, literature, philosophy, and architecture spreading across the Muslim world and beyond during the Islamic Golden Age. Over the next two centuries, a series of native Muslim dynasties emerged before the Seljuq Turks and the Mongols conquered the region. In the 15th century, the native Safavids re-established a unified Iranian state and national identity[4] and converted the country to Shia Islam.[5][19] Under the reign of Nader Shah in the 18th century, Iran once again became a major world power,[20] though by the 19th century a series of conflicts with Russia led to significant territorial losses.[21][22] The early 20th century saw the Persian Constitutional Revolution. Efforts to nationalize its fossil fuel supply from Western companies led to an Anglo-American coup in 1953, which resulted in greater autocratic rule under Mohammad Reza Pahlavi and growing Western political influence.[23] He went on to launch a far-reaching series of reforms in 1963.[24] After the Iranian Revolution, the current Islamic Republic was established in 1979[25] by Ruhollah Khomeini, who became the country's first Supreme Leader.The Government of Iran is an Islamic theocracy which includes elements of a presidential democracy, with the ultimate authority vested in an autocratic "Supreme Leader",[26] a position held by Ali Khamenei since Khomeini's death in 1989. The Iranian government is widely considered to be authoritarian, and has attracted widespread criticism for its significant constraints and abuses against human rights and civil liberties,[27][28][29][30] including several violent suppressions of mass protests, unfair elections, and limited rights for women and children.Iran is a regional and middle power, with a geopolitically strategic location in the Asian continent.[31] It is a founding member of the United Nations, the ECO, the OIC, and the OPEC. It has large reserves of fossil fuels—including the world's second-largest natural gas supply and the fourth-largest proven oil reserves.[32] The country's rich cultural legacy is reflected in part by its 26 UNESCO World Heritage Sites.[33] Historically a multinational state, Iran remains a pluralistic society comprising numerous ethnic, linguistic, and religious groups, the largest being Persians, Azeris, Kurds, Mazandaranis and Lurs.'''},
    {'id': 1, 'title': 'Akbar',
     'description': '''Abu'l-Fath Jalal-ud-din Muhammad Akbar[7] (Persian: ابو الفتح جلال الدين محمد اكبر; 25 October 1542[a] – 27 October 1605),[10][11][12] popularly known as Akbar the Great[13] (Persian: اکبر اعظم, romanized: Akbar-i-azam), and also as Akbar I (IPA: [əkbər]),[14] was the third Mughal emperor, who reigned from 1556 to 1605. Akbar succeeded his father, Humayun, under a regent, Bairam Khan, who helped the young emperor expand and consolidate Mughal domains in India.A strong personality and a successful general, Akbar gradually enlarged the Mughal Empire to include much of the Indian subcontinent. His power and influence, however, extended over the entire subcontinent because of Mughal military, political, cultural, and economic dominance. To unify the vast Mughal state, Akbar established a centralised system of administration throughout his empire and adopted a policy of conciliating conquered rulers through marriage and diplomacy. To preserve peace and order in a religiously and culturally diverse empire, he adopted policies that won him the support of his non-Muslim subjects. Eschewing tribal bonds and Islamic state identity, Akbar strove to unite far-flung lands of his realm through loyalty, expressed through an Indo-Persian culture, to himself as an emperor.Mughal India developed a strong and stable economy, leading to commercial expansion and greater patronage of culture. Akbar himself was a patron of art and culture. He was fond of literature, and created a library of over 24,000 volumes written in Sanskrit, Urdu, Persian, Greek, Latin, Arabic and Kashmiri, staffed by many scholars, translators, artists, calligraphers, scribes, bookbinders and readers. He did much of the cataloging himself through three main groupings.[15] Akbar also established the library of Fatehpur Sikri exclusively for women,[16] and he decreed that schools for the education of both Muslims and Hindus should be established throughout the realm. He also encouraged bookbinding to become a high art.[15] Holy men of many faiths, poets, architects, and artisans adorned his court from all over the world for study and discussion. Akbar's courts at Delhi, Agra, and Fatehpur Sikri became centres of the arts, letters, and learning. Timurid and Perso-Islamic culture began to merge and blend with indigenous Indian elements, and a distinct Indo-Persian culture emerged characterized by Mughal style arts, painting, and architecture. Disillusioned with orthodox Islam and perhaps hoping to bring about religious unity within his empire, Akbar promulgated Din-i-Ilahi, a syncretic creed derived mainly from Islam and Hinduism as well as some parts of Zoroastrianism and Christianity.Akbar's reign significantly influenced the course of Indian history. During his rule, the Mughal Empire tripled in size and wealth. He created a powerful military system and instituted effective political and social reforms. By abolishing the sectarian tax on non-Muslims and appointing them to high civil and military posts, he was the first Mughal ruler to win the trust and loyalty of the native subjects. He had Sanskrit literature translated, participated in native festivals, realising that a stable empire depended on the co-operation and good-will of his subjects. Thus, the foundations for a multicultural empire under Mughal rule were laid during his reign. Akbar was succeeded as emperor by his son, Prince Salim, later known as Jahangir.'''},
]


def handler():
    return Response({"user": "kokab", 'password': "454546543"}, 500)


def home():
    user_id = get_user_id_by_cookie(request, users)
    user = users[user_id] if user_id else None

    return render_template("home.html", user=user)


def posts():
    user_id = get_user_id_by_cookie(request, users)
    user = users[user_id] if user_id else None

    return render_template("posts.html", posts=post_data, user=user)


def post(post_id: int):
    user_id = get_user_id_by_cookie(request, users)
    user = users[user_id] if user_id else None

    return render_template("post.html", post=post_data[post_id], user=user)


def new_post():
    user_id = get_user_id_by_cookie(request, users)
    user = users[user_id] if user_id else None

    if request.method == "GET":
        return render_template("new_post.html", user=user)

    elif request.method == "POST":
        title = request.form.get('title')
        description = request.form.get('description')
        post_data.append({
            'id': len(post_data),
            'title': title,
            'description': description
        })
        return redirect(url_for('posts'))


def about():
    user_id = get_user_id_by_cookie(request, users)
    user = users[user_id] if user_id else None

    return render_template("about.html", user=user)


def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == "POST":
        # get form inputs!
        username = request.form.get('username', None)
        password = request.form.get('password', None)

        # auth
        for user in users:
            if user['username'] == username and user['password'] == password:
                # login!!!
                from uuid import uuid4
                user['key'] = uuid4().hex

                res = Response("login successfully")
                res.set_cookie("user_id", str(users.index(user)))
                res.set_cookie("login_key", user['key'])

                return res

        return "Username or password incorrect"


def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == "POST":
        username = request.form.get('username')

        for user in users:
            if user['username'] == username:
                return "this user is exists!"

        users.append({
            'username': username,
            'password': request.form.get('password'),
            'bdate': request.form.get('bdate'),
            'key': None
        })

        print(users)
        return "This user registered!"


def logout():
    resp = Response('Logout successfully')
    resp.delete_cookie('user_id')
    resp.delete_cookie('login_key')
    return resp


def translate(target_lang, from_lang, provider):
    import translators as ts

    if request.method == "GET":
        return 'HELLO FROM TRANSLATOR'
    elif request.method == "POST":
        text = request.form.get('text')
        print(provider)
        translated_text = getattr(ts, provider)(text, to_language=target_lang, from_language=from_lang)
        print(translated_text)
        return translated_text