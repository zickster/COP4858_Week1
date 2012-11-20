import urllib2
import webbrowser
import cookielib
from collections import defaultdict
from BeautifulSoup import BeautifulSoup


chart_data = []

# String template for the Google Charts API that you can use to create the graph
# You just to call .substitute on it with the following keyword parameters
#     colors - the colors in HTML hex format, e.g. FF0000, separated by | of each of the points
#     roomlabelpos - the numbers 1, 2, 3, ..., up to the number of rooms also separated by |
#     maxroomaxis - the number of rooms + 1
#     data - the x values for the graph separated by , followed by a |, then the y values of the graph
#            separated by commas

#chart_url_template = Template('http://chart.googleapis.com/chart?chxl=0:|M|T|W|R|1:|${rooms}&chxp=0,1,2,3,4|1,${roomlabelpos}&chxr=0,0,5|1,0,${maxroomaxis}&chxs=0,,16|1,,16&chxt=x,y&chs=500x300&cht=s&chco=${colors}&chds=0,5,0,${maxroomaxis}&chd=t:${data}&chdl=CGS|Majors&chdls=0000FF,FF0000&chtt=Bldg+48+3rd+Floor+Evening+Classroom+Usage')



def getWebData():
    """Goes to the Advanced Search on the Class Finder at
       http://www.broward.edu/FCCSC/registration/coursesearch.jsp
       and searches for evening computer classes.
    """

    # This will handle HTTP cookies -- which are required to use
    # the broward.edu form
    cj = cookielib.CookieJar()

    # install opener, including the cookie processor
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)

    # Pretend we are Firefox making the request
    user_agent = r'Mozilla/5.0 (Windows NT 6.1; rv:6.0.2) Gecko/20100101 Firefox/6.0.2';
    headers = {'User-Agent': user_agent}

    # open the search form to get the cookie
    urlForCookie = r'http://www.broward.edu/FCCSC/registration/coursesearch.jsp'
    req = urllib2.Request(urlForCookie, headers=headers)
    response = urllib2.urlopen(req)

    # Some debugging code
    ##  print "Page headers:"
    ##  print response.info()
    ##  print "Cookies"
    ##  for index, cookie in enumerate(cj):
    ##    print index, '  :  ', cookie
    ##  URL Results http://www.broward.edu/FCCSC/servlet/registration.IAS012N2s?from=registration/coursearch.jsp&campus=2&classStatus=A&classType=A&course0=&course1=&course2=&course3=&course4=&course5=&course6=&course7=&course8=&course9=&coursePrefix=ETD&coursePrefix=CEN%2CCET%2CCGS%2CCIS%2CCOP%2CCDA%2CCTS&coursePrefix=CGS%2CCOP%2CCTS%2CCDA%2CCEN%2CCET%2CCIS&coursePrefix=ETD&courseTitle=&dayType=A&days=M&days=T&days=W&days=R&days=F&endTime=ANY&instructorName=&session=*&startTime=1800000&term=20132


    # This is the URL that the form data needs to be submitted to
    url = r'http://www.broward.edu/FCCSC/servlet/registration.IAS012N2s?from=registration/coursearch.jsp'
    # Here's all the form data for you
    data = r'&campus=2&classStatus=A&classType=A&course0=&course1=&course2=&course3=&course4=&course5=&course6=&course7=&course8=&course9=&coursePrefix=ETD&coursePrefix=CEN%2CCET%2CCGS%2CCIS%2CCOP%2CCDA%2CCTS&coursePrefix=CGS%2CCOP%2CCTS%2CCDA%2CCEN%2CCET%2CCIS&coursePrefix=ETD&courseTitle=&dayType=A&days=M&days=T&days=W&days=R&days=F&endTime=ANY&instructorName=&session=*&startTime=1800000&term=20132'

    # Submit and read the response
    req = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(req)

    the_page = response.read(300000)
    return the_page

# soup's on!

def maSoup():
    """Demo of how to use BeautifulSoup"""
    # first we grab the data from results of the web form
    # and parse the HTML with BeautifulSoup
    soup = BeautifulSoup(getWebData())

    # find all the tables on the page, stored in a
    # list variable named tables
    tables = soup.findAll('table')

    details = tables[2].findAll('td', {'class': 'fccsc-detail-x-small-black'})[:80]
    rows = tables[2].findAll('tr')
    data = []
    course_data = []
    new_course_data = dict()
    room_data = []
    day_data = []
    date_data = []
    potter_day = []
    ma_course_data = defaultdict()

    for tr in rows:
        if '48/003' in tr.text:
            data.append(tr)
    for course in data:
        cells = course.findAll('td', {'class': 'fccsc-detail-x-small-black'})
        for day in cells[11:18]:
            if len(day.text) == 7:
                day_data = day.text[0]
                if day_data == 'M':
                    potter_day.append(20)
                elif day_data == 'T':
                    potter_day.append(40)
                elif day_data == 'W':
                    potter_day.append(60)
                elif day_data == 'R':
                    potter_day.append(80)
                elif day_data == 'F':
                    potter_day.append(100)
        #ma_course_data[cells[2].text].append(cells[4].text, day_data)
        new_course_data[cells[2].text] = cells[4].text, day_data
        course_data.append(cells[2].text)
        room_data.append(cells[4].text)
        date_data.append(day_data)



    #generates Google Chart
    url_start = 'http://chart.googleapis.com/chart?chxr=0,-5,105|1,0,105&chxt=x,y&chxl=0:||M|T|W|TR|1:||'

    #removes duplicates
    result = []
    for item in room_data:
        if item not in result:
            result.append(item)

    for g_course_potter in result[::-1]:
        url_start = url_start + str(g_course_potter) + '|'
    url_start = url_start[:-1]
    url_start = url_start + '&chs=600x500&cht=s&chco=0000FF&chds=0,100,-5,100&chd=t:'

    #This creates the chs plotters

    y_plot = []
    y_plotter = []
    y_plot_dic = dict()
    pos_rate = 100 / len(result) + 2
    pos_plot = 100



    #Dict for Room = Y-Axis value
    for result_check in result:
        y_plot_dic[result_check] = pos_plot
        pos_plot = pos_plot - pos_rate

    #Dict for Course dates


    x_plot = []
    x_plotter = []
    x_plot_dict = dict()


    for grab_y in new_course_data:
        if grab_y in new_course_data:
            x_plot = new_course_data[grab_y][1]
            y_plot = new_course_data[grab_y][0]
            if y_plot in y_plot_dic:
                y_plotter.append(y_plot_dic[y_plot])
            if x_plot == 'M':
                x_plotter.append(25)
            elif x_plot == 'T':
                x_plotter.append(50)
            elif x_plot == 'W':
                x_plotter.append(75)
            elif x_plot == 'R':
                x_plotter.append(100)
            elif x_plot == 'F':
                x_plotter.append(-5)


    for x_url in x_plotter:
        url_start = url_start + str(x_url) + ','

    url_start = url_start[:-1]
    url_start = url_start + '|'

    for y_url in y_plotter:
        url_start = url_start + str(y_url) + ','
    url_start = url_start[:-1]
    url_start = url_start + '&chdl=Majors&chtt=.++Bldg+48+3rd+Floor+Evening+Classroom+Usage'

    handle=webbrowser.get()
    handle.open(url_start)



    #return course_data, room_data, date_data
    return url_start



#this is to run function maSoup
maSoup()
