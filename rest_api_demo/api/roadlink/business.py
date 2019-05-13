from rest_api_demo.database.models import Roadlink,  loadSession
from sqlalchemy import func
import json

def get_traffic_intensities(start_time, end_time):
    session=loadSession()
    q=session.query(Roadlink.profile_id,func.sum(Roadlink.flow)).group_by(Roadlink.profile_id).filter(Roadlink.time_stamp>=start_time, Roadlink.time_stamp<=end_time)
    roadlinks=[]
    for row in q:
        roadlinks.append(row)
    h=[]
    [h.append({'id':i[0],'traffic_intensity':i[1]}) for i in roadlinks]
    d={'start_time':start_time,'end_time':end_time,'items':h}
    session.close()
    return d

'''def create_roadlink(data):
	id = data.get('id')
	name = data.get('name')
	traffic_intensity = data.get('traffic_intensity')
	pub_date = datetime.datetime.strptime(data.get('pub_date'),'%Y-%m-%d %H:%M:%S')
	roadlink = Roadlink(id, name, traffic_intensity, pub_date)
	db.session.add(roadlink)
	db.session.commit()


def update_roadlink(data):
	id = data.get('id')
	pub_date = data.get('pub_date')
	roadlink = Roadlink.query.filter(Roadlink.id == id & Roadlink.pub_date == pub_date).one()
	roadlink.traffic_intensity = data.get('traffic_intensity')
	db.session.add(roadlink)
	db.session.commit()


def delete_roadlink(roadlink_id):
	roadlink = Roadlink.query.filter(Roadlink.id == roadlink_id).one()
	db.session.delete(roadlink)
	db.session.commit()'''
