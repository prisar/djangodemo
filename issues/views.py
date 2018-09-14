from django.http import HttpResponse
from .models import Issue

# Create your views here.
def index(request):
    all_issues = Issue.objects.all()
    html = ''
    for issue in all_issues:
        url = '/issues/' + str(issue.id) + '/'
        html += '<a href="'+ url +'">' + issue.issue_title + '</a><br>'
    return HttpResponse(html)

def detail(request, issue_id):
    html = ''
    issue = Issue.objects.get(id=issue_id)
    html += "<h2>Id: " + str(issue_id) + "</h2><br/>"
    html += "<h2>Title: " + issue.issue_title + "</h2><br/>"
    html += "<h2>Description: " + issue.description + "</h2><br/>"
    html += "<h2>Created By: " + issue.tag + "</h2><br/>"
    html += "<h2>Created By: " + issue.created_by + "</h2><br/>"
    return HttpResponse(html)