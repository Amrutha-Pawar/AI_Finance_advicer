from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def finance_advice(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            income = float(data.get("income", 0))
            expenses = float(data.get("expenses", 0))
            goal = float(data.get("goal", 0))

            remaining = income - expenses

            # Simple logic for AI-style advice
            if remaining > goal:
                advice = "You're saving well! Consider investing the extra funds."
            elif remaining == goal:
                advice = "Perfect balance — you’re achieving your goals smoothly!"
            else:
                advice = "Try to reduce expenses or find extra income sources."

            return JsonResponse({
                "remaining": remaining,
                "advice": advice
            })

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Only POST method allowed"}, status=405)
