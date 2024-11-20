import os
from django.http import HttpResponse

def frontend(request):
    # Construct the path to React's built index.html
    index_path = os.path.join(os.path.dirname(__file__), '../frontend/build/index.html')
    try:
        with open(index_path, 'r') as f:
            return HttpResponse(f.read())  # Serve the index.html file
    except FileNotFoundError:
        return HttpResponse("React app not found. Please build your React app.", status=404)
