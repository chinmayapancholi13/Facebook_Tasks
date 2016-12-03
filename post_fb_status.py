# coding: utf-8

from facepy import GraphAPI

DESIRED_STATUS = "Test status for FB"
# generate this access token from 'https://developers.facebook.com/tools/explorer'
YOUR_ACCESS_TOKEN = 'abcd'

access_token = YOUR_ACCESS_TOKEN
apiConnection = GraphAPI(access_token)

apiConnection.post(path='me/feed', message=DESIRED_STATUS)
