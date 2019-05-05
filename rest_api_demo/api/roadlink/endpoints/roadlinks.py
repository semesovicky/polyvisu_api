import logging

from flask import request
from flask_restplus import Resource
from rest_api_demo.api.roadlink.business import get_traffic_intensities
from rest_api_demo.api.roadlink.serializers import roadlink, set_of_roadlinks
from rest_api_demo.api.roadlink.parsers import time_arguments
from rest_api_demo.api.restplus import api
from rest_api_demo.database.models import Roadlink

log = logging.getLogger(__name__)

ns = api.namespace('roadlinks/traffic_intensity', description='Operations related to traffic intensity of roadlinks')


@ns.route('/')
class RoadlinksCollection(Resource):

	@api.expect(time_arguments)
	@api.marshal_with(set_of_roadlinks)
	def get(self):
		"""
		Returns list of roadlinks.
		"""
		args = time_arguments.parse_args(request)
		start_time = args.get('start_time')
		end_time = args.get('end_time')

		roadlinks_query = get_traffic_intensities(start_time, end_time)
		return roadlinks_query

'''@api.expect(roadlink)
	def post(self):
		"""
		Creates a new blog post.
		"""
		create_roadlink(request.json)
		return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Post not found.')
class RoadlinkItem(Resource):

	@api.marshal_with(roadlink)
	def get(self, id):
		"""
		Returns a blog post.
		"""
		return Roadlink.query.filter(Roadlink.id == id).one()

	@api.expect(roadlink)
	@api.response(204, 'Roadlink successfully updated.')
	def put(self):
		"""
		Updates a roadlink.
		"""
		data = request.json
		update_roadlink(id, data)
		return None, 204

	@api.response(204, 'Roadlink successfully deleted.')
	def delete(self, id):
		"""
		Deletes roadlink.
		"""
		delete_roadlink(id)
		return None, 204


@ns.route('/archive/<int:year>/')
@ns.route('/archive/<int:year>/<int:month>/')
@ns.route('/archive/<int:year>/<int:month>/<int:day>/')
class RoadlinksArchiveCollection(Resource):

	@api.expect(pagination_arguments, validate=True)
	@api.marshal_with(page_of_roadlinks)
	def get(self, year, month=None, day=None):
		"""
		Returns list of blog posts from a specified time period.
		"""
		args = pagination_arguments.parse_args(request)
		page = args.get('page', 1)
		per_page = args.get('per_page', 10)

		start_month = month if month else 1
		end_month = month if month else 12
		start_day = day if day else 1
		end_day = day + 1 if day else 31
		start_date = '{0:04d}-{1:02d}-{2:02d}'.format(year, start_month, start_day)
		end_date = '{0:04d}-{1:02d}-{2:02d}'.format(year, end_month, end_day)
		posts_query = Post.query.filter(Post.pub_date >= start_date).filter(Post.pub_date <= end_date)

		posts_page = posts_query.paginate(page, per_page, error_out=False)

		return posts_page
'''
