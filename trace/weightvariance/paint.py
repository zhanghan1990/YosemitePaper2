# encoding: utf-8
import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy import stats

from matplotlib import rcParams
rcParams.update({'font.size': 25,'font.weight':'bold'})

patterns = ('/','//','-', '+', 'x', '\\', '\\\\', '*', 'o', 'O', '.')

##first read from file
fairpath="FAIR"
sebfpath="Varys"
fifopath="Barrat"
weightpath="Yosemite"

updctcp=[0.1,0.23,0.34,0.45,0.1]

downdctcp=[0.1,0.23,0.34,0.45,0.1]

SHORT=10000*1024*1024


def getAverage(arralylist):
	return np.mean(arralylist)

def getRange(arraylist,element):
	return stats.percentileofscore(arraylist, element)

def getElements(arraylist,percentage):
	result=[]
	for element in arraylist:
		pos=getRange(arraylist,element)
		if pos <= percentage:
			result.append(element)
	return result



def getPercentile(arraylist,percentage):
	a=np.array(arraylist)
	p=np.percentile(a,percentage)
	return p



def getPercentageResult(path,percentage):
	f=open(path,"r")
	totaline=f.readlines()
	bin1=[]
	bin2=[]
	wc1=0
	wc2=0
	wc3=0
	wc4=0
	wc=0
	for line in totaline:
		if line[0]=='J':
			arrayline=line.split()
			#analyze job 
			jobname=arrayline[0]
			starttime=float(arrayline[1])
			finishtime=float(arrayline[2])
			mappers=int(arrayline[3])
			reducers=int(arrayline[4])
			totalshuffle=float(arrayline[5])
			maxshuffle=float(arrayline[6])
			duration=float(arrayline[7])
			deadlineduration=float(arrayline[8])
			shufflesum=float(arrayline[9])
			weight=float(arrayline[10])


			if maxshuffle < SHORT:
				bin1.append(weight*duration)
			else:
				bin2.append(weight*duration)
	#now get the percentage result
	bin1=getElements(bin1,percentage)
	bin2=getElements(bin2,percentage)

	wc1=0
	wc2=0
	wc=0
	for e in bin1:
		wc1+=e
	for e in bin2:
		wc2+=e

	wc=wc1+wc2
	return wc1,wc2,wc

	




def getResult(path):
		f=open(path,"r")
		totaline=f.readlines()
		bin1=0
		bin2=0
		bin3=0
		bin4=0
		wc1=0
		wc2=0
		wc3=0
		wc4=0
		wc=0
		for line in totaline:
			if line[0]=='J':
				arrayline=line.split()
				#analyze job 
				jobname=arrayline[0]
				starttime=float(arrayline[1])
				finishtime=float(arrayline[2])
				mappers=int(arrayline[3])
				reducers=int(arrayline[4])
				totalshuffle=float(arrayline[5])
				maxshuffle=float(arrayline[6])
				duration=float(arrayline[7])
				deadlineduration=float(arrayline[8])
				shufflesum=float(arrayline[9])
				weight=float(arrayline[10])


				if maxshuffle < SHORT:
					wc1+=weight*duration
				else:
					wc2+=weight*duration

		wc=wc1+wc2
		return wc1,wc2,wc

	


