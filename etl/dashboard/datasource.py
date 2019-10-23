from io import StringIO
from pandas import read_csv, DataFrame
from requests import get


class AdverityReader(object):

    data = None

    def __init__(self, url):
        """Construct reader with given URL."""
        self.url = url

    def get_data_frame(self):
        """Get data frame from given URL."""
        if not self.data:
            try:
                content = get(self.url).text
                self.data = read_csv(StringIO(content))
            except ValueError as e:
                return DataFrame()

        return self.data
