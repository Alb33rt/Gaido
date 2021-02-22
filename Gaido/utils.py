from blog.models import Type, Region

def get_categories():
    categories = [i[1] for i in Type.CHOICES]
    return categories

def get_regions():
    regions = [i[1] for i in Region.REGION_CHOICES]
    return regions