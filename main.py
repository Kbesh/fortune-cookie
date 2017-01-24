#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random

def getRandomFortune():
    #list of possible fortunes
    fortunes = [
    "I see much code in code in your future",
    "Consider eating more fortun cookies",
    "You have tamed the mighty Python, now you must free it into the Great Spider's Web!"
    ]

    #randomly select one of the fortunes
    index = random.choice(fortunes)

    return "test"


class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Fortune Cookie</h1>"

        fortune = getRandomFortune()
        fortune_sentence = "Your fortune: " + fortune
        fortune_paragraph = "<p>" + forture_sentence + "</p>"

        lucky_number = random.randint(1, 100)
        number_sentence = 'Your lucky number:'+ str(lucky_number)
        number_paragraph = "<p>" + number_sentence + "</p>"

        cookie_again_button = "<a href=".">Another cookie plz!</a>"

        content = header + fortune_paragraph + number_paragraph
        self.response.write(content)


class LoginHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Thanks for trying to log in!")



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
