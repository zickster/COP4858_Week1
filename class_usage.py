import urllib
from urllib import urlopen
import urllib2
import re
import webbrowser
import cookielib
import webbrowser
from BeautifulSoup import BeautifulSoup
from string import Template

chart_data = []

# String template for the Google Charts API that you can use to create the graph
# You just to call .substitute on it with the following keyword parameters
#     colors - the colors in HTML hex format, e.g. FF0000, separated by | of each of the points
#     roomlabelpos - the numbers 1, 2, 3, ..., up to the number of rooms also separated by |
#     maxroomaxis - the number of rooms + 1
#     data - the x values for the graph separated by , followed by a |, then the y values of the graph
#            separated by commas

#chart_url_template = Template('http://chart.googleapis.com/chart?chxl=0:|M|T|W|R|1:|${rooms}&chxp=0,1,2,3,4|1,${roomlabelpos}&chxr=0,0,5|1,0,${maxroomaxis}&chxs=0,,16|1,,16&chxt=x,y&chs=500x300&cht=s&chco=${colors}&chds=0,5,0,${maxroomaxis}&chd=t:${data}&chdl=CGS|Majors&chdls=0000FF,FF0000&chtt=Bldg+48+3rd+Floor+Evening+Classroom+Usage')

def getWebtest():

  webpage = urlopen('http://www.broward.edu/FCCSC/servlet/registration.IAS012N2s?from=registration/coursearch.jsp&campus=2&classStatus=A&classType=A&course0=&course1=&course2=&course3=&course4=&course5=&course6=&course7=&course8=&course9=&coursePrefix=ETD&coursePrefix=CEN%2CCET%2CCGS%2CCIS%2CCOP%2CCDA%2CCTS&coursePrefix=CGS%2CCOP%2CCTS%2CCDA%2CCEN%2CCET%2CCIS&coursePrefix=ETD&courseTitle=&dayType=A&days=M&days=T&days=W&days=R&days=F&endTime=ANY&instructorName=&session=*&startTime=1800000&term=20132').read
  clsFinder = re.compile('<td class="fccsc-detail-x-small-black" align="LEFT">(.*)</td>')

  listIterator =[]
  listIterator[:] = range(2,16)


  soup2 = BeautifulSoup(webpage)
                        
  titleSoup = soup2.findall('td')

  for i in listIterator:
    print titleSoup[i]
    
    
  


def getWebData():
  """Goes to the Advanced Search on the Class Finder at
     http://www.broward.edu/FCCSC/registration/coursesearch.jsp
     and searches for evening computer classes.
  """

  # This will handle HTTP cookies -- which are required to use
  # the broward.edu form
  cj=cookielib.CookieJar()

  # install opener, including the cookie processor
  opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
  urllib2.install_opener(opener)

  # Pretend we are Firefox making the request
  user_agent = r'Mozilla/5.0 (Windows NT 6.1; rv:6.0.2) Gecko/20100101 Firefox/6.0.2';
  headers = { 'User-Agent' : user_agent }

  # open the search form to get the cookie
  urlForCookie=r'http://www.broward.edu/FCCSC/registration/coursesearch.jsp'
  req=urllib2.Request(urlForCookie, headers=headers)
  response=urllib2.urlopen(req)

  # Some debugging code
##  print "Page headers:"
##  print response.info()
##  print "Cookies"
##  for index, cookie in enumerate(cj):
##    print index, '  :  ', cookie
##  URL Results http://www.broward.edu/FCCSC/servlet/registration.IAS012N2s?from=registration/coursearch.jsp&campus=2&classStatus=A&classType=A&course0=&course1=&course2=&course3=&course4=&course5=&course6=&course7=&course8=&course9=&coursePrefix=ETD&coursePrefix=CEN%2CCET%2CCGS%2CCIS%2CCOP%2CCDA%2CCTS&coursePrefix=CGS%2CCOP%2CCTS%2CCDA%2CCEN%2CCET%2CCIS&coursePrefix=ETD&courseTitle=&dayType=A&days=M&days=T&days=W&days=R&days=F&endTime=ANY&instructorName=&session=*&startTime=1800000&term=20132


  # This is the URL that the form data needs to be submitted to            
  url=r'http://www.broward.edu/FCCSC/servlet/registration.IAS012N2s?from=registration/coursearch.jsp'
  # Here's all the form data for you
  data=r'&campus=2&classStatus=A&classType=A&course0=&course1=&course2=&course3=&course4=&course5=&course6=&course7=&course8=&course9=&coursePrefix=ETD&coursePrefix=CEN%2CCET%2CCGS%2CCIS%2CCOP%2CCDA%2CCTS&coursePrefix=CGS%2CCOP%2CCTS%2CCDA%2CCEN%2CCET%2CCIS&coursePrefix=ETD&courseTitle=&dayType=A&days=M&days=T&days=W&days=R&days=F&endTime=ANY&instructorName=&session=*&startTime=1800000&term=20132'
  
  # Submit and read the response
  req=urllib2.Request(url, data, headers)
  response=urllib2.urlopen(req)
  
  the_page=response.read(300000)
  return the_page

