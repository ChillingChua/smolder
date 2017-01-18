import logging
from charcoal.smolder_plugin import SmolderPlugin

LOG = logging.getLogger('smolder')


class ResponseContains(SmolderPlugin):
    """ checks if a string-ified has a specific substring value """

    def run(self, req):
        # Did we expect something specific in the response body?
        required_text = req.test['outcomes']['response_contains']
        LOG.debug(required_text)
        try:
            req_content = req.req.content.decode()
        except UnicodeDecodeError:
            req_content = req.req.content
        if req_content.find(required_text) < 0:
            return req.fail_test("\"{0}\" does not contain \"{1}\"".format(req_content, required_text))
        else:
            return req.pass_test("Body contains \"{0}\"".format(required_text))
