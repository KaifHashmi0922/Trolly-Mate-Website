# from django.http import HttpResponse
# class IndexMiddlesUse:
#     def __init__(self,get_response):
#         self.get_response=get_response
    
#     def __call__(self,request):
#         res=self.get_response(request)
#         # print(res)
#         # return HttpResponse("")
#         if res=="empty":
#             return HttpResponse("site Under Cunstruction ")
#         else :
#             return res
#     def process_exception(self,request,exception):
#         msg=exception
#         print(msg.__class__.__name__)
#         print(msg)
#         return HttpResponse(msg)
        