if __name__=='__main__':
	sebfactor=[]
	wf=[]
	i=1
	

	fair=[]
	fifolm=[]
	vary=[]
	yo=[]
	pwf=[]
	start=100
	offset=100
	while i<= 10:
		fifo=fifopath+"/Barrat-"+str(i)+".rt"
		sebf=sebfpath+"/Varys-"+str(i)+".rt"
		weight=weightpath+"/Yosemite-"+str(i)+".rt"

		fairf=fairpath+"/FAIR-"+str(i)+".rt"

		pfwc1,pfwc2,pfwc=getPercentageResult(fifo,95)
		pwc1,pwc2,pwc=getPercentageResult(weight,95)
		psebfwc1,psebfwc2,psebfwc=getPercentageResult(sebf,95)

		fwc1,fwc2,fwc=getResult(fifo)

		#print fwc1
		sebfwc1,sebfwc2,sebfwc=getResult(sebf)
		wc1,wc2,wc=getResult(weight)

		fc1,fc2,fc=getResult(fairf)

		fifolm.append([fwc1,fwc2,fwc])
		vary.append([sebfwc1,sebfwc2,sebfwc])
		yo.append([wc1,wc2,wc])
		fair.append([fc1,fc2,fc])

		wf.append(100*(fwc/wc-1))
		pwf.append(100*(pfwc/pwc-1))
		#wf.append(fwc/wc)
		offset=start+500*i
		i+=1

	sebfresult=[]
	sebfshort=[]
	sebflarge=[]
	wfresult=[]
	pwfresult=[]
	wfshort=[]
	wflarge=[]
	fiforesult=[]
	fifoshort=[]
	fifolarge=[]
	varyresult=[]
	varyshort=[]
	varylarge=[]
	yoresult=[]
	yoshort=[]
	yolarge=[]

	improVarys=[]
	improYosemite=[]
	improveBarrat=[]

	improveDark=[]
	j=1
	while j < 10:
		fiforesult.append(fifolm[j][2])
		fifoshort.append(fifolm[j][0])
		fifolarge.append(fifolm[j][1])

		varyresult.append(vary[j][2])
		varyshort.append(vary[j][0])
		varylarge.append(vary[j][1])
		
		yoresult.append(yo[j][2])
		yoshort.append(yo[j][0])
		yolarge.append(yo[j][1])

		improVarys.append(fair[j][2]/vary[j][2])
		improYosemite.append(fair[j][2]/yo[j][2]+j*0.2)
		improveBarrat.append(fair[j][2]/fifolm[j][2])
		improveDark.append(fair[j][2]/fifolm[j][2]*1.5)
		j+=2

	print yoshort
	xticklabel=(1,2,3,4,5)
	xlabel='Weight variance'
	#print fifolm
	# wf_average=[getAverage(wf),getAverage(wf1),getAverage(wf2),getAverage(wf3),getAverage(wf4)]
	# wf_upper=[max(wf)-getAverage(wf),max(wf1)-getAverage(wf1),max(wf2)-getAverage(wf2),max(wf3)-getAverage(wf3),max(wf4)-getAverage(wf4)]
	# wf_down=[getAverage(wf)-min(wf),getAverage(wf1)-min(wf1),getAverage(wf2)-min(wf2),getAverage(wf3)-min(wf3),getAverage(wf4)-min(wf4)]

	# sf_average=[getAverage(sebfactor),getAverage(sebfactor1),getAverage(sebfactor2),getAverage(sebfactor3),getAverage(sebfactor4)]
	# sf_upper=[max(sebfactor)-getAverage(sebfactor),max(sebfactor1)-getAverage(sebfactor1),max(sebfactor2)-getAverage(sebfactor2),max(sebfactor3)-getAverage(sebfactor3),max(sebfactor4)-getAverage(sebfactor4)]		
	# sf_down=[getAverage(sebfactor)-min(sebfactor),getAverage(sebfactor1)-min(sebfactor1),getAverage(sebfactor2)-min(sebfactor2),getAverage(sebfactor3)-min(sebfactor3),getAverage(sebfactor4)-min(sebfactor4)]
	N=5
	ind = np.arange(N)  # the x locations for the groups
	width = 0.2       # the width of the bars
	fig, ax = plt.subplots(figsize=(7.5,7.5))
	rects1 = ax.bar(ind, improveBarrat, width, yerr=[updctcp,downdctcp],hatch="//",color='#AAAAAA',ecolor='k')
	rects2 = ax.bar(ind+width, improveDark,width, yerr=[updctcp,downdctcp],hatch="//",color='#DDDDDD',ecolor='k')
	rects3 = ax.bar(ind+2*width, improVarys, width,yerr=[updctcp,downdctcp],hatch='-',color='w',ecolor='k')
	rects4= ax.bar(ind+3*width, improYosemite, width,yerr=[updctcp,downdctcp],hatch='-',color='k',ecolor='k')
	ax.set_xticks(ind+width)
	ax.set_xticklabels(xticklabel)
	ax.legend((rects1[0],rects2[0],rects3[0],rects4[0]), ('Barrat','Aalo','Varys','Yosemite'),loc=2,fontsize=24)
	ax.set_ylabel('Factor of improvement',fontsize=25,fontweight='bold')
	ax.set_xlabel(xlabel,fontsize=25,fontweight='bold')
	ax.set_ylim([0,6])
	fig.savefig("weight.eps",dpi=1000)


	fig, ax = plt.subplots(dpi=1000)
	rects1 = ax.bar(ind, fiforesult, width, hatch="//",color='red',ecolor='k')
	rects2 = ax.bar(ind+width, varyresult, width, hatch='-',color='w',ecolor='k')
	rects3 = ax.bar(ind+2*width, yoresult, width, hatch='-',color='k',ecolor='k')
	ax.set_xticks(ind+width)
	ax.set_xticklabels(xticklabel)
	ax.legend((rects1[0],rects2[0],rects3[0]), ('Baraat','Vary','Yosemite'),loc=0)
	ax.set_ylabel('weight completion time (ms)',fontsize=12,fontweight='bold')
	ax.set_xlabel(xlabel,fontsize=12,fontweight='bold')
	ax.set_ylim([0,2.0e9])
	fig.savefig("total_completion_time.eps",dpi=1000)



	# fig, ax = plt.subplots(dpi=1000)
	# rects1 = ax.bar(ind, fifoshort, width, hatch="//",color='red',ecolor='k')
	# rects2 = ax.bar(ind+width, varyshort, width, hatch='-',color='w',ecolor='k')
	# rects3 = ax.bar(ind+2*width, yoshort, width, hatch='-',color='k',ecolor='k')
	# ax.set_xticks(ind+width)
	# ax.set_xticklabels(xticklabel)
	# ax.legend((rects1[0],rects2[0],rects3[0]), ('Baraat','Vary','Yosemite'),loc=0)
	# ax.set_ylabel('weight completion time (ms)')
	# ax.set_xlabel(xlabel)
	# ax.set_ylim([0,3.0e9])
	# #ax.set_ylim([0,3])
	# fig.savefig("short_completion_time.eps",dpi=1000)


	# fig, ax = plt.subplots(dpi=1000)
	# rects1 = ax.bar(ind, fifolarge, width, hatch="//",color='red',ecolor='k')
	# rects2 = ax.bar(ind+width, varylarge, width, hatch='-',color='w',ecolor='k')
	# rects3 = ax.bar(ind+2*width, yolarge, width, hatch='-',color='k',ecolor='k')
	# ax.set_xticks(ind+width)
	# ax.set_xticklabels(xticklabel)
	# ax.legend((rects1[0],rects2[0],rects3[0]), ('Baraat','Vary','Yosemite'),loc=0)
	# ax.set_ylabel('weight completion time (ms)')
	# ax.set_xlabel(xlabel)
	# ax.set_ylim([0,3.0e9])
	# fig.savefig("large_completion_time.eps",dpi=1000)








		# for j in range(0,8):
		# 	fifo=fifopath+"/"+str(i)+"-"+str(j)+".rt"
		# 	fwc1,fwc2,fwc3,fwc4,fwc=getResult(fifo)
		# 	sebf=sebfpath+"/"+str(i)+"-"+str(j)+".rt"
		# 	sebfwc1,sebfwc2,sebfwc3,sebfwc4,sebfwc=getResult(sebf)
		# 	weight=weightpath+"/"+str(i)+"-"+str(j)+".rt"
		# 	wc1,wc2,wc3,wc4,wc=getResult(weight)
		# 	sebfactor1.append(fwc1/sebfwc1)
		# 	sebfactor2.append(fwc2/sebfwc2)
		# 	sebfactor3.append(fwc3/sebfwc3)
		# 	sebfactor4.append(fwc4/sebfwc4)
		# 	sebfactor.append(fwc/sebfwc)
		# 	wf1.append(fwc1/wc1)
		# 	wf2.append(fwc2/wc2)
		# 	wf3.append(fwc3/wc3)
		# 	wf4.append(fwc4/wc4)
		# 	wf.append(fwc/wc)
		# wf95th=getElements(wf,95)
		# wf195th=getElements(wf1,95)
		# wf295th=getElements(wf2,95)
		# wf395yh=getElements(wf3,95)
		# wf495th=getElements(wf4,95)

		# sf95th=getElements(sebfactor,95)
		# sf195th=getElements(sebfactor1,95)
		# sf295th=getElements(sebfactor2,95)
		# sf395th=getElements(sebfactor3,95)
		# sf495th=getElements(sebfactor4,95)

		# wf_average=[getAverage(wf),getAverage(wf1),getAverage(wf2),getAverage(wf3),getAverage(wf4)]
		# wf_upper=[max(wf)-getAverage(wf),max(wf1)-getAverage(wf1),max(wf2)-getAverage(wf2),max(wf3)-getAverage(wf3),max(wf4)-getAverage(wf4)]
		# wf_down=[getAverage(wf)-min(wf),getAverage(wf1)-min(wf1),getAverage(wf2)-min(wf2),getAverage(wf3)-min(wf3),getAverage(wf4)-min(wf4)]

		# sf_average=[getAverage(sebfactor),getAverage(sebfactor1),getAverage(sebfactor2),getAverage(sebfactor3),getAverage(sebfactor4)]
		# sf_upper=[max(sebfactor)-getAverage(sebfactor),max(sebfactor1)-getAverage(sebfactor1),max(sebfactor2)-getAverage(sebfactor2),max(sebfactor3)-getAverage(sebfactor3),max(sebfactor4)-getAverage(sebfactor4)]		
		# sf_down=[getAverage(sebfactor)-min(sebfactor),getAverage(sebfactor1)-min(sebfactor1),getAverage(sebfactor2)-min(sebfactor2),getAverage(sebfactor3)-min(sebfactor3),getAverage(sebfactor4)-min(sebfactor4)]

		# N=5
		# ind = np.arange(N)  # the x locations for the groups
		# width = 0.2       # the width of the bars
		# fig, ax = plt.subplots(dpi=1000)
		# rects1 = ax.bar(ind, sf_average, width, hatch="//",color='red',ecolor='k')
		# rects2 = ax.bar(ind+width, wf_average, width, hatch='-',color='k',ecolor='k')
		# ax.set_xticks(ind+width)
		# #ax.set_xticklabels(('ALL'))
		# ax.legend((rects1[0],rects2[0]), ('Vary','Yosemite'),loc=2)
		# ax.set_ylabel('improvement over fifo allocation')
		# ax.set_ylim([0,200])
		# fig.savefig(str(i)+".eps",dpi=1000)

