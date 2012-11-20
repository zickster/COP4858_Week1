__author__ = 'ladmin'

import urllib2
import cookielib
from BeautifulSoup import BeautifulSoup

def getWebData():
    cj = cookielib.CookieJar()

    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)

    user_agent = r'Mozilla/5.0 (Windows NT 6.1; rv:6.0.2) Gecko/20100101 Firefox/6.0.2'
    headers = {'User-Agent': user_agent}

    urlForCookie = r'http://www.broward.edu/FCCSC/registration/coursesearch.jsp'
    req = urllib2.Request(urlForCookie, headers=headers)
    response = urllib2.urlopen(req)

    url = r'http://www.broward.edu/FCCSC/servlet/registration.IAS012N2s?from=registration/coursearch.jsp'

    data = r'&campus=2&classStatus=A&classType=A&course0=&course1=&course2=&course3=&course4=&course5=&course6=&course7=&course8=&course9=&coursePrefix=ETD&coursePrefix=CEN%2CCET%2CCGS%2CCIS%2CCOP%2CCDA%2CCTS&coursePrefix=CGS%2CCOP%2CCTS%2CCDA%2CCEN%2CCET%2CCIS&coursePrefix=ETD&courseTitle=&dayType=A&days=M&days=T&days=W&days=R&days=F&endTime=ANY&instructorName=&session=*&startTime=1800000&term=20132'

    req = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(req)

    the_page = response.read(300000)
    return the_page


def soupDemo():

    global result_check
    soup = BeautifulSoup(getWebData())

    tables = soup.findAll('table')

    details = tables[2].findAll('td', {'class': 'fccsc-detail-x-small-black'})[:80]
    rows = tables[2].findAll('tr')
    data = []
    course_data = []
    new_course_data = dict()
    room_data = []
    day_data = []
    date_data = []
    potter_data = []
    potter_day = []


    for tr in rows:
        if '48/003' in tr.text:
            data.append(tr)

    for course in data:
        cells = course.findAll('td', {'class': 'fccsc-detail-x-small-black'})
        for day in cells[11:18]:
        #course_data.append([cells[2].text, cells[4].text, day_data])
            new_course_data[cells[2].text] = cells[4].text, day_data
            course_data.append(cells[2].text)
            room_data.append(cells[4].text)
            date_data.append(day_data)

    url_start = 'http://chart.googleapis.com/chart?chxr=0,-5,105|1,0,105&chxt=x,y&chxl=0:||M|T|W|TR|F|1:||'

    result = []
    for item in room_data:
        if item not in result:
            result.append(item)


    for g_course_potter in result[::-1]:
        url_start = url_start + str(g_course_potter) + '|'

    url_start = url_start + '&chs=600x500&cht=s&chco=FF0000|0000FF&chds=0,100,-5,100&'

    y_plot = []
    y_plot_dic = dict()
    pos_rate = 100 / len(result) + 2
    pos_plot = 100

    #Dict for Room = Y-Axis value
    for result_check in result:
        y_plot_dic[result_check] = pos_plot
        pos_plot = pos_plot - pos_rate


    x_plot = []
    x_plot_dict = dict()

    for room_check in new_course_data:
        if room_check in result_check


    return course_data


soupDemo()