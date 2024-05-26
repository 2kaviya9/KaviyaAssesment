import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from account.models import Account
from destination.models import Destination

@csrf_exempt
def incoming_data(request):
    if request.method == 'POST':
        # Ensure the 'CL-X-TOKEN' header is present
        # if 'CL-X-TOKEN' not in request.headers:
        #     return JsonResponse({'error': 'Unauthenticated'}, status=401)
        
        # Extract app secret token from header
#        app_secret_token = request.headers['CL-X-TOKEN']
        app_secret_token = "2742"
        
        try:
            # Identify account based on the provided app secret token
            account = Account.objects.get(app_secret_token=app_secret_token)
        except Account.DoesNotExist:
            return JsonResponse({'error': 'Invalid app secret token'}, status=400)
        
        try:
            # Parse incoming JSON data
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        
        # Get destinations associated with the account
        destinations = Destination.objects.filter(account=account)
        
        for destination in destinations:
            url = destination.url
            http_method = destination.http_method
            headers = destination.headers
            
            # Prepare request headers
            request_headers = {}
            for key, value in headers.items():
                request_headers[key] = value
            
            # Send data to destination based on HTTP method
            if http_method == 'GET':
                # Append data as query parameters
                response = requests.get(url, params=data, headers=request_headers)
            elif http_method in ['POST', 'PUT']:
                # Send data as JSON payload
                response = requests.request(http_method, url, json=data, headers=request_headers)
            else:
                return JsonResponse({'error': 'Unsupported HTTP method'}, status=400)
            
            # Check response status
            if response.status_code not in [200, 201]:
                return JsonResponse({'error': f'Failed to send data to {url}'}, status=500)
        
        return JsonResponse({'message': 'Data sent to destinations successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

