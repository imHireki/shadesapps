from django.shortcuts import redirect, render


def redir(request):
    return redirect('/')

def robots_txt(request):
    return render(request, 'robots.txt', content_type='text/plain')

def sitemap_xml(request):
    return render(request, 'sitemap.xml', content_type='text/xml')
