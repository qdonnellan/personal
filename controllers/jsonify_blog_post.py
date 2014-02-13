import json
import re
from controllers.fetch_blog_post import fetch_blog_post
from controllers.markdown2 import markdown

def jsonify_blog_post(year, month, day):
    '''
    accept a blog post and retun a json object representing that blog post
    '''
    blog_post = fetch_blog_post(year, month, day)

    if not blog_post:
        data = {'error' : 'blog post does not exist'}
    else:
        title = re.search('[#].*\n', blog_post).group()
        author = re.search('author:.*\n', blog_post)
        if author:
            author = author.group()
            blog_post = re.sub(author, '', blog_post)
            author = re.sub('author:', '', author).strip('\n')
        else:
            author = 'Quentin Donnellan'

        blog_post = re.sub(title, '', blog_post).strip('\n')
        
        title = re.sub('[#]', '', title).strip('\n')
        data = {
            'year' : year,
            'day' : day, 
            'month' : month,
            'author' : author.strip(' '),
            'markdown' : blog_post,
            'html' : markdown(blog_post),
            'title' : title.strip(' ')
        }
    return json.dumps(data)