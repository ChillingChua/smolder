import logging
import re
from charcoal.smolder_plugin import SmolderPlugin
LOG = logging.getLogger('smolder')


class ResponseRedirect(SmolderPlugin):

    def run(self, req):
        if "30" in str(req.req.status_code):
            match = re.match(req.test['outcomes']['response_redirect'], req.req.headers['location'])
            if match:
                message = req.pass_test("Redirect to {0}".format(req.test['outcomes']['response_redirect']))
                return message
            else:
                return req.fail_test("Got redirected to {0} instead of {1}".format(
                    req.req.headers['location'],
                    req.test['outcomes']['response_redirect']))
        else:
            return req.fail_test("Not being redirected: {0}".format(req.req.status_code))
