# Problem

This problem was asked by Microsoft.

Implement a URL shortener with the following methods:

shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
restore(short), which expands the shortened string into the original url.
If no such shortened string exists, return null.

Hint: What if we enter the same URL twice?

# Solution

## How to design a tiny URL or URL shortener?

https://www.geeksforgeeks.org/how-to-design-a-tiny-url-or-url-shortener/

### One Simple Solution could be Hashing

Use a hash function to convert long string to short string.
In hashing, that may be collisions (2 long urls map to same short url)
and we need a unique short url for every long url so that we can access long url back.

# A Better Solution is to use the integer id stored in database

and convert the integer to character string that is at most 6 characters long.
This problem can basically seen as a base conversion problem
where we have a 10 digit input number and we want to convert it into a 6 character long string.
