import os

def fetch_blog_map():
    '''
    return the json file which holds the blog blog
    '''
    this_dir = os.path.abspath(os.path.join(__file__, os.pardir))
    parent_dir = os.path.abspath(os.path.join(this_dir, os.pardir))
    path = parent_dir + "/blog_files/blogmap.json"
    with open(path, 'r') as f:
        blog_map = f.read()
    f.closed
    return blog_map