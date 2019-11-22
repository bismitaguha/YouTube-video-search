import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

import os

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def youtubeApi():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret_242612500753-vioq36brgj6p7j1dvq7ro51v1ht610rr.apps.googleusercontent.com.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.search().list(
        part="snippet",
        forDeveloper=True,
        maxResults=25,
        q="funny",
        order="date"
    )
    response = request.execute()

    # webbrowser.open_new_tab("https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=242612500753-vioq36brgj6p7j1dvq7ro51v1ht610rr.apps.googleusercontent.com&redirect_uri=urn%3Aietf%3Awg%3Aoauth%3A2.0%3Aoob&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fyoutube.force-ssl&state=FFcHK8eY5NPEaiEegti463USFa9S1g&prompt=consent&access_type=offline&code_challenge=IU6q_O-C2nvah6S4xGmkSKOnRUxBFBR0w8F2MZGXytI&code_challenge_method=S256")

    return response