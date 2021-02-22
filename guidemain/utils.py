from blog.models import Type, Region

def find_match_specific(query):
    match = [i[0] for i in Type.CHOICES if i[1] == query]
    if not match:
        match = [i[0] for i in Region.REGION_CHOICES if i[1] == query]

    return match