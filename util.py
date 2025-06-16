import os, requests

def auth():
    auth_session = requests.get(url="https://api.fishtank.live/v1/auth", headers={"Cookie": "sb-wcsaaupukpdmqdjcgaoo-auth-token=%5B%22eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1YTI5ZWI0OC1hZmZlLTRhZGUtOWMyYS1iMDA2ZmZmMDdiZGYiLCJpYXQiOjE3NTAxMDA5NjksImV4cCI6MTc1MDEwMTg2OX0.MHHw5FjTSHy4wZIzgLmmIguHs_PdsehUcgs_RO7iUf8%22%2C%22eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1YTI5ZWI0OC1hZmZlLTRhZGUtOWMyYS1iMDA2ZmZmMDdiZGYiLCJpYXQiOjE3NTAxMDA5NjksImV4cCI6MTc1MjY5Mjk2OX0.5uICDwbzJUyHDvFClGumPB4eYWSPoMJwriKYA_i2GIg%22%5D; ph_phc_OS9anuhxekzZwfvZPJFdY5NSiKmmxY7h0DqI9pSDVRj_posthog=%7B%22distinct_id%22%3A%225a29eb48-affe-4ade-9c2a-b006fff07bdf%22%2C%22%24sesid%22%3A%5B1750100654156%2C%22019779e5-3cf3-72a9-a3d6-62cef89d1f36%22%2C1750096755955%5D%2C%22%24epp%22%3Atrue%2C%22%24initial_person_info%22%3A%7B%22r%22%3A%22%24direct%22%2C%22u%22%3A%22https%3A%2F%2Fwww.fishtank.live%2F%22%7D%7D"}).json()["session"]
    access_token = auth_session["access_token"]
    refresh_token = auth_session["refresh_token"]
    return auth_session, access_token, refresh_token

