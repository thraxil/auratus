from annoying.decorators import render_to
from auratus.main.models import Photo, Album, Tag

@render_to('main/index.html')
def index(request):
    return dict(
        photos=Photo.objects.all()[:50],
        albums=Album.objects.all(),
        tags=Tag.objects.all(),
        )
