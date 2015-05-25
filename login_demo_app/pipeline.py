#!/usr/bin/python
 
from login_demo_app.models import UserProfile
def get_profile_picture(
    backend,
    user,
    response,
    details,
    is_new=False,
    *args,
    **kwargs
    ):
    img_url = None
    if backend.name == 'facebook':
        img_url = "http://graph.facebook.com/%s/picture?type=large" % response['id']
    elif backend.name == 'github':
        img_url = response.get('profile_image_url', '').replace('_normal', '')
    
    profile = UserProfile.objects.get_or_create(user = user)[0]
    profile.photo = img_url
    profile.save()


