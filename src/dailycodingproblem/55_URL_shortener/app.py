"""

"""
import attr
from typing import List, Optional

alphanums = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
map_alphanum_to_id = {
    **{
        alphanum: ord(alphanum) - ord('0')
        for alphanum in alphanums[:10]
    },
    **{
        alphanum: ord(alphanum) - ord('a') + 10
        for alphanum in alphanums[10:10 + 26]
    },
    **{
        alphanum: ord(alphanum) - ord('A') + (10 + 26)
        for alphanum in alphanums[10 + 26:]
    },
}
base = len(alphanums)
# with 6 coefficients in base-62, we can produce 56 800 235 584 values

map_url_to_id = {}


@attr.s(frozen=True, slots=True)
class URLShortenURL:
    __weakref__ = attr.ib(init=False, hash=False, repr=False, cmp=False)
    #
    url: str = attr.ib()
    shorten_url: str = attr.ib()


urls_shorturls = []     # type: List[URLShortenURL]
pk_id = 0  #  primary key for url id


def id_to_shorturl(id_url: int) -> str:
    """
    Generate shorten url from id (with our bijective function using our base)
    The shorten url will be len == 6 and all characters in ['0...9','a...z','A...Z']

    :param id_url:
    :return:

    >>> id_to_shorturl(0)
    '000000'
    >>> id_to_shorturl(10)
    '00000a'
    >>> id_to_shorturl(62**6 - 1)
    'ZZZZZZ'
    >>> id_to_shorturl(62**6 - 1 + 1)
    '000000'
    >>> id_to_shorturl(62**6 - 1 + 2)
    '000001'
    """
    shorten_url = ""
    id_url = id_url % 56800235584    # 62**6=56800235584
    while id_url > 0:
        int_digit = id_url % base
        shorten_url += alphanums[int_digit]
        id_url = id_url // base
    return '0' * (6 - len(shorten_url)) + shorten_url   # pad with '0' (neutral element) shorten url produce


def shorturl_to_id(short_url: str) -> int:
    """

    :param short_url: Valid short url (len == 6, all characters in ['0...9','a...z','A...Z']
    :return:

    >>> shorturl_to_id('000000')
    0
    >>> shorturl_to_id('00000a')
    10
    >>> shorturl_to_id('dummy_id')

    """
    if len(short_url) != 6:
        raise ValueError

    id_url = 0

    try:
        for c in short_url:
            id_url = id_url * base + map_alphanum_to_id[c]
    except KeyError:
        raise ValueError

    return id_url


def shorten(url: str) -> str:
    """

    :param url:
    :return:

    >>> shorten("www.google.fr")
    '000000'
    >>> shorten("www.hotmail.com")
    '000001'
    >>> shorten("www._hotmail_.com")
    '000002'
    """
    global pk_id

    # using map/dict to searching request url
    if url not in map_url_to_id:
        # if this request url not exist ->
        # associate url to (primary key) url id
        map_url_to_id[url] = pk_id
        # generate shorten url from (primary key) id (using bijective function)
        shorten_url = id_to_shorturl(pk_id)
        # save pairing (url, shorten url)
        urls_shorturls.append(URLShortenURL(url, shorten_url))
        # (auto) increment (primary key) url id
        pk_id += 1
    else:
        # else retrieve information
        shorten_url = urls_shorturls[map_url_to_id[url]].shorten_url

    return shorten_url


def restore(short_url: str) -> Optional[str]:
    """

    :param short_url:
    :return:

    >>> restore(shorten("www.google.fr"))
    'www.google.fr'
    >>> restore(shorten("www.hotmail.com"))
    'www.hotmail.com'
    >>> restore(shorten("www._hotmail_.com"))
    'www._hotmail_.com'
    >>> restore(shorten("www.@hotmail@.com"))
    'www.@hotmail@.com'

    >>> restore('invalid_shorten_url') is None
    True

    """
    try:
        return urls_shorturls[shorturl_to_id(short_url)].url
    except (IndexError, ValueError):
        return None


def tests():
    assert len(id_to_shorturl(2)) == 6
    assert id_to_shorturl(2) == f'00000{alphanums[2]}'

    test_urls = [
        "www.google.fr",
        "www.google.fr/toto",
        "www.google.fr/toto/tata",
        "www.google.fr",
    ]
    test_shorter_urls = [
        shorten(url)
        for url in test_urls
    ]

    assert all(map(lambda su: len(su) == 6, test_shorter_urls))

    for url, shorten_url in zip(test_urls, map(lambda usu: usu.shorten_url, urls_shorturls)):
        assert shorten(url) == shorten_url

    assert len(set(test_shorter_urls)) == len(set(test_urls))

    assert restore(shorten("www.google.fr")) == "www.google.fr"
    assert restore("dummy") is None
    assert restore(shorten("www.google.fr/toto/tata")) == "www.google.fr/toto/tata"

    assert shorturl_to_id(shorten("www.google.fr")) == 0
    assert shorturl_to_id(shorten("www.google.fr/toto/tata")) == 2


def main():
    tests()


if __name__ == '__main__':
    main()
