from pymongo.mongo_client import MongoClient
from rest_framework.response import Response
from rest_framework.views import APIView

from feeds.basic_authentication import basic_authentication


class feed(APIView):

    def get(self, request):
        auth = request.META['HTTP_AUTHORIZATION']
        head = basic_authentication()
        if auth == basic_authentication():
            page = int(request.query_params.get('page', 1))
            client = MongoClient()
            db = client.Explore
            collection = db.story
            response = [post for post in collection.find({}, {'_id': 0}).skip((page - 1) * 5).limit(5).sort('index', direction=1)]
            return Response(response)
        
        return Response({"Not Authenticated":304})

class search(APIView):
    
    def get(self, request):
        auth = request.META['HTTP_AUTHORIZATION']
        head = basic_authentication()
        if auth == basic_authentication():
            query = request.query_params.get('q', 'a')
            client = MongoClient()
            db = client.test
            collection = db.loc
            import re
            string = "^" + query 
            regx = re.compile(string, re.IGNORECASE)
            response = [post for post in collection.find({'value':{'$regex' : regx}}, {'_id': 0})]
            return Response(response)

