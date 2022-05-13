
import os
import json
import urllib
import webapp2
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

    def post(self):
        city_name = self.request.get('city_name')
        url = "http://universities.hipolabs.com/search?name="+ city_name
        data = urllib.urlopen(url).read()
        data = json.loads(data)
        print(data)
        if(len(data)>0):
            code = data[0]['alpha_two_code']
            country = data[0]['country']
            name = data[0]['name']
            domains = data[0]['domains'][0]
            template_values = {
                "code": code,
                "country": country,
                "name": name,
                "domains": domains
            }
            path = os.path.join(os.path.dirname(__file__), 'results.html')
            self.response.out.write(template.render(path, template_values))
        else:
            template_values = {}
            path = os.path.join(os.path.dirname(__file__), 'error.html')
            self.response.out.write(template.render(path, template_values))
        
        
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
