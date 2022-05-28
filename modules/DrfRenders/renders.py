from rest_framework import renderers
import json

class SerializerDataRender(renderers.JSONRenderer):

    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):  

        if renderer_context is not None:
            response_code = renderer_context['response'].status_code 


        if 'ErrorDetail' in str(data):
            return  json.dumps({
                'status':'failed',
                "data_type": str(type(data)) ,
                "response_code":response_code,
                'errors': data })
       
        return json.dumps({
                'status':'succuss',
                 "data_type": str(type(data)) ,
                 "response_code":response_code,
                'data': data})
       