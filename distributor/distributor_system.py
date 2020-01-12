from queue import Queue
import os

from .models import TaskPath, TaskPathBoundingBox

from backend import params 
from backend import settings
class DistributorSystem(object):

	#TO CHANGE WHENEVER CREATING AN INSTANCE OF THIS METHOD
	#CANNOT SCALE, JUST TO MAKE IT WORK
	VALID = params.VALID
	# DATAPATH = 'C:/Users/DELL/Desktop/AnnoKriya-master/backend/distributor/distributor_system_test/'
	# DATAPATH = '/Users/asad/Code/AnnoKriya/backend/distributor/distributor_system_test_img/'
	IMG_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	# IMG_BASE_DIR = 
	DATAPATH = os.path.join(IMG_BASE_DIR, 'distributor_system_test_img')
	
	MAX_QUEUELEN = params.MAX_QUEUELEN
	THRESHOLD_QUEUELEN = params.THRESHOLD_QUEUELEN
	TASK_TYPE = params.TASK_TYPE

	#Constants This won't change
	pathIDSet = []
	Qlist = []
	CURRENT_DATA_COUNT = -1
	TOTAL_DATA_LENGTH = 0
	CURRENT_ITERATION = 0
	CURRENT_POS = 0

	DB_CREATED = False

	def createPathIDSet(self):
		files = list(os.listdir(DistributorSystem.DATAPATH))
		files = [(i+1, files[i]) for i in range(len(files))]
		DistributorSystem.pathIDSet = files
		DistributorSystem.TOTAL_DATA_LENGTH = len(files)
		# print(DistributorSystem.pathIDSet)

	def createQueue(self):
		for i in range(DistributorSystem.VALID):
			DistributorSystem.Qlist.append(Queue(maxsize = DistributorSystem.MAX_QUEUELEN))
		for i in range(DistributorSystem.MAX_QUEUELEN):
			DistributorSystem.Qlist[0].put(DistributorSystem.pathIDSet[i][0])
		DistributorSystem.CURRENT_ITERATION += self.MAX_QUEUELEN

		for i in range(DistributorSystem.VALID-1,0,-1):
			if(DistributorSystem.Qlist[i].empty() !=True):
				DistributorSystem.Qlist[i].get()

	def refillQueue(self, size):
		for i in range(self.CURRENT_DATA_COUNT, self.CURRENT_DATA_COUNT + size):
			if(i<DistributorSystem.TOTAL_DATA_LENGTH):
				DistributorSystem.Qlist[0].put(DistributorSystem.pathIDSet[i][0])
		DistributorSystem.CURRENT_ITERATION += 1

	def checkQueueStatus(self):
		empty_slots = self.MAX_QUEUELEN - self.Qlist[0].size()
		if(empty_slots < self.THRESHOLD_QUEUELEN and CURRENT_DATA_COUNT < TOTAL_DATA_LENGTH):
			self.refillQueue(self.MAX_QUEUELEN)

	def get_next_ID(self, prevID):
		# if(DistributorSystem.Qlist[0].empty()):
		# 	size = min(self.TOTAL_DATA_LENGTH-self.CURRENT_DATA_COUNT, self.MAX_QUEUELEN)
		# 	self.refillQueue(size=self.MAX_QUEUELEN)
		flag=1;
		for i in range(DistributorSystem.VALID-1, -1, -1):
			print(i)
			if(DistributorSystem.Qlist[i].empty() != True and DistributorSystem.Qlist[i].queue[0] > prevID):
				flag=0;
				break
		if(flag):
			#return None
			#print("yes")
			#break
			DistributorSystem.CURRENT_DATA_COUNT+=1
			if(DistributorSystem.CURRENT_DATA_COUNT<DistributorSystem.TOTAL_DATA_LENGTH):
				self.refillQueue(size=self.MAX_QUEUELEN)
				pathID=DistributorSystem.Qlist[0].get()
				DistributorSystem.Qlist[i+1].put(pathID)
				return(pathID)
			return None
		pathID = DistributorSystem.Qlist[i].get()
		if(i!=DistributorSystem.VALID-1):
			if(i==0):
				DistributorSystem.CURRENT_DATA_COUNT+=1
			DistributorSystem.Qlist[i+1].put(pathID)

		return(pathID)

	def printQueue(self):
		for i in range(DistributorSystem.VALID):
			print(DistributorSystem.Qlist[i].queue)

	def populateTaskPathModel(self):
		task = TaskPath.objects.filter(taskgivenID__startswith = self.TASK_TYPE)
		print(len(task))
		if(len(task) != 0):
			print("Dataset exist")
			return 
		for i in range(self.TOTAL_DATA_LENGTH):
			TaskPath.objects.create(taskgivenID = self.TASK_TYPE + str(self.pathIDSet[i][0]).zfill(6),
				taskPath = os.path.join(self.DATAPATH, str(self.pathIDSet[i][1])),)
		DistributorSystem.DB_CREATED = True
		print('Dataset Created')


