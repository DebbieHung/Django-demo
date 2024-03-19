from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.


def user_register(request):
    message = ""
    form = UserCreationForm()
    # 取得所有all=>User.objects.all()
    # 取得唯一get=>User.objects.get(username="debbie")
    # 取得篩選filter=>User.objects.filter(username="debbie1")
    # print(User.objects.filter(username="debbie1"))
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        print(username, password1, password2)

        try:
            if len(password1) < 8:
                message = "密碼長度必須包含至少8個字元"
            elif password1 != password2:
                message = "兩次密碼不匹配"
            else:
                # 檢查使用者是否存在
                user = User.objects.filter(username=username)
                if len(user) >= 1:
                    message = "帳號已經存在"
                else:
                    User.objects.create_user(
                        username=username, password=password1
                    ).save()
                    message = "註冊成功"
        except Exception as e:
            print(e)
            message = "不明錯誤發生..."

    return render(request, "user/register.html", {"form": form, "message": message})
