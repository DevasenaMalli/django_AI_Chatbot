from django.shortcuts import render,redirect
import openai
from.models import Past
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
#openai.api_key = "sk-proj-zIJ5utwB16d9AplGmwaiKfb4mtrtWkDhk9-"

def home(request):
   
   if request.method == 'POST':
   
    question = request.POST['question']
    past_response = request.POST.get('past_response','')
    openai.api_key = "my_openai_key"

    openai.Model.list()
    try:
        response = openai.ChatCompletion.create(
            model = "gpt-4o",
            messages = [{"role": "user", "content": question}],
            temperature= 0,
            max_tokens = 60,
            top_p = 1.0,
            frequency_penalty = 0.0,
            presence_penalty = 0.0,
          )  
        #parse the response

        response = (response["choices"][0]["message"]["content"]).strip()
        #logic for Past response

        if "41elder41" in past_response:
            past_response = response
        else:
            past_response = f"{past_response}</br></br>{response}"

        # Save To Database
        record = Past(question=question, answer=response)
        record.save()

        return render(request, 'home.html', {'question': question,"response":response,"past_response":past_response})
    except Exception as e:
        return render(request, 'home.html',{'question': question,"response":e,"past_response":past_response})
   return render(request, 'home.html')



def past(request):
    p = Paginator(Past.objects.all(), 5)
    page = request.GET.get('page')
    pages = p.get_page(page)

    past = Past.objects.all()
    return render(request,'past.html',{"past":past,"pages":pages})


def delete_past(request,id):
    past = Past.objects.get(id=id)
    past.delete()
    messages.success(request, ("Message got delete successfully.."))
    return redirect('past')