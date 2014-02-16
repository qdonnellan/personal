import os

def discover_blog_files():
    this_dir = os.path.abspath(os.path.join(__file__, os.pardir))
    parent_dir = os.path.abspath(os.path.join(this_dir, os.pardir))
    blog_dir = parent_dir + '/blog_files/'

    discovered_files = []

    for root, dirs, files in os.walk(blog_dir):
        for f in files:
            if f.endswith(".md"):
                file_path = os.path.join(root, f)
                discovered_files.append(file_path)

    return discovered_files