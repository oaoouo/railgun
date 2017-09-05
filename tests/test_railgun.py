#coding: utf-8

import os
import shutil


root_path = os.getcwd()
test_env = os.path.join(root_path, 'tests/')

# build tree
build_tree = ['./blog/',
              './blog/app', './blog/gen',
              './blog/app/pages', './blog/app/themes', './blog/app/static', './blog/app/templates', 
              './blog/app/static/img', './blog/app/static/css', './blog/app/static/js', './blog/app/themes/cat',
              './blog/app/themes/cat/static', './blog/app/themes/cat/templates', 
              './blog/app/themes/cat/static/img', './blog/app/themes/cat/static/css', './blog/app/themes/cat/static/js']


def test_railgun_init():
    # assert test_env == "/home/neo1218/oaoouo/railgun/tests/"
    os.chdir(test_env)
    os.popen('railgun init blog')
    path_list = []
    for path, _, _ in os.walk("./blog/"):
        if "./blog/app/themes/cat/.git" not in path:
            path_list.append(path)
    assert set(path_list) == set(build_tree)
    clean_test_env()


def clean_test_env():
    os.chdir(test_env)
    blog_path = os.path.join(test_env, './blog')
    shutil.rmtree(blog_path)
