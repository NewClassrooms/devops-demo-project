from django.shortcuts import render, resolve_url
from django.views.decorators.http import require_safe

# Create your views here.
@require_safe
def homepage(request):
    graphql_endpoint = request.build_absolute_uri(resolve_url('graphql'))
    return render(request, "schooldata/homepage.html", {"graphql_endpoint": graphql_endpoint})
