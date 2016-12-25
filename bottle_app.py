from bottle import route, run, default_app, debug,request


def htmlify(title, content):
    page = """<!DOCTYPE html>
              <html>
                  <head>
                      <title>""" + title + """</title>
                      <meta charset="utf-8" />
                  </head>
                  <body>
                      """ + content + """
                  </body>
              </html>"""
    return page


def a3_index():
    return htmlify("My lovely website", "This is going to be an awesome website, when it is finished.")


def website_index():
    return htmlify('My lovely homepage',
                   """
                   <!-- p><a href="/assignment1/">Click for my assignment 1.</a></p -->
                   <!-- p><a href="/assignment2/">Click for my assignment 2.</a></p -->
                   <p><a href="/home/">Click for my assignment 3.</a></p>
                   """)
comments = [{'Username':'mahmut','comment' : 'Berbat bir sa','points' : '3'},{'Username':'mahmut','comment' : 'Berbat bir sa','points' : '7'}]
def home_page():
    html ="""
            <p>
            <form action="http://localhost:8080/home/news/results" method="get">
            Username:
            <br>
            <input type="text" name="Username" value="Mickey" required>
            <input type="range" name="points" min="0" max="10">
            <br>
            <textarea style="height: 100px; width: 300px" type="textarea" name="comment"/>What do you think?</textarea>
            <br>
            <input type="submit" value="Submit">
            </form>
            </p>
            <br>
            """
    for person in comments:
        html += person['Username']
        html += person['comment']
        html += person['points']
    x=0
    for range in comments:
        x+=int(range['points'])
        html+="<br>"+str(x)
    total = 0
    #for i in range (0,2):
      #  total+=int(comments[i]['points'])
      #  html+="<br>"+str(total)
    return htmlify("home",html)

def get_comment():
    users_name = str(request.GET.get('Username'))
    users_comment = str(request.GET.get('comment'))
    users_range = str(request.GET.get('points'))
    global comments
    comments+=[{'Username':users_name,'comment':users_comment,'points':users_range}]
    html = str(users_name)+str(users_comment)+str(users_range)
    return htmlify("comment",html)


route('/home/news/results','GET',get_comment)
route('/home/news','GET',home_page)
route('/home/','GET', a3_index)
route('/', 'GET', website_index)

debug(True)
application = default_app()
if __name__ == "__main__":
    run()