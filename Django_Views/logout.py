def logout(request):
    print(request.session)
    request.session.clear()
    print(request.session)
    # messages.success(request, "You have successfully logged out !")
    return redirect('/')
