import json
import socket
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView
from django.template import Template, Context, RequestContext
from grooveGenerator.models import Color
from grooveGenerator.Groove import *

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

def ajax1(request):
   if request.POST.has_key('client_response'):
       
        #x = request.POST['client_response']
        #y = socket.gethostbyname(x)
        #response_dict = {}
        #response_dict.update({'server_response': y }) 
        #return HttpResponse(json.dumps(response_dict), content_type='application/json') 
        #myGroove = Groove(request.POST['client_response'], request.POST['client_chord_progression'])
        #myGroove = Groove(request.POST['client_response'])
        #print str(request.POST.getlist('client_chord_progression[]'))
        if request.POST.has_key('client_chord_3'):
            print "we have chords!"
        else:
            print "we have no chords WTF m8"

        """ Build chord progression list """
        inputChordList = []
        if request.POST.has_key('client_chord_0'):
            inputChordList.append(int(request.POST['client_chord_0']))
        else:
            inputChordList.append(0)
        if request.POST.has_key('client_chord_1'):
            inputChordList.append(int(request.POST['client_chord_1']))
        else:
            inputChordList.append(0)
        if request.POST.has_key('client_chord_2'):
            inputChordList.append(int(request.POST['client_chord_2']))
        else:
            inputChordList.append(0)
        if request.POST.has_key('client_chord_3'):
            inputChordList.append(int(request.POST['client_chord_3']))
        else:
            inputChordList.append(0)

        if inputChordList:
            print request.POST['client_response']
            print inputChordList
        myGroove = Groove(request.POST['client_response'], inputChordList)
        #myGroove = Groove(request.POST['client_response'])
        #myGroove.key = request.POST['client_response']
        myGroove.genMelody()
        currList = []
        genList = []
        durationMapToStr = {1.0:"q", 0.5:"h", 0.25:"q", 0.125:"e", 0.0625:"s"}
        for phrase in myGroove.melody.phraseList:
            for note in phrase.noteList:
                keyOffset = 0
                if myGroove.key == "C":
                    keyOffset = 0
                if myGroove.key == "D":
                    keyOffset = 2
                if myGroove.key == "E":
                    keyOffset = 4
                if myGroove.key == "F":
                    keyOffset = 5
                if myGroove.key == "G":
                    keyOffset = 7
                if myGroove.key == "A":
                    keyOffset = 9
                if myGroove.key == "B":
                    keyOffset = 11
                currList.append(keyOffset + note.octave*12+note.noteVal+Groove.scaleSteps[note.noteVal])
                #for i in range(len(currList)):
                genList.append(str(myGroove.allTMNotesList[currList[-1]]) + " " + durationMapToStr[note.duration]) 
        # TODO Currently finishes on root note
        genList.append(str(myGroove.allTMNotesList[currList[0]]) + " h") 
        currBassList = []
        for phrase in myGroove.melody.phraseList:
            for note in phrase.underlyingList:
                keyOffset = 0
                # Use proper key offsets
                if myGroove.key == "C":
                    keyOffset = 0
                if myGroove.key == "D":
                    keyOffset = 2
                if myGroove.key == "E":
                    keyOffset = 4
                if myGroove.key == "F":
                    keyOffset = 5
                if myGroove.key == "G":
                    keyOffset = 7
                if myGroove.key == "A":
                    keyOffset = 9
                if myGroove.key == "B":
                    keyOffset = 11
                currBassList.append(keyOffset + note.octave*12+note.noteVal+Groove.scaleSteps[note.noteVal])
                #print "Adding: " + str(keyOffset + note.octave*12+Groove.scaleSteps[note.noteVal])
        response_dict = {}
        genBassList = []
        #for i in range(len(currList)):
        #    genList.append(str(myGroove.allTMNotesList[currList[i]]) + " e") 
        for i in range(len(currBassList)):
            genBassList.append(str(myGroove.allTMNotesList[currBassList[i]]) + " w") 
        # TODO Currently finishes on root note
        genBassList.append(str(myGroove.allTMNotesList[currBassList[0]]) + " h") 
        #response_dict.update({'server_response_lead': ['lolz', 'lulz'] })
        #response_dict.update({'server_response_lead': genList})
        response_dict.update({'server_response_lead': genList, 'server_response_bass': genBassList })
        return HttpResponse(json.dumps(response_dict), content_type='application/json') 
        
   else:
        return Http404("IDKYET LOL")


