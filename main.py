import webapp2
import cgi

#def build_form():


class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Signup</h1>"
        form = """
        <form method='post'>
            <table><tbody>
            <tr><td>
            <label>Username</label></td>
            <td><input name = 'username' type='text' value required>
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

        self.response.write(header + form)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
