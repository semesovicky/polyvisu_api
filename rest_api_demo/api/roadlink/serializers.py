from flask_restplus import fields
from rest_api_demo.api.restplus import api

roadlink = api.model('Traffic Intensities', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of roadlink'),
    'traffic_intensity': fields.Integer(required=True, description='Number of passing cars for one hour'),
})

time_arguments = api.model('Results for certain time period', {
    'start_time': fields.String(descriptiopn='Timestamp of the start of measurements'),
    'end_time': fields.String(descriptiopn='Timestamp of the end of measurements'),
})

set_of_roadlinks = api.inherit('Set of traffic intensities', time_arguments,  {
	'items': fields.List(fields.Nested(roadlink))
})

#category = api.model('Blog category', {
#	'id': fields.Integer(readOnly=True, description='The unique identifier of a blog category'),
#	'name': fields.String(required=True, description='Category name'),
#})

#category_with_posts = api.inherit('Blog category with posts', category, {
#	'posts': fields.List(fields.Nested(blog_post))
#})
