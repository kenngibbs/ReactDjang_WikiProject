from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from .models import MainWikiModel, RelatedWikiModel
from .forms import MainWikiForm, RelatedWikiForm, UserForm
from django.contrib import messages


# Create your views here.
def index(request):
    form = UserForm(request.POST or None)
    if request.method == "POST":
        checkUserAuth = authenticate(username= request.POST["username"], password= request.POST["password"])
        if checkUserAuth is not None:
            print(checkUserAuth)
            login(request, checkUserAuth)
            return redirect("index")
        else:
            messages.error(request, "Username or password incorrect!")
    context = {
        "titleText": "All Wiki Entries Below",
        "form": form,
        "allWikis": MainWikiModel.objects.all(),
    }
    return render(request, "WikiApp/index.html", context)


def userEntries(request):
    context = {
        "allWikis": MainWikiModel.objects.filter(userForeignKey=request.user),
    }
    return render(request, "WikiApp/user_wiki_entries.html", context)


def newAuthor(request):
    form = UserForm(request.POST or None)
    if request.method == "POST":

        if form.is_valid():
            createNewUser = User.objects.create_user(username= request.POST["username"], email="", password= request.POST["password"])
            login(request, createNewUser)
            return redirect("index")
    context = {
        "form": form,
    }
    return render(request, "WikiApp/new_author.html", context)


def mainAdd(request):
    form = MainWikiForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        form = MainWikiForm(request.POST, request.FILES)
        if form.is_valid():
            newWikiModel = form.save(commit= False)
            newWikiModel.userForeignKey = request.user
            newWikiModel.save()
            return redirect("index")
    context = {
        "form": form,
    }
    return render(request, "WikiApp/add_main_wiki.html", context)


def mainDetails(request, mainWikiID):
    selectedMainWiki = MainWikiModel.objects.get(pk=mainWikiID)
    context = {
        "mainWiki": selectedMainWiki,
        "relatedWikis": RelatedWikiModel.objects.filter(mainForeignKey=selectedMainWiki),
    }
    return render(request, "WikiApp/detail_main_wiki.html", context)


def mainEdit(request, mainWikiID):
    selectedMainWiki = MainWikiModel.objects.get(pk=mainWikiID)
    editMainWikiForm = MainWikiForm(instance=selectedMainWiki)

    if request.method == "POST":
        editMainWikiForm = MainWikiForm(request.POST, request.FILES, instance=selectedMainWiki)
        editMainWikiForm.save()
        return redirect("mainDetails", mainWikiID)
    context = {
        "mainWikiForm": editMainWikiForm,
        "mainWikiID": mainWikiID,
        "relatedWikis": RelatedWikiModel.objects.filter(mainForeignKey=selectedMainWiki),
    }
    return render(request, "WikiApp/edit_main_wiki.html", context)


def mainDelete(request, mainWikiID):
    tempMainWiki = MainWikiModel.objects.get(pk=mainWikiID)
    tempMainWiki.delete()
    return redirect("index")


def relatedAdd(request, mainWikiID):
    form = RelatedWikiForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        tempmainWiki = get_object_or_404(MainWikiModel, pk=mainWikiID)
        print(tempmainWiki)
        if form.is_valid() and tempmainWiki:
            newRelatedWikiModel = form.save(commit= False)
            newRelatedWikiModel.mainForeignKey = tempmainWiki
            newRelatedWikiModel.save()
            return redirect("mainEdit", mainWikiID)
    context = {
        "form": form,
    }
    return render(request, "WikiApp/add_main_wiki.html", context)


def relatedEdit(request, relatedWikiID):
    selectedRelatedWiki = RelatedWikiModel.objects.get(pk=relatedWikiID)
    editRelatedWikiForm = RelatedWikiForm(instance=selectedRelatedWiki)
    mainWikiID = selectedRelatedWiki.mainForeignKey.id

    if request.method == "POST":
        editMainWikiForm = RelatedWikiForm(request.POST, request.FILES, instance=selectedRelatedWiki)
        editMainWikiForm.save()
        return redirect("mainEdit", mainWikiID)
    context = {
        "relatedWikiForm": editRelatedWikiForm,
        "relatedWikiID": relatedWikiID,
    }
    return render(request, "WikiApp/edit_related_wiki.html", context)


def relatedDelete(request, relatedWikiID):
    tempRelatedWiki = RelatedWikiModel.objects.get(pk=relatedWikiID)
    mainWikiID = tempRelatedWiki.mainForeignKey.id
    tempRelatedWiki.delete()
    return redirect("mainEdit", mainWikiID)


def wikiSearch(request):

    if request.method == 'POST':
        wikiSearchResults = MainWikiModel.objects.filter(title__contains=request.POST['searchText'])
    context = {
        # "form": form,
        "titleText": "All SearchResults Results Below",
        "allWikis": wikiSearchResults,
    }
    return render(request, "WikiApp/index.html", context)


def userLogout(request):
    logout(request)
    return redirect("index")