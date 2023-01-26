from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_params(request):
    """

    """
    name_query = request.GET.get('name')
    surname_query = request.GET.get('surname')
    content = {
        'name':name_query,'surname':surname_query
    }
    return Response(content, status=status.HTTP_200_OK)

#def get_params():
#    content = {

#    }

    #return Response(content, status=status.HTTP_200_OK)