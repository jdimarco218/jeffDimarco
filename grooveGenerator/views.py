from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from grooveGenerator.models import Color

MIN_SEARCH_CHARS = 2
"""
The minimum number of characters required in a search. If there are less,
the form submission is ignored. This value is used by the below view and
the template.
"""
class ColorList(ListView):
    """
    Displays all colors in a table with only two columns: the name of the
    color, and a "like/unlike" button.
    """
    model = Color
    context_object_name = "colors"
 
    def dispatch(self, request, *args, **kwargs):
        self.request = request     #So get_context_data can access it.
        return super(ColorList, self).dispatch(request, *args, **kwargs)
 
    def get_queryset(self):
        """
        Returns the all colors, for display in the main table. The search
        result query set, if any, is passed as context.
        """
        return  super(ColorList, self).get_queryset()
 
    def get_context_data(self, **kwargs):
        #The current context.
        context = super(ColorList, self).get_context_data(**kwargs)
 
        global  MIN_SEARCH_CHARS
 
        search_text = ""   #Assume no search
        if(self.request.method == "GET"):
            """
            The search form has been submitted. Get the search text from
            it. If it's less than MIN_SEARCH_CHARS characters, ignore the
            request.
 
            Must be GET, not post.
            - http://stackoverflow.com/questions/25878993/django-view-works-with-default-call-but-form-submission-to-same-view-only-calls
 
            Also, must use
 
                if(self.request.method == "GET")
 
            not
 
                if(self.request.GET)
 
https://docs.djangoproject.com/en/1.7/ref/request-response/#django.http.HttpRequest.method
 
 
https://docs.djangoproject.com/en/1.7/ref/request-response/#django.http.HttpRequest.POST
 
            """
            search_text = self.request.GET.get("search_text", "").strip().lower()
            if(len(search_text) < MIN_SEARCH_CHARS):
                search_text = ""   #Ignore search
 
        if(search_text != ""):
            color_search_results = Color.objects.filter(name__contains=search_text)
        else:
            #An empty list instead of None. In the template, use
            #  {% if color_search_results.count > 0 %}
            color_search_results = []
 
        #Add items to the context:
 
        #The search text for display and result set
        context["search_text"] = search_text
        context["color_search_results"] = color_search_results
 
        #For display under the search form
        context["MIN_SEARCH_CHARS"] = MIN_SEARCH_CHARS
 
        return  context
 
 
def toggle_color_like(request, color_id):
    """Toggle "like" for a single color, then refresh the color-list page."""
    color = None
    try:
        #There's only one object with this id, but this returns a list
        #of length one. Get the first (index 0)
        color = Color.objects.filter(id=color_id)[0]
    except Color.DoesNotExist as e:
        raise  ValueError("Unknown color.id=" + str(color_id) + ". Original error: " + str(e))
 
    print("pre-toggle:  color_id=" + str(color_id) + ", color.is_favorited=" + str(color.is_favorited) + "")
 
    color.is_favorited = not color.is_favorited
    color.save()  #Commit the change to the database
 
    print("post-toggle: color_id=" + str(color_id) + ", color.is_favorited=" + str(color.is_favorited) + "")
 
    #return  redirect("grooveGenerator")  #See urls.py
    #Render the just-clicked-on like-button.
    return  render_to_response("grooveGenerator/color_like_link__html_snippet.txt",
                               {"color": color})

#def grooveGenerator(request):
#    return HttpResponse("grooveGenerator says hey there world!")
