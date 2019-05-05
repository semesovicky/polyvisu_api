import sqlite3
	

ot_mapping={"TrafficIntensity":"profiles_1h"}


class Concept():
	def __init__(self, attributes):
		self._attributes=attributes
		
	def get_attributes(self):
		return self._attributes
	
	def set_attributes(self,attributes):
		self._attributes=attributes
		
class GlobalContext():
	def __init__(self,concepts=[],dbstorages=[],memoryobjects=[],connections_dictionary={}):
		self._concepts=concepts
		self._dbstorages=dbstorages
		self._memoryobjects=memoryobjects
		self._connections_dictionary=connections_dictionary
		
	def add_concept(self,concept):
		self._concepts.append(concept)
		
	def add_dbstorage(self,dbstorage):
		self._dbstorages.append(dbstorage)
		
	def add memoryobject(self,memoryobject):
		self._memoryobjects.append(memoryobject)
		
	def add_connection(self,from,to):
		if from in self._concepts:
			if to in self._dbstorages:
			elif to in 
			self._connections_dictionary.
		else:
			print("Given object is not a concept!")
		
		
		
		
TrafficIntensity=Concept(attributes={"profile_id":"integer","flow":"integer","timestamp":"str"})
Con

	

class DatabaseStorage():
	def __init__ (self, address):
		'''
			inicializace tridy
		'''
		self._address=address
		
	def connect(self):
		conn=sqlite3.connect(self._address)
		return conn
	
	def execute_query(self,query):
		connection=self.connect()
		cursor=connection.cursor()
		cursor.execute(query)
		connection.commit()
		results=cursor.fetchall()
		connection.close()
		return results
	
class Table():
	def __init__ (self, name, fields):
		self._name=name
		self._fields=fields
		
	def get_name(self):
		return self._name
	
	def set_name(self,name):
		self._name=name
	
	def get_fields(self):
		return self._fields
	
	def set_fields(self,fields):
		self._fields=fields
		
	def create_db_table(self,db):
		query=('create table %s(' % self._name +(','.join([str(x[0])+' '+str(x[1]) for x in json.loads(self._fields).items()]))+')')
		self.execute_query(query)


class TrafficIntensity():
	def __init__ (self, table):
		'''
			inicializace tridy
		'''
		for key, val in table.get_fields():
			exec(('self._'+key)+'=val')
		
	def get_timestamp(self):
		return self._time_stamp
	
	def set_timestamp(self,timestamp):
		self._time_stamp=timestamp
	
	def get_profileid(self):
		return self._profile_id
	
	def set_profileid(self,profileid):
		self._profile_id=profileid
	
	def get_flow(self):
		return self._flow
	
	def set_flow(self,flow):
		self._flow=flow
		
	def get_occupancy(self):
		return self._occupancy
	
	def set_occupancy(self,occupancy):
		self._occupancy=occupancy
	
	def get_obscount(self):
		return self._obs_count
	
	def set_obscount(self,obscount):
		self._obs_count=obscount
	
	def get_intercount(self):
		return self._inter_count
	
	def set_intercount(self,intercount):
		self._inter_count=intercount
	
	def get_inserted(self):
		return self._inserted
	
	def set_inserted(self,inserted):
		self._inserted=inserted
	
	def get_src(self):
		return self._src
	
	def set_src(self,src):
		self._src=src
	
	def get_id(self):
		return self._id
	
	def set_id(self,id):
		self._id=id
		
	def save_to_db(self,db,table):
		query="INSERT INTO %s VALUES ('%s',%s,%s,%s,%s,%s,'%s','%s')" % (table, self._time_stamp, self._profile_id, self._flow, self._occupancy, self._obs_count, self._inter_count, self._inserted, self._src)
		db.execute_query(query)
		return('Object inserted into db!')
	
d=Database('polyvisu.sqlite') 	
ti=d.execute_query('select * from profiles_1h')
tio=TrafficIntensity(*ti[0])
tio.set_flow(10001)
tio.save_to_db(d,'profiles_1h')
d.execute_query('select * from profiles_1h where flow>10000')
d.execute_query('delete from profiles_1h where flow>10000')

datetime.datetime.strptime(tio.get_inserted()[:19],'%Y-%m-%d %H:%M:%S')

datetime.datetime.strftime(datetime.datetime.strptime(tio.get_inserted()[:19],'%Y-%m-%d %H:%M:%S')+datetime.timedelta(hours=1),'%Y-%m-%d %H:%M:%S')
	
		
import sqlite3
import csv
conn = sqlite3.connect('statistics.db')
c = conn.cursor()
c.execute('SELECT * FROM rh')
with open('output3.csv','w') as out_csv_file:
  csv_out = csv.writer(out_csv_file)
  csv_out.writerow([d[0] for d in c.description])
  for result in c:
   csv_out.writerow(result)



class Roadlink():
	def __init__ (self, id, kind, name, capacity, geometry):
		'''
			inicializace tridy
		'''
		self._id = id
		self._kind = kind
		self._name = name
		self._capacity=capacity
		self._geometry=geometry
		
	def save_to_db(self,db,table):
		cursor=connection.cursor()
		query=('insert into %s (index_type,name,field_id,date,statistics,value_matrix_of_pixels) VALUES (\'%s\',\'%s\',%s,\'%s\'::timestamp, (\'%s\'::json), ST_SetValues(ST_AddBand(ST_MakeEmptyRaster(%s, %s, %s, %s, 1, 1, 0, 0, 4326),\'32BF\'::text, 2, %s), 1, 1, 1,ARRAY%s::double precision[][]));' %(table,self._index_type,self._name,self._field_id,self._time,self.get_statistics(),self._value_matrix_of_pixels.get_data().shape[1],self._value_matrix_of_pixels.get_data().shape[0],self._value_matrix_of_pixels.get_metadata()['affine_transformation'][0],self._value_matrix_of_pixels.get_metadata()['affine_transformation'][3],self._value_matrix_of_pixels.get_metadata()['nodata'],(np.array2string(self._value_matrix_of_pixels.get_data().filled(self._value_matrix_of_pixels.get_metadata()['nodata']), separator=',',formatter={'float_kind':lambda x: "%.4f" % x},prefix='[',suffix=']').replace('\n', ''))) )
		cursor.execute(query)
		connection.commit()
		cursor.close()
		return('Object inserted into db!')

class TrafficIntensity():