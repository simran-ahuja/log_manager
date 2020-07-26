import re


def mask(url):
    return re.sub("\d+", "{id}", url)
