from io import StringIO
from pandas import read_csv
from requests import get


class AdverityReader(object):

    data = None

    def __init__(self, url):
        """Construct reader with given URL."""
        self.url = url

    def get_data_frame(self):
        """Get data frame from given URL."""
        if not self.data:
            content = get(self.url).text
            self.data = read_csv(StringIO(content))

        return self.data
