from flask_restplus import reqparse

time_arguments = reqparse.RequestParser()
time_arguments.add_argument('start_time', type=str,  required=True, default='2017-02-28 05:00:00.000', help='Timestamp of beginning of the measurements')
time_arguments.add_argument('end_time', type=str,  required=True, default='2017-02-28 06:00:00.000', help='Timestamp of end of the measurements')
