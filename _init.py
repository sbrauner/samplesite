#
#  create an object for our application data.  We can't just
#  use a 'scalar' as it would require us to modify the app scopea
#  which currently isn't allowed.  This is somethign we're working
#  on

import re

def mapUrlToJxpFile(uri, request, response):
	
    if( uri.match(re.compile("^/assets/") )):
        return None

    if ( uri.match(re.compile("^/favicon\.ico/"))):
        return None


    # otherwise, just always return our "controller"
    return "controller.py"



