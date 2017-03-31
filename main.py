import webapp2
import cgi
import re

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>User Signup</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
"""

def build_form(user_error='', pass_error='', verify_error='', email_error=''):
    form = """
    <form method='post'>
        <table><tbody>
        <tr><td>
        <label>Username</label></td>
        <td><input name='username' type='text' value required>
        </td><td><span class="error">{0}</span></td></tr>

        <tr><td>
        <label>Password</label></td>
        <td><input name='password' type='password' value required>
        </td><td><span class="error">{1}</span></td></tr>

        <tr><td>
        <label>Verify Password</label></td>
        <td><input name='verify' type='password' value required>
        </td><td><span class="error">{2}</span></td></tr>

        <tr><td>
        <label>Email (optional)</label></td>
        <td><input name='email' type='text'>
        </td><td><span class="error">{3}</span></td></tr>

        </tbody></table>
        <input type='submit'>
    </form>
        """.format(user_error, pass_error, verify_error, email_error)
    return form


header = "<h1>Signup</h1>"

class MainHandler(webapp2.RequestHandler):
    def get(self):

        form = build_form()
        self.response.write(page_header + header + form)

    def post(self):

        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        def valid_username(username):
            return USER_RE.match(username)

        PASS_RE = re.compile(r"^.{3,20}$")
        def valid_password(password):
            return PASS_RE.match(password)

        EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
        def valid_email(email):
            return EMAIL_RE.match(email)

        user_error = ''
        pass_error = ''
        verify_error = ''
        email_error = ''

        if not valid_username(username):
            user_error= "Username is not valid"
        if not valid_password(password):
            pass_error= "Password is not vaild"
        if verify != password:
            verify_error = "Passwords do not match"
        if email and not valid_email(email):
            email_error =  "Email address is not valid"

        form = build_form(user_error, pass_error, verify_error, email_error)

        self.response.write(page_header + header + form)





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
