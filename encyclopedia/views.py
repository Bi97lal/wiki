from django.shortcuts import render
from markdown2 import Markdown
from . import util
import random
def convert_md_html(title):
    content=util.get_entry(title)
    markdowner=Markdown()
    if content==None:
        return None
    else:
        return markdowner.convert(content)
            
    

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def entry(request, title):
    content = convert_md_html(title)
    if content == None:
        return render(request, 'encyclopedia/error.html',{
            'message':'Entry Does not exist'
        })
    
    else:

       return render(request, 'encyclopedia/entry.html', {
    'title': title,
    'content': content
})

def search_text(request):
    if request.method == "POST":  
        search_page = request.POST.get('q') 
        content = convert_md_html(search_page)
        if content is not None:  
            return render(request, 'encyclopedia/entry.html', {
                'title': search_page,
                'content': content
            })
        else:
            suggestion=[]
            entrys=util.list_entries()
            search_lower = search_page.lower()
            
            for entry in entrys:
                if search_lower in entry.lower()  and entry not in suggestion:
                     
                     suggestion.append(entry)
                
            return render(request, 'encyclopedia/search.html', {
              
                'suggestion':suggestion
            })
def create_page(requset):
    if requset.method=="GET":
         return render(requset, 'encyclopedia/create.html')
    else:
        title= requset.POST['title']
        content=requset.POST['content']
        IF_title_Exist=util.get_entry(title)
        if IF_title_Exist is not None:
            return render(requset, 'encyclopedia/error.html',{
            'message':'Entry  exist'
        })
        else:
            util.save_entry(title,content)
            content = convert_md_html(title) 
            return render(requset, 'encyclopedia/entry.html', {
                'title': title,
                'content': content
            })

def edit(request):
    if request.method=="POST":

       title=request.POST['title-Edit']
       content=util.get_entry(title)
       return render(request, 'encyclopedia/edit.html', {
            'title': title,
            'content': content
            })
             
def  edit_page(request):
    if request.method=="POST":
        title=request.POST['title']
        content=request.POST['content']
        util.save_entry(title,content)
        content = convert_md_html(title) 
        return render( request, 'encyclopedia/entry.html', {
            'title': title,
            'content': content
        })
   

def rand_page(request):
    entryies=util.list_entries()
    random_choice= random.choice(entryies)
    content = convert_md_html(random_choice) 
    return render( request, 'encyclopedia/entry.html', {
        'title': random_choice,
        'content': content
        })
   



        

