import requests
from icalendar import Calendar, Event
import re
from flask import Flask, make_response, render_template


flask_app = Flask("ghsathletics")


url = "https://www2.arbitersports.com/ICal/School/schedule.ics?id=cHHWgTXR%2b%2fvlYfnDlphDuQ%3d%3d"

cal = Calendar.from_ical(requests.get(url).text)

#print(cal.to_ical().decode("utf-8").replace('\r\n', '\n').strip())

newcal = Calendar()

for component in cal.walk(name="VEVENT"):
    if re.search(".*Boys Freshman*", component.get("description")) and re.search(".*Sport: Lacrosse*", component.get("description")):
        component.get("description")
        newcal.add_component(component)
        #print(component.to_ical().decode("utf-8").replace('\r\n', '\n').strip())
           
print(newcal.to_ical().decode("utf-8").replace('\r\n', '\n').strip())


