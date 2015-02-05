from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse

from users.models import User

def index(request):
    user_list = User.objects.order_by('-login_date')[:5]
    """
    template = loader.get_template('users/index.html')
    context = RequestContext(request, {
        'user_list': user_list,
    })
    return HttpResponse(template.render(context))
    """
    context = {'user_list': user_list}
    return render(request, 'users/index.html', context)

def detail(request, user_id):
    # user = get_object_or_404(User, pk=user_id)
    try:
      u = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("Question does not exist")
    #return HttpResponse(u)
    return render(request, 'users/detail.html', {'user': u})

def results(request, user_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % user_id)

def vote(request, user_id):
    u = get_object_or_404(User, pk=user_id)
    try:
        selected_payment = u.payment_set.get(pk=request.POST['payment'])
    except (KeyError, User.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'users/detail.html', {
            'user': u,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_payment.price += 1000
        selected_payment.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('users:results', args=(u.id,)))
    return HttpResponse("You're voting on question %s." % user_id)
