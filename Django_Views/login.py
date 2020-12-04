def login(request):
    if request.method == "GET":
        return redirect('/')
    if not User.objects.authenticate(request.POST['email'], request.POST['password']):
        messages.error(request, 'Invalid Email or Password')
        return redirect('/')
    user = User.objects.get(email=request.POST['email'])
    request.session['user'] = user.first_name
    request.session['user_id'] = user.id
    # messages.success(request, "You have successfully logged in !")
    return redirect('/success')
