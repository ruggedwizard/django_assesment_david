from django.http import JsonResponse
from django.contrib.auth.models import AnonymousUser
from base.models import Expense, Budget

class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        user = request.user 
        print(response)
        
        if "expenses" in request.path:
            if request.method == "GET":
                expense_split = request.path.split("/")
                if len(expense_split) != 4:
                    # there is not expense_id, continue with the request
                    response = self.get_response(request)
                    return response
                if isinstance(user, AnonymousUser):
                    return JsonResponse(
                                {
                                    "success": False,
                                    "message": "Unauthorized",
                                },
                                status=401,
                            )                   
                # there is expense_id
                expense_id = expense_split[-2]
                # you have the expense_if, get the expense object and check if the logged in user is the owner of the object
                if not Expense.objects.filter(id=expense_id, user=user).exists():
                    # the user is not the owner of the expense object, return 403
                    return JsonResponse(
                        {
                            "success": False,
                            "message": "You are not the creator of this expense",
                        },
                        status=403,
                    )
                else:
                    # the logged in user is the author of the expense object
                    # continue with the request
                    response = self.get_response(request)
                    return response
        if "budget" in request.path:           
            if request.method == "GET":
                budget_split = request.path.split("/")
                #the split array will hae 4 elements: ['BASE_URL', 'budgets', 'budget_id', '']
                if len(budget_split) != 4:
                    # there is not budget_id, continue with the request
                    response = self.get_response(request)
                    return response
                if isinstance(user, AnonymousUser):
                    return JsonResponse(
                                {
                                    "success": False,
                                    "message": "Unauthorized",
                                },
                                status=401,
                            )    
                # there is budget_id
                budget_id = budget_split[-2]
                # you have the budget_id, get the expense objet and ccheck if the logged in user is the owner of the object
                if not Budget.objects.filter(id=budget_id, user=user).exists():
                    # the user is not the owner of the expense object, return 403
                    return JsonResponse(
                        {
                            "success": False,
                            "message": "You are not the creator of this budget",
                        },
                        status=403,
                    )
                else:
                    # the logged in user is the author of the expense object
                    # continue with the request
                    response = self.get_response(request)
                    return response
        return response
