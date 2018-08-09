"""

"""
from typing import Optional


alphanums = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
map_url_to_id = {}
shorturls = []
urls = []
cur_url_id = 0


def id_to_shorturl(id_url: int) -> str:
    res = ""
    base = len(alphanums)
    while id_url > 0:
        int_digit = id_url % base
        res += alphanums[int_digit]
        id_url = id_url // base
    return '0' * (6 - len(res)) + res


def shorturl_to_id(short_url: str) -> int:
    id_url = 0
    base = len(alphanums)
    for c in short_url:
        if ord('0') <= ord(c) <= ord('9'):
            id_url = id_url*base + ord(c) - ord('0')
        if ord('a') <= ord(c) <= ord('z'):
            id_url = id_url*base + ord(c) - ord('a') + 26
        if ord('A') <= ord(c) <= ord('Z'):
            id_url = id_url*base + ord(c) - ord('A') + 52
    return id_url


def shorten(url: str) -> str:
    global cur_url_id

    if url not in map_url_to_id:
        map_url_to_id[url] = cur_url_id
        shorturl = id_to_shorturl(cur_url_id)
        shorturls.append(shorturl)
        urls.append(url)
        cur_url_id += 1
    else:
        id_url = map_url_to_id[url]
        shorturl = shorturls[id_url]

    return shorturl


def restore(short_url: str) -> Optional[str]:
    try:
        return urls[shorturl_to_id(short_url)]
    except IndexError:
        return None


def main():
    assert len(id_to_shorturl(2)) == 6
    assert id_to_shorturl(2) == f'00000{alphanums[2]}'

    print(shorten("www.google.fr"))
    print(shorten("www.google.fr/toto"))
    print(shorten("www.google.fr/toto/tata"))
    print(shorten("www.google.fr"))

    assert restore(shorten("www.google.fr")) == "www.google.fr"
    assert restore("dummy") is None
    assert restore(shorten("www.google.fr/toto/tata")) == "www.google.fr/toto/tata"

    print(shorturl_to_id(shorten("www.google.fr")))
    print(shorturl_to_id(shorten("www.google.fr/toto/tata")))


if __name__ == '__main__':
    main()
