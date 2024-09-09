from django.http import HttpResponse 
from django.shortcuts import render , redirect , get_object_or_404
from django.urls import reverse , reverse_lazy
from .models import Articles
from .forms import ArticlesForm , CommentForm
from django.views.generic import ListView , CreateView , DeleteView , UpdateView , DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    return HttpResponse("hello words")

class ArticlesListView(ListView):
    model = Articles
    template_name = 'Articles/List.html' 
    context_object_name = 'articles'

class ArticlesCreateView(LoginRequiredMixin, CreateView):
    model = Articles
    form_class = ArticlesForm
    template_name = 'Articles/formulaire.html'
    success_url = reverse_lazy('List_articles')

    def form_valid(self, form):
        # Associer l'utilisateur connecté à l'article avant de l'enregistrer
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ArticlesDeleteView(DeleteView):
    model = Articles
    template_name = 'Articles/delete_article.html'
    success_url = reverse_lazy('List_articles')


class ArticlesUpdateView(LoginRequiredMixin,UpdateView):
    model = Articles
    form_class = ArticlesForm
    template_name = 'Articles/update_article.html'
    success_url = reverse_lazy('List_articles')
    
class ArticlesDetailView(DetailView):
    model = Articles
    template_name = 'Articles/detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context
    

def add_comment(request, id):

    if request.method == 'POST':
        article = Articles.objects.get(id=id)
        # initial = {'article': article}
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.owner = request.user
            comment.save()
        else:
            context = {
                'article': article,
                'form': form
            }
            return render(request, 'articles/article_detail.html', context)
    return redirect('detail_article', article.id)

# def List_articles(request):
#     articles = Articles.objects.all()
#     context = {
#         'articles' : articles
#     }
    
#     return render(request,'Articles/List.html',context)



# def formulaire(request):
#     if request.method == 'POST':
#         form = ArticlesForm(request.POST , files=request.FILES)
#         if form.is_valid():
#             # cleaned_data = form.cleaned_data
#             # article = Articles(**cleaned_data)
#             # article.title = cleaned_data['title']
#             # article.sumary = cleaned_data['sumary']
#             # article.date_pub = cleaned_data['date_pub']
#             # article.content = cleaned_data['content']
#             form.save()
#             return redirect(reverse('List_articles'))
#         else :
#             print(form.errors)
#     else :
#         form = ArticlesForm()
#     context  = {
#         'form': form
#     }
#     return render(request,'Articles/formulaire.html',context)


# def delete_article(request, article_id):
#     article = get_object_or_404(Articles, id=article_id)
#     if request.method == 'POST':
#         article.delete()
#         return redirect(reverse('List_articles'))
#     context = {
#         'article': article
#     }
#     return render(request, 'Articles/delete_article.html', context)


# def update_article(request, article_id):
#     article = get_object_or_404(Articles, id=article_id)

#     if request.method == 'POST':
#         form = ArticlesForm(request.POST, instance=article)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('List_articles'))
#     else:
#         form = ArticlesForm(instance=article)

#     context = {
#         'form': form,
#         'article': article
#     }
#     return render(request, 'Articles/update_article.html', context)
         
