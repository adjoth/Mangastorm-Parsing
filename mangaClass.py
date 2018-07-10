## Manga Class
# Reading = R
# Following = Y
# Archive = A
# floating point number meaning is unknown

## SITES LISTING ##
# z03mangahere
# z10readmangatoday
# mangareader
# mangafoxmb     # Moblie Site
# mangafox       # Desktop Site
# z02batoto


class Manga():
    def __init__(self, site=0, title=0, url=0, status=0, num=0):
        self.site = site
        self.title = title
        self.url = url
        self.status = status
        self.num = num
        
    def site(self, site):           # Reasigns Site
        self.site = site
    def title(self, title):         # Reasigns Title
        self.title = title
    def url(self, url):             # Reasigns URL
        self.url = url
    def status(self, status):       # Reasigns Status
        self.status = status
    def num(self, num):             # Reasigns Num
        self.num = num

    def rsite(self):                # Returns Site
        return self.site
    def rtitle(self):               # Returns Title
        return self.title
    def rurl(self):                 # Returns URL
        return self.url
    def rstatus(self):              # Returns Status
        return self.status
    def num(self):                  # Returns Num
        return self.num
