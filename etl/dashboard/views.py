from django.shortcuts import render
from .datasource import AdverityReader


def index(request):
    reader = AdverityReader(
        "http://adverity-challenge.s3-website-eu-west-1.amazonaws.com/"
        "DAMKBAoDBwoDBAkOBAYFCw.csv"
    )
    df = reader.get_data_frame()
    context = dict(question=df)
    return render(request, 'dashboard/index.html', context)
