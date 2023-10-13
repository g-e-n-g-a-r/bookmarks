import requests
import json 


if __name__ == "__main__":
    a = 'https://api.github.com/users/g-e-n-g-a-r/starred?per_page=100&page='
    b = 1
    c = ''.join([a, str(b)])
    d = requests.get(c)
    e = d.text
    f = json.loads(e)
    with open('docs/stars.md', 'w') as g:
        while len(f):
            for h in f:
                i = h.get('name')
                j = h.get('html_url')
                k = [' - [', i, '](', j, ')\n']
                l = ''.join(k)
                g.write(l)
            b += 1
            c = ''.join([a, str(b)])
            d = requests.get(c)
            e = d.text
            f = json.loads(e)
