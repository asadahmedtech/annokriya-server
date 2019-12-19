from queue import Queue
import os

from .models import TaskPath

class DistributorSystem(object):

	#TO CHANGE WHENEVER CREATING AN INSTANCE OF THIS METHOD
	#CANNOT SCALE, JUST TO MAKE IT WORK
	VALID = 2
	# DATAPATH = 'C:/Users/DELL/Desktop/AnnoKriya-master/backend/distributor/distributor_system_test/'
	# DATAPATH = '/Users/asad/Code/AnnoKriya/backend/distributor/distributor_system_test_img/'
	IMG_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	DATAPATH = os.path.join(IMG_BASE_DIR, 'distributor_system_test_img')
	
	MAX_QUEUELEN = 4
	THRESHOLD_QUEUELEN = MAX_QUEUELEN / 2
	TASK_TYPE = 'IMGDROPBOX'

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
