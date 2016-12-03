# coding: utf-8

from facepy import GraphAPI

DESIRED_STATUS = "Test status for FB"

# generate this access token from 'https://developers.facebook.com/tools/explorer'
access_token = 'EAACEdEose0cBAGkai82xt32tWaE2YoXP3YRmHrnV0C1o72a89eiP8UOTsGD3ateB8ajr15xCTGKzaDDLjd13GN3beuz3PXmWFyUHqZAxItk9gE9Eayyf7mlOWvevUOHqcoozgEysnZBUuzgiDRlwNLdcfqZAgZATXYxXYcAgHgZDZD'
apiConnection = GraphAPI(access_token)

apiConnection.post(path='me/feed', message=DESIRED_STATUS)