# soup's on!

def soupDemo():
  """Demo of how to use BeautifulSoup"""
  # first we grab the data from results of the web form
  # and parse the HTML with BeautifulSoup
  soup=BeautifulSoup(getWebData())
  
  # find all the tables on the page, stored in a
  # list variable named tables
  tables=soup.findAll('table')
##  print "There are", str(len(tables)), "tables on the page"
##  print "Here is the first one"
##  print tables[0].prettify()
##  print
##  print "Here is the second"
##  print tables[1].prettify()
  # HINT: The table at tables[2] is the one that holds the data you need

  # Now we will for tags with a particular attribute
  details=tables[2].findAll('td', {'class': 'fccsc-detail-x-small-black'})
  results_tol = len(details)
  
  print details
  test = re.compile('align=LEFT"(.*)"/>')
  print test
    #print details[i].prettify()

  ##http://chart.googleapis.com/chart?chxr=0,-5,105|1,0,105&chxt=x,y&chxl=0:||M|T|W|TR|F|1:||48-306|48-307|48-308|48-309|&chs=300x150&cht=s&chco=FF0000|0000FF&chds=0,100,-5,100&chd=t:12,75,23,68,34,87,41,96,71,9|98,27,56,58,18,60,34,79,74,76&chdl=MGS|Majors&chm=o,FFFFFF,0,4,0|o,FF0000,0,0:4,8|d,0000FF,0,5:9,10&chtt=.++Bldg+48+3rd+Floor+Evening+Classroom+Usage
##handle=webbrowser.get()
##  handle.open('http://chart.googleapis.com/chart?chxr=0,-5,105|1,0,105&chxt=x,y&chxl=0:||M|T|W|TR|F|1:||48-306|48-307|48-308|48-309|&chs=300x150&cht=s&chco=FF0000|0000FF&chds=0,100,-5,100&chd=t:12,75,23,68,34,87,41,96,71,9|98,27,56,58,18,60,34,79,74,76&chdl=MGS|Majors&chm=o,FFFFFF,0,4,0|o,FF0000,0,0:4,8|d,0000FF,0,5:9,10&chtt=.++Bldg+48+3rd+Floor+Evening+Classroom+Usage')








  ##from BeautifulSoup import BeautifulSoup
##import urllib2
##url="http://www.utexas.edu/world/univ/alpha/"
##page=urllib2.urlopen(url)
##soup = BeautifulSoup(page.read())
##universities=soup.findAll('a',{'class':'institution'})
##for eachuniversity in universities:
##print eachuniversity['href']+","+eachuniversity.string
#soup=soupDemo()




    
  # Sometimes you want to search by more involved means
  # For instance, suppose we wanted to find scripts that
  # have actual javascript in them as opposed to linking
  # a javascript file -- basically we are looking for
  # script tags that have a non-empty contents

  # first we define a helper function that returns
  # true if and only if we are looking at a script
  # with non-empty contents

  


##def google_scrape(query):
##    address = "http://www.google.com/search?q=%s&num=100&hl=en&start=0" % (urllib.quote_plus(query))
##    request = urllib2.Request(address, None, {'User-Agent':'Mosilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11'})
##    urlfile = urllib2.urlopen(request)
##    page = urlfile.read()
##    soup = BeautifulSoup(page)
##
##    linkdictionary = {}
##
##    for li in soup.findAll('li', attrs={'class':'g'}):
##        sLink = li.find('a')
##        print sLink['href']
##        sSpan = li.find('span', attrs={'class':'st'})
##        print sSpan
##
##    return linkdictionary
##
##if __name__ == '__main__':
##    links = google_scrape('beautifulsoup')








