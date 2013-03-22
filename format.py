# format.py 
# a mashup of markdown and my own shorthand

# Copyright (C) 2013 Quentin Donnellan
# http://qdonnellan.appspot.com
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import markdown2
import cgi
import re

def formatContent(contents):
    newContents= []
    for content in contents:
        newContents.append(formatted(content))        
    return newContents

class formatted():
    def __init__(self, content):
        # body is a temp variable that will be formatted then applied to the class
        body = content.body

        # Escaping underscore charcters before Markdown
        body = re.sub('_', '\_', body)

        # Escaping user-supplied HTML injection
        body = cgi.escape(body)

        # Markdown!
        body = markdown2.markdown(body)

        # Un-escaping underscore characters (post-Markdown)
        body = re.sub('\_', '_', body)

        # Formatting for code blocks (post-Markdown)
        if 'code=latex' in body:
            body = re.sub('code=latex', '', body)
            body = re.sub(r'<pre><code>', r'<pre class="prettyprint linenums lang-tex">', body)
        elif 'code=blank' in body:
            body = re.sub('code=blank', '', body)
            body = re.sub(r'<pre><code>', r'<pre>', body)
        else:
            body = re.sub(r'<pre><code>', r'<pre class="prettyprint linenums">', body)
        body = re.sub(r'</code></pre>', r'</pre>', body)     

        # Re-formatting double-escaped stuff (post-Markdown)
        body = re.sub(r'&amp;lt;',r'&lt;', body)
        body = re.sub(r'&amp;gt;',r'&gt;', body)
        body = re.sub(r'&amp;amp;',r'&amp;', body)

        # Formatting for step-by-step directions as a label (post-Markdown)
        if len(re.findall(r'@@', body)) == 2*len(re.findall(r'/@@', body)):
            body = re.sub(r'/@@', r'</span>', body)
            body = re.sub(r'@@',r'<span class="label label-info"> STEP ', body)


        # Formatting youtube videos to be responsive iframes #
        videoPre = '''
            <section class="row-fluid">
                <div class="span12">
                    <div class="flex-video widescreen"><iframe src="https://www.youtube-nocookie.com/embed/'''
        videoPost = '''" frameborder="0" allowfullscreen=""></iframe></div>
                    </div>                    
            </section>
            '''

        quotePre = '''
        <div class="lesson-quote well">
        <span class="text-info"><i class="icon-quote-left icon-4x pull-left icon"></i></span>       
        '''
        quotePost='</div>'
        if len(re.findall('quote::', body)) == len(re.findall('::quote', body)):
            body = re.sub('quote::', quotePre, body)
            body = re.sub('::quote', quotePost, body)

        body = re.sub('cite::', '<div class="pull-right muted"><i class="icon-minus"></i> ', body)
        body = re.sub('::cite', '</div>', body)


        if len(re.findall('video::', body)) == len(re.findall('::video', body)):
            body = re.sub('video::', videoPre, body)
            body = re.sub('::video', videoPost, body)

        body = re.sub('video;;', 'video::', body)
        body = re.sub(';;video', '::video', body)


        body = re.sub('&amp;#64;', '@', body)


        # Passing everything, including the formatted body, to the new formatted class
        self.body = body
        self.title = content.title
        self.id = content.key.id()
        self.created = content.created