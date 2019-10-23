from django.shortcuts import render
from .datasource import AdverityReader


def index(request):
    datasources_values = request.POST.getlist('datasources')
    campaigns_values = request.POST.getlist('campaigns')
    reader = AdverityReader(
        'http://adverity-challenge.s3-website-eu-west-1.amazonaws.com/'
        'DAMKBAoDBwoDBAkOBAYFCw.csv'
    )

    frame = reader.get_data_frame()
    datasources = list(set(frame['Datasource']))
    campaigns = list(set(frame['Campaign']))

    result = frame
    if datasources_values:
        result = frame[(frame.Datasource.isin(datasources_values))]
    if campaigns_values:
        result = frame[(frame.Campaign.isin(campaigns_values))]

    clicks = result[['Date', 'Clicks']].values.tolist()
    impressions = result[['Date', 'Impressions']].values.tolist()

    context = dict(
        clicks=clicks,
        impresions=impressions,
        datasources_options=datasources,
        datasources_values=datasources_values,
        campaigns_options=campaigns,
        campaigns_values=campaigns_values,
    )
    return render(request, 'dashboard/index.html', context)
