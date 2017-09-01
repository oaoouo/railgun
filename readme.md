# ⚡️ railgun

> static site generator

## Step1: Initialize a blog

```shell
$ railgun init blog
```

## Step2: Config

```shell
$ cd blog
$ vim config.py
```

don't forget to change ``default config class``
```python

config = {
    'default': MyConfig
}
```

## Step3: Writing

```shell
$ cd blog
$ railgun new newblog
```

then

```shell
$ vim app/pages/newblog.md
```

the default article template show below:

```markdown
title:
date: %Y-%m-%d %H:%M:%S
tags: ['tag1', 'tag2']
```

the default format for the blog is ``markdown``, you can change it in the config.py file

```python
class Config(object):
    # ......
    FLATPAGES_EXTENSION = '.md'
```

## Step4: Preview
```shell
$ railgun server
```

## Step5: Build and Deploy

```shell
$ railgun build
$ railgun upload
```

done! <br/>
enjoy writing :)

## Install

### Install from git

```shell
$ git clone https://github.com/oaoouo/railgun/ railgun
$ cd railgun
$ pip install --editable .
```

## CopyRight

Old Project: https://github.com/neo1218/railgun
<br/>
MIT, check LICENSE for detail.

## Change Log

### 20170901

speed up! generate 200 files in just 5s :)

### 20170831

fix bug :(

### 20170830

bye bye neo1218 :)

## ToDo

+ [x] speed up
+ [ ] unit tests
+ [ ] theme system
+ [ ] reverse generation
