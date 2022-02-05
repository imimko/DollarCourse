from twirp.asgi import TwirpASGIApp

import requests
import xml.etree.cElementTree as ET

import dollar_cource_twirp, dollar_cource_pb2

class DollarCourseService():
    async def GetCourse(self, context, mes):
        dollar_req = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
        courses = ET.fromstring(dollar_req.text)
        dollar_course = courses.find("Valute[@ID='R01235']").find('Value').text.replace(',', '.')

        return dollar_cource_pb2.Course(price=float(dollar_course))

service = dollar_cource_twirp.DollarcourseServer(service=DollarCourseService())

app = TwirpASGIApp()
app.add_service(service)