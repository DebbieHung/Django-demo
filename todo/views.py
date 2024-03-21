from django.shortcuts import render
from .models import Todo


# Create your views here.
def todo(request):
    # todos = Todo.objects.all() 這樣無論誰登入都會看到全部人的資料，應該用filter
    todos = None
    if request.user.is_authenticated:
        todos = Todo.objects.filter(user=request.user)

    return render(request, "todo/todo.html", {"todos": todos})
