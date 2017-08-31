title: ⚡️ How to Use
date: 2016-11-06 15:44:37
tags: ['railgun', 'use']

![](https://images5.alphacoders.com/733/thumb-350-733587.jpg)

# How to Use

## Step1: Initialize a blog

    $ railgun init blog

## Step2: Config

    $ cd blog
    $ vim config.py

don't forget to change **default config class**

    config = {
        'default': MyConfig
    }

## Step3: Writing

    $ cd blog
    $ railgun new newblog

then

    $ vim app/pages/newblog.md

the default article template show below:

    title:
    date: %Y-%m-%d %H:%M:%S
    tags: ['tag1', 'tag2']

the default format for the blog is ``markdown``, you can change it in the config.py file

    class Config(object):
        # ......
        FLATPAGES_EXTENSION = '.md'

## Step4: Preview

    $ railgun server

## Step5: Build and Deploy

    $ railgun build
    $ railgun upload

done! <br/>
enjoy writing :)
