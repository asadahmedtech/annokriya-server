from distributor.models import TaskPath , TaskProcessedData
from .models import OutputTable
from dashboard.models import Dashboard
# from sklearn.cluster import DBSCAN
# from sklearn.preprocessing import StandardScaler
# from sklearn.preprocessing import normalize
# from sklearn.decomposition import PCA

class MergerSystem(object):

    THRESHOLD_VALUE=2
    def add_to_db(self):
        out=OutputTable.objects.all()
        print(str(out))
        e=TaskPath.objects.filter(taskCount=5)
        #e=TaskPath.objects.all()

        print(e)
        for entry in e:
            a=entry.taskgivenID
            print('in for')
            print(entry.taskgivenID)
            u=TaskProcessedData.objects.filter(taskpath=a)
            #u=TaskProcessedData.objects.all()
            print(u)
            # x=[0.0,0.0,0.0,0.0,0.0]
            # y=[0.0,0.0,0.0,0.0,0.0]
            x=[0,0,0,0,0]
            y=[0,0,0,0,0]
            for user_data in u:
                # print(user_data.x1)
                # print(user_data.x2)
                # print(user_data.x3)
                # print(user_data.x4)
                # print(user_data.x5)
                # print(user_data.y1)
                # print(user_data.y2)
                # print(user_data.y3)
                # print(user_data.y4)
                # print(user_data.y5)
                x[0]=x[0]+(int(user_data.x1))
                x[1]=x[1]+(int(user_data.x2))
                x[2]=x[2]+(int(user_data.x3))
                x[3]=x[3]+(int(user_data.x4))
                x[4]=x[4]+(int(user_data.x5))
                y[0]=y[0]+(int(user_data.y1))
                y[1]=y[1]+(int(user_data.y2))
                y[2]=y[2]+(int(user_data.y3))
                y[3]=y[3]+(int(user_data.y4))
                y[4]=y[4]+(int(user_data.y5))

            for i in range(0,5,1):
                x[i]=x[i]/5
                y[i]=y[i]/5
            for users in u:
                flag=0
                for i in range(0,5,1):
                    if ((x[i]-(int(users.x1)))>MergerSystem.THRESHOLD_VALUE or \
                    (x[i]-(int(users.x2)))>MergerSystem.THRESHOLD_VALUE or \
                    (x[i]-(int(users.x3)))>MergerSystem.THRESHOLD_VALUE or \
                    (x[i]-(int(users.x4)))>MergerSystem.THRESHOLD_VALUE or \
                    (x[i]-(int(users.x5)))>MergerSystem.THRESHOLD_VALUE or \
                    (y[i]-(int(users.y1)))>MergerSystem.THRESHOLD_VALUE or \
                    (y[i]-(int(users.y2)))>MergerSystem.THRESHOLD_VALUE or \
                    (y[i]-(int(users.y3)))>MergerSystem.THRESHOLD_VALUE or \
                    (y[i]-(int(users.y4)))>MergerSystem.THRESHOLD_VALUE or \
                    (y[i]-(int(users.y5)))>MergerSystem.THRESHOLD_VALUE ) :
                            flag=1
                            break;
                if(flag==1):
                    print('in flag=1')
                    d=Dashboard.objects.filter(user=user_data.user)
                    for db in d:
                        db.pending=db.pending-1
                        db.wrong=db.wrong+1
                        db.save()
                    break
                else :
                    print('in flag -1')
                    d=Dashboard.objects.filter(user=user_data.user)
                    for db in d:
                        db.pending=db.pending-1
                        db.correct=db.correct+1
                        db.credits=str((db.credits) + 1 )
                        db.save()
                    break

            output=OutputTable(ox1=(str(x[0])),ox2=(str(x[1])),ox3=(str(x[2])),ox4=(str(x[3])),ox5=(str(x[4])),oy1=(str(y[0])),oy2=(str(y[1])),oy3=(str(y[2])),oy4=(str(y[3])),oy5=(str(y[4])),otaskid=entry.taskgivenID, otaskpath=entry.taskPath)
            output.save()
            print("output is "+str(output))
            print(output.otaskpath)
            TaskPath.objects.filter(taskgivenID=entry.taskgivenID).delete()
            return str(output)
