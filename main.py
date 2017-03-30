import webapp2
import cgi
import re

#def build_form():


class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Signup</h1>"
        form = """
        <form method='post'>
            <table><tbody>
            <tr><td>
            <label>Username</label></td>
            <td><input name='username' type='text' value required>
            </td></tr>

            <tr><td>
            <label>Password</label></td>
            <td><input name='password' type='password' value required>
            </td></tr>

            <tr><td>
            <label>Verify Password</label></td>
            <td><input name='verify' type='password' value required>
            </td></tr>

            <tr><td>
            <label>Email (optional)</label></td>
            <td><input name='email' type='text'>
            </td></tr>

            </tbody></table>
            <input type='submit'>
        </form>
            """
    #def write_form(self)

        self.response.write(header + form)

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

        x = "valid"

        if not valid_username(username):
            x = "not vaild"

        self.response.write(x)





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
