from rest_framework.views import APIView
from pymongo.mongo_client import MongoClient
from rest_framework.response import Response
from feeds.basic_authentication import basic_authentication
from PIL import Image   
class feed(APIView):

    def get(self, request):
        auth = request.META['HTTP_AUTHORIZATION']
        head = basic_authentication()
        if auth == basic_authentication():
            page =int(request.query_params.get('page',1))
            client = MongoClient()
            db = client.Explore
            collection = db.Story
            response = [post for post in collection.find({}, {'_id': 0}).skip((page -1)*5).limit(5)]
            return Response(response)

class getImage(APIView):

    def get(self,request):
#       img = request.query_params().get('image_uri')
        import pdb; pdb.set_trace();
        img = image.view("/home/saurabh/Desktop/images/1.png")
        return Response(img, content_type="image/png")