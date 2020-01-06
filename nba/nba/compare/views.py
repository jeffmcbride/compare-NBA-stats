from django.views.generic import TemplateView, ListView
from nba_api.stats.static import *
from .models import Team


class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        results = []
        dic = teams.find_teams_by_full_name(query)
        for i in range(len(dic)):
            results.append(dic[i]['full_name'])
            print(results)
        return results