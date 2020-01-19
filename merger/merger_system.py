from distributor.models import TaskPath , TaskProcessedData, TaskPathBoundingBox, TaskProcessedDataBoundingBox
from .models import OutputTable, BoundingBoxObject, BoundingBoxObjectnew, BoundingBoxObjectallnew
from dashboard.models import Dashboard
from backend import params
# from sklearn.cluster import DBSCAN
# from sklearn.preprocessing import StandardScaler
# from sklearn.preprocessing import normalize
# from sklearn.decomposition import PCA

class MergerSystem(object):

    THRESHOLD_VALUE= params.THRESHOLD_VALUE
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
            # TaskPath.objects.filter(taskgivenID=entry.taskgivenID).delete()
            return str(output)



class MergerSystemBoundingBox(object):
    # THRESHOLD_VALUE=100
    CORRECT_THRESHOLD=params.CORRECT_THRESHOLD
    VALID = params.VALID
    OVERLAP_PERCENT = params.OVERLAP_PERCENT
    MIN_CLUSTER_LEN = params.MIN_CLUSTER_LEN
    def add_to_db_bounding_box(self):
        # bb_out=BoundingBox.objects.all()
        # print(str(bb_out))
        # print('inside merger system bounding box')
        bb_e=TaskPathBoundingBox.objects.filter(bb_taskCount=MergerSystemBoundingBox.VALID)
        #e=TaskPath.objects.all()

        print(bb_e)
        # print(" printing bb_e")
        for entry in bb_e:
            a=entry.bb_taskgivenID
            # print('in for')
            # print(entry.bb_taskgivenID)
            u=TaskProcessedDataBoundingBox.objects.filter(bb_taskpath=a)
            #u=TaskProcessedData.objects.all()
            # print(u)
            # x=[0.0,0.0,0.0,0.0,0.0]
            # y=[0.0,0.0,0.0,0.0,0.0]
            Tu={}
            user_val=""
            j=0
            user_count={}
            userlist=[]
            for user_d in u:
                cnt=TaskProcessedDataBoundingBox.objects.filter(bb_taskpath=a,user=user_d.user)
                u_1 = []
                # print(user_d)
                # print("hi\n")
                # print(cnt)
                if user_d.user in userlist:
                    print("already exists")
                else:
                    userlist.append(user_d.user)
                    for user_data in cnt:
                        user_count[user_data.user]=0
                        u_2=[]
                        x1 =[]
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
                        x1.append(int((user_data.x.split('.')[0].strip())))
                        x1.append(int((user_data.y.split('.')[0].strip())))
                        x1.append(int((user_data.l.split('.')[0].strip())))
                        x1.append(int((user_data.h.split('.')[0].strip())))
                        x1.append(user_data.user)
                        u_2.append(x1)
                        u_1.append(u_2)
                        out1 = BoundingBoxObjectallnew(x=str(x1[0]),y=str(x1[1]),l=str(x1[2]),h=str(x1[3]),taskid=entry.bb_taskgivenID, taskurl = entry.bb_taskPath, user=user_data.user )
                        out1.save()
                    # u_2[0].append(user_d.user)
                Tu[j]=u_1
                j=j+1
            print(Tu)
            # print("\n\nyayaya\n\n")
            # print(Tu[0])
            # return HttpResponse('hello')
            # print("\n\nnonononon\n\n")
            cluster={}
            cluster[0]=Tu[0]
            # cluster[0][0].append("hi")
            # print(cluster[0])
            # print("\n\nyes\n\n")
            # print(cluster[0][0])
            # print(cluster[0][0][0])
            # print(cluster[0][0][0][0])
            # print(len(cluster[0]))
            # print("\n\nyoo\n\n")
            # print(Tu[0][0][0][len(Tu[0][0][0])-1])
            # print(len(cluster[0]))
            # print("\n\n\n\n")
            user_count[Tu[0][0][0][len(Tu[0][0][0])-1]]=len(cluster[0])
            # print("user count is \n")
            # print(user_count)
            for i in range(1,j,1):

                flag1=0
                # print(len(Tu[i]))
                for k in range(0,len(Tu[i]),1):
                    # print("\n\ncurrent tuple\n\n")
                    # print(k)
                    # print(Tu[i][k][0])
                    # print(Tu[i][1])
                    # print(len(cluster[0]))
                    # print(len(cluster[0]))
                    for l in range(0,len(cluster[0]),1):
                        # print("\ncomapring with\n")
                        # print(Tu[0][l])
                        area=0
                        if((int(Tu[0][l][0][0]))<=(int(Tu[i][k][0][0]))):
                            if((Tu[0][l][0][1]<=Tu[i][k][0][1])):
                                if(((Tu[0][l][0][0]+Tu[0][l][0][2]-Tu[i][k][0][0])<0) or ((Tu[0][l][0][1]+Tu[0][l][0][3]-Tu[i][k][0][1])<0)):
                                    area=0
                                else:
                                    area=(Tu[0][l][0][0]+Tu[0][l][0][2]-Tu[i][k][0][0])*(Tu[0][l][0][1]+Tu[0][l][0][3]-Tu[i][k][0][1])
                            else:
                                if((Tu[i][k][0][3]+Tu[i][k][0][1]-Tu[0][l][0][1])<0):
                                    area=0
                                else:
                                    area=(Tu[0][l][0][0]+Tu[0][l][0][2]-Tu[i][k][0][0])*(Tu[i][k][0][3]+Tu[i][k][0][1]-Tu[0][l][0][1])
                        else:
                            if(Tu[0][l][0][1]<=Tu[i][k][0][1]):
                                if(((Tu[i][k][0][2]+Tu[i][k][0][0]-Tu[0][l][0][1])<0) or ((Tu[i][k][0][2]+Tu[i][k][0][1]-Tu[0][l][0][1])<0)):
                                    area=0
                                else:
                                    area=(Tu[i][k][0][2]+Tu[i][k][0][0]-Tu[0][l][0][1])*(Tu[i][k][0][2]+Tu[i][k][0][1]-Tu[0][l][0][1])
                            else:
                                if((Tu[0][l][0][1]+Tu[0][l][0][3]-Tu[i][k][0][1])<0):
                                    area=0
                                else:
                                    area=(Tu[i][k][0][2]+Tu[i][k][0][0]-Tu[0][l][0][0])*(Tu[0][l][0][1]+Tu[0][l][0][3]-Tu[i][k][0][1])

                        if (area>(MergerSystemBoundingBox.OVERLAP_PERCENT*Tu[0][l][0][3]*Tu[0][l][0][2])):

                            cluster[0][l].append(Tu[i][k][0])
                            user_count[Tu[i][k][0][len(Tu[i][k][0])-1]]=user_count[Tu[i][k][0][len(Tu[i][k][0])-1]]+1
                            # print("user counting printing \n")
                            # print(user_count)
                            # print(Tu[i][len(Tu[i])-1][0])
                            # print("appending")
                            # print(Tu[i][k][0])
                            # print("to")
                            # print(cluster[0][l])
                            # print("\n\n\n")
                            # cluster[0][l][len(cluster[0][l])-1].append(Tu[i][len(Tu[i])-1][0])

                            # print(cluster[0][l])
                            # print("\n\nprinted\n\n")
                            # cluster[0][l].append(Tu[i][len(Tu[i]-1)][0])
                            flag1=1
                            break

                    if(flag1==0):
                        # print("\n\n\nnot matched with any\n\n\n")
                        u3=[[]]
                        u3[0]=(Tu[i][k][0])
                        cluster[0].append(u3)
                        user_count[Tu[i][k][0][len(Tu[i][k][0])-1]]+=1
                        # print("new user count\n")
                        # print(user_count)
                        # cluster[0][len(cluster[0])-1].append(Tu[i][len(Tu[i])-1])
                    else:
                        flag1=0
            # print(cluster)
            # print("done")
            maxi=0
            ox=0
            oy=0
            ol=0
            ow=0

            # print(cluster[0])
            # print(user_count)

            for i in range(0,len(cluster[0]),1):
                if(len(cluster[0][i])<=MergerSystemBoundingBox.MIN_CLUSTER_LEN):
                    user_count[cluster[0][i][0][len(cluster[0][i][0])-1]]=user_count[cluster[0][i][0][len(cluster[0][i][0])-1]]-1
                    # print("updates user count\n")
                    # print(user_count)
                    # print("\n\n\nremoving cluster\n\n\n")
                    # print(cluster[0][i])
                    cluster[0][i].clear()
                else:
                    #maxi+=1        #CHANGED HERE
                    # print("\n\nadding these clustering to get a point\n\n")
                    for j in range(0,len(cluster[0][i]),1):
                        # print(cluster[0][i][j])
                        # print(cluster[0][i])
                        # print("printed\n")
                        ox+=(int(cluster[0][i][j][0]))
                        oy+=(int(cluster[0][i][j][1]))
                        ol+=(int(cluster[0][i][j][2]))
                        ow+=(int(cluster[0][i][j][3]))
                        
                    ox=ox/len(cluster[0][i])
                    oy=oy/len(cluster[0][i])
                    ol=ol/len(cluster[0][i])
                    ow=ow/len(cluster[0][i])
                    out=BoundingBoxObjectnew(x=str(ox),y=str(oy),l=str(ol),h=str(ow),taskid=entry.bb_taskgivenID, taskurl = entry.bb_taskPath)
                    out.save()
                    # TaskPathBoundingBox.objects.filter(bb_taskgivenID=entry.bb_taskgivenID).delete()
                    ox=0
                    oy=0
                    ol=0
                    ow=0
            maxi=len(cluster[0])        #CHANGED HERE
            # print("\n\nno\n\n")
            # print(maxi)
            # print("\n\nyes\n\n")
            # print(cluster[0])
            # print(user_count)

            key=list(user_count.keys())
            print(user_count)
            print(key)
            for i in range(0,len(key),1):       #CHANGED HERE
                if((user_count[key[i]]/maxi) >=self.CORRECT_THRESHOLD ):
                    d=Dashboard.objects.filter(user=key[i])
                    for db in d:
                        db.pending=db.pending-1
                        db.correct=db.correct+1
                        db.credits=str((db.credits) + 1 )
                        db.save()
                        break
                else:
                    d=Dashboard.objects.filter(user=key[i])
                    for db in d:
                        db.pending=db.pending-1
                        db.wrong=db.wrong+1
                        db.save()
                        break

            # counts={}
            # for i in range(0,len(cluster[0]-2)):

