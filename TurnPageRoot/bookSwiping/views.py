from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.generic import ListView, TemplateView
from .models import *
import random


# Create your views here.
class BookshelfView(LoginRequiredMixin, TemplateView):
    model = Book
    template_name = 'bookSwiping/bookshelf.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        random_items = random.sample(list(self.model.objects.all()), 10)
        saved_books = random.sample(list(self.model.objects.all()), 10)
        context['books'] = random_items
        context['saved_books'] = saved_books
        return context


@login_required
@require_POST
def book_like(request):
    book_id = request.POST.get('id')
    action = request.POST.get('action')
    if book_id and action:
        try:
            book = Book.objects.get(id=book_id)
            if action == 'like':
                book.users_liked_list.add(request.user)
            else:
                book.users_liked_list.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except Book.DoesNotExist:
            pass
    return JsonResponse({'status': 'error'})


class HomeView(ListView):
    model = Book
    context_object_name = "books"
    template_name = "bookSwiping/home.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        all_books = self.model.objects.all()
        items = list(self.model.objects.all())
        # change to how many random items you want
        random_items = random.sample(items, 15)
        # creates a list of books, random for now, from the database
        context["all_books"] = all_books
        context["book01"] = random_items[0]
        context["book02"] = random_items[1]
        context["book03"] = random_items[2]
        context["book04"] = random_items[3]
        context["book05"] = random_items[4]
        context["book06"] = random_items[5]
        context["book07"] = random_items[6]
        context["book08"] = random_items[7]
        context["book09"] = random_items[8]
        context["book10"] = random_items[9]
        context["book11"] = random_items[10]
        context["book12"] = random_items[11]
        context["book13"] = random_items[12]
        context["book14"] = random_items[13]
        context["book15"] = random_items[14]
        return context
