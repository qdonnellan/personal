import os

def fetch_blog_post(year, month, day):
    '''
    fetches the blog post given year, month, and day or None of it doesn't exist
    '''
    try:
        this_dir = os.path.abspath(os.path.join(__file__, os.pardir))
        parent_dir = os.path.abspath(os.path.join(this_dir, os.pardir))
        blog_path = parent_dir + "/blog_files/{year}/{month}/{day}.md".format(
            year = year, 
            month = month, 
            day = day
            )
        with open(blog_path, 'r') as f:
          blog_data = f.read()
        f.closed
        return blog_data
    except:
        return None