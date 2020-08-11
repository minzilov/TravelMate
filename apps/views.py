from django.shortcuts import render

# Create your views here.

def opening(request):
    return render(request, 'opening.html')

def diary(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dictionary = {}

    for word in words:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    return render(request, 'result.html', {'full':text, 'total':len(words), 'dictionary':word_dictionary.items()})