class DistributorSystemBoundingBox(object):

	#TO CHANGE WHENEVER CREATING AN INSTANCE OF THIS METHOD
	#CANNOT SCALE, JUST TO MAKE IT WORK
	VALID = params.VALID
	# DATAPATH = 'C:/Users/DELL/Desktop/AnnoKriya-master/backend/distributor/distributor_system_test/'
	# DATAPATH = '/Users/asad/Code/AnnoKriya/backend/distributor/distributor_system_test_img/'
	IMG_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	DATAPATH = os.path.join(IMG_BASE_DIR, 'distributor_system_test_img')

	MAX_QUEUELEN = params.MAX_QUEUELEN
	THRESHOLD_QUEUELEN = params.THRESHOLD_QUEUELEN
	TASK_TYPE = params.TASK_TYPE

	#Constants This won't change
	pathIDSet = []
	Qlist = []
	CURRENT_DATA_COUNT = -1
	TOTAL_DATA_LENGTH = 0
	CURRENT_ITERATION = 0
	CURRENT_POS = 0
	START_QUEUE_NUMBER = 1

	DB_CREATED = False

	# def createPathIDSet(self):
	# 	files = list(os.listdir(DistributorSystemBoundingBox.DATAPATH))
	# 	files = [(i+1, files[i]) for i in range(len(files))]
	# 	DistributorSystemBoundingBox.pathIDSet = files
	# 	DistributorSystemBoundingBox.TOTAL_DATA_LENGTH = len(files)
		# print(DistributorSystem.pathIDSet)

	def createQueue(self):
		for i in range(DistributorSystemBoundingBox.VALID):
			DistributorSystemBoundingBox.Qlist.append(Queue(maxsize = DistributorSystemBoundingBox.MAX_QUEUELEN))
		queuesize = min(DistributorSystemBoundingBox.MAX_QUEUELEN, len(DistributorSystemBoundingBox.pathIDSet))
		for i in range(queuesize):
			DistributorSystemBoundingBox.Qlist[0].put(DistributorSystemBoundingBox.pathIDSet[i])
		DistributorSystemBoundingBox.CURRENT_ITERATION += queuesize

		for i in range(DistributorSystemBoundingBox.VALID-1,0,-1):
			if(DistributorSystemBoundingBox.Qlist[i].empty() !=True):
				DistributorSystemBoundingBox.Qlist[i].get()
		print("inside create queue, the queue created is ")
		self.printQueue()
		print("end of create queue function")


	def refillQueue(self, size):
		for i in range(self.CURRENT_DATA_COUNT, self.CURRENT_DATA_COUNT + size):
			if(i<DistributorSystemBoundingBox.TOTAL_DATA_LENGTH):
				DistributorSystemBoundingBox.Qlist[0].put(DistributorSystemBoundingBox.pathIDSet[i])
		DistributorSystemBoundingBox.CURRENT_ITERATION += 1
		print("inside refill queue, the queue created is ")
		self.printQueue()
		print("end of refill queue function")

	def checkQueueStatus(self):
		empty_slots = self.MAX_QUEUELEN - self.Qlist[0].size()
		if(empty_slots < self.THRESHOLD_QUEUELEN and CURRENT_DATA_COUNT < TOTAL_DATA_LENGTH):
			self.refillQueue(self.MAX_QUEUELEN)

	def get_next_ID(self, prevID):
		# if(DistributorSystem.Qlist[0].empty()):
		# 	size = min(self.TOTAL_DATA_LENGTH-self.CURRENT_DATA_COUNT, self.MAX_QUEUELEN)
		# 	self.refillQueue(size=self.MAX_QUEUELEN)
		print("getting next id and the queue is as follows")
		self.printQueue()
		print("inside func get next id")
		flag=1;
		for i in range(DistributorSystemBoundingBox.VALID-1, -1, -1):
			print(i)
			print("is value of i")
			print(prevID)
			print("is value of prevID")
			if(DistributorSystemBoundingBox.Qlist[i].empty()!=True):
				print(DistributorSystemBoundingBox.Qlist[i].queue[0])
				print(" is front of i'th queue")
			if(DistributorSystemBoundingBox.Qlist[i].empty() != True and DistributorSystemBoundingBox.Qlist[i].queue[0] > prevID):
				flag=0;
				break
		if(flag):
			# return None
			print("yes")
			#break
			DistributorSystemBoundingBox.CURRENT_DATA_COUNT+=1
			if(DistributorSystemBoundingBox.CURRENT_DATA_COUNT<DistributorSystemBoundingBox.TOTAL_DATA_LENGTH):
				print("before refilling queue")
				self.refillQueue(size=self.MAX_QUEUELEN)
				print("after refilling queue")
				pathID=DistributorSystemBoundingBox.Qlist[0].get()
				DistributorSystemBoundingBox.Qlist[i+1].put(pathID)
				print("printing pathID")
				print(pathID)
				return(pathID)
			return None
		pathID = DistributorSystemBoundingBox.Qlist[i].get()
		if(i!=DistributorSystemBoundingBox.VALID-1):
			if(i==0):
				DistributorSystemBoundingBox.CURRENT_DATA_COUNT+=1
			DistributorSystemBoundingBox.Qlist[i+1].put(pathID)
		print("returning path id equal to")
		print(pathID)
		print("at end of get next id queue is ")
		self.printQueue()
		print("get next id function ended")
		return(pathID)

	def printQueue(self):
		for i in range(DistributorSystemBoundingBox.VALID):
			print(DistributorSystemBoundingBox.Qlist[i].queue)

	def populateTaskPathBoundingBoxModel(self):
		task = TaskPathBoundingBox.objects.filter(bb_taskgivenID__startswith = self.TASK_TYPE)
		if(len(task) != 0):
			print("Dataset exist")
			print(int(str(list(task)[0])[-6:]))
			for i in list(task):
				DistributorSystemBoundingBox.pathIDSet.append(int(str(i)[-6:]))
			DistributorSystemBoundingBox.pathIDSet.sort()
			print("Printing")
			print(DistributorSystemBoundingBox.pathIDSet)
			DistributorSystemBoundingBox.START_QUEUE_NUMBER = int(str(list(task)[0])[-6:])
			return

		import boto3
		_BUCKET_NAME = 'annokriya-assets'
		_PREFIX = 'pilot_test1/'
		files = []
		client = boto3.client('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
		def ListFiles(client):
			"""List files in specific S3 URL"""
			response = client.list_objects(Bucket=_BUCKET_NAME, Prefix=_PREFIX)
			for content in response.get('Contents', []):
				yield content.get('Key')
		file_list = ListFiles(client)
		for file in file_list:
			image_url = "https://" + settings.AWS_S3_CUSTOM_DOMAIN + "/" + str(file)
			files.append(image_url)

		# files = list(os.listdir(DistributorSystemBoundingBox.DATAPATH))

		files = [(i+1, files[i]) for i in range(len(files))]
		DistributorSystemBoundingBox.pathIDSet = files
		DistributorSystemBoundingBox.TOTAL_DATA_LENGTH = len(files)

		for i in range(self.TOTAL_DATA_LENGTH):
			TaskPathBoundingBox.objects.create(bb_taskgivenID = self.TASK_TYPE + str(self.pathIDSet[i][0]).zfill(6),
				bb_taskPath = str(self.pathIDSet[i][1]),)
		DistributorSystemBoundingBox.DB_CREATED = True
		print('Dataset Created')


if __name__ == '__main__':
	
	obj1 = DistributorSystem()
	obj1.createPathIDSet()
	obj1.createQueue()
	obj1.printQueue()
	obj1.get_next_ID(-1)

	obj2 = DistributorSystem()
	obj2.printQueue()

	obj1.get_next_ID(1)
	obj2.printQueue()

	obj2.get_next_ID(0)
	obj2.printQueue()
