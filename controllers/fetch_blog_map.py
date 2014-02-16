from controllers.discover_blog_files import discover_blog_files
from controllers.jsonify_blog_post import jsonify_blog_post
import re
import json

def fetch_blog_map():
    '''
    return the a json object containing a list of references to all blog files
    '''
    file_list = discover_blog_files()
    data = []
    for f in file_list:
        re_match = re.search('(\d+)/(\d+)/(\d+)', f)
        year = re_match.group(1)
        month = re_match.group(2)
        day = re_match.group(3)
        blog_json_object = json.loads(jsonify_blog_post(year, month, day))
        data.append(blog_json_object)

    return json.dumps(data)