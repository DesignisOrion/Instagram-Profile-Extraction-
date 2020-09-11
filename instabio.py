# Today I was introduced to the instaloader module.
# This program allows you to extract the username, Followers and Bio of an instagram page. Enjoy!
# Author : Orion F. www.DesignIsOrion.com


import instaloader
L = instaloader.Instaloader()
profile = instaloader.Profile.from_username(
    L.context, 'BlackDevsRock')

print(profile.full_name)
print(profile.followers)
print(profile.biography)
