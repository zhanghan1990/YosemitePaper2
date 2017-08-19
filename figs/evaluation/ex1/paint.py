# encoding: utf-8
import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy import stats

from matplotlib import rcParams
rcParams.update({'font.size': 10,'font.weight':'bold'})

patterns = ('/','//','-', '+', 'x', '\\', '\\\\', '*', 'o', 'O', '.')

##first read from file
pFabric="pFabric"
Varys="Varys"
Barrat="Barrat"
Yosemite="Yosemite"
Fair="FAIR"

DARK='DARK'



if __name__=='__main__':


	rcParams.update({'font.size': 16,'font.weight':'bold'})
	N=5
	ind = np.arange(N)  # the x locations for the groups
	width = 0.3       # the width of the bars
	#plt.xticks(fontsize=18,fontweight='bold',rotation=30,ha='center')
	fig, ax = plt.subplots()

	VarysResult=[3,25,14,55,33]
	YosemiteResult=[2,22,12,50,25]
	wfresult=[5,30,20,70,40]


	rects3 = ax.bar(ind+2*width, wfresult, width,hatch="-",color='white',ecolor='k')
	rects1 = ax.bar(ind, YosemiteResult, width,hatch="/",color='#AAAAAA',ecolor='k')
	rects2 = ax.bar(ind+width, VarysResult, width,hatch="+",color='#DDDDDD',ecolor='k')

	ax.set_xticks(ind+width)
	plt.setp(ax.xaxis.get_majorticklabels())
	ax.set_xticklabels(('S-N','L-N','S-W','L-W','ALL'),fontsize=12,fontweight='bold')
	ax.set_yticklabels((0,20,40,60,80,100),fontsize=16,fontweight='bold')
	ax.legend((rects1[0],rects2[0],rects3[0]), ('Yosemite','Varys','TCP'),loc=0,fontsize=15)
	ax.set_ylabel('Average WCCT(Normalized)',fontsize=16,fontweight='bold')
	ax.set_ylim([0,100])
	ax.set_xlabel('Coflow Types',fontsize=12,fontweight='bold')
	fig.savefig("evaluation_motivation1.eps")

	VarysResult=[5,11,16,13,1.3,6,18,7,45,33]
	YosemiteResult=[3,7,11,12,1.5,9,15,12,50,45]
	wfresult=[4,8,20,18,1.7,8,22,13,70,65]


	rcParams.update({'font.size': 16,'font.weight':'bold'})
	N=10
	ind = np.arange(N)  # the x locations for the groups
	width = 0.3       # the width of the bars
	#plt.xticks(fontsize=18,fontweight='bold',rotation=30,ha='center')
	fig, ax = plt.subplots()

	rects3 = ax.bar(ind+2*width, wfresult, width,hatch="-",color='white',ecolor='k')
	rects1 = ax.bar(ind, YosemiteResult, width,hatch="/",color='#AAAAAA',ecolor='k')
	rects2 = ax.bar(ind+width, VarysResult, width,hatch="+",color='#DDDDDD',ecolor='k')


	ax.set_xticks(ind+width)
	plt.setp(ax.xaxis.get_majorticklabels(), rotation=30)
	ax.set_xticklabels(('event','vRouter','Druid','Hadoop','Web','VoltDB','HIVE','Redies','backup','data\ndistr'),fontsize=15,fontweight='bold')
	ax.set_yticklabels((0,20,40,60,80,100),fontsize=16,fontweight='bold')
	ax.legend((rects1[0],rects2[0],rects3[0]), ('Yosemite','Varys','TCP'),loc=0,fontsize=15)
	ax.set_ylabel('Average CCT(Normalized)',fontsize=16,fontweight='bold')
	ax.set_ylim([0,100])
	ax.set_xlabel('Application',fontsize=16,fontweight='bold')
	#plt.figure(figsize=(12,3))
	#plt.show()
	fig.savefig("evaluation_motivation2.eps")



	VarysResult=[2,20,14,40,20]
	YosemiteResult=[1,18,12,30,15]
	wfresult=[5,25,20,70,25]

	N=5
	ind = np.arange(N)  # the x locations for the groups
	width = 0.3       # the width of the bars
	#plt.xticks(fontsize=18,fontweight='bold',rotation=30,ha='center')
	fig, ax = plt.subplots()

	rects3 = ax.bar(ind+2*width, wfresult, width,hatch="-",color='white',ecolor='k')
	rects1 = ax.bar(ind, YosemiteResult, width,hatch="/",color='#AAAAAA',ecolor='k')
	rects2 = ax.bar(ind+width, VarysResult, width,hatch="+",color='#DDDDDD',ecolor='k')

	ax.set_xticks(ind+width)
	plt.setp(ax.xaxis.get_majorticklabels())
	ax.set_xticklabels(('S-N','L-N','S-W','L-W','ALL'),fontsize=15,fontweight='bold')
	ax.set_yticklabels((0,20,40,60,80,100,120,140),fontsize=16,fontweight='bold')
	ax.legend((rects1[0],rects2[0],rects3[0]), ('Yosemite','Varys','TCP'),loc=0,fontsize=15)
	ax.set_ylabel('Average WCCT(Normalized)',fontsize=12,fontweight='bold')
	ax.set_ylim([0,100])
	ax.set_xlabel('Coflow Types',fontsize=12,fontweight='bold')
	fig.savefig("evaluation_motivation3.eps")


	VarysResult=[11,35,14,5,11,3]
	YosemiteResult=[9,22,13,5,13,5]
	wfresult=[13,26,21,8,17,7]


	rcParams.update({'font.size': 16,'font.weight':'bold'})
	N=6
	ind = np.arange(N)  # the x locations for the groups
	width = 0.3       # the width of the bars
	#plt.xticks(fontsize=18,fontweight='bold',rotation=30,ha='center')
	fig, ax = plt.subplots()

	rects3 = ax.bar(ind+2*width, wfresult, width,hatch="-",color='white',ecolor='k')
	rects1 = ax.bar(ind, YosemiteResult, width,hatch="/",color='#AAAAAA',ecolor='k')
	rects2 = ax.bar(ind+width, VarysResult, width,hatch="+",color='#DDDDDD',ecolor='k')


	ax.set_xticks(ind+width)
	plt.setp(ax.xaxis.get_majorticklabels(), rotation=20)
	ax.set_xticklabels(('index\nsort','db\n analysis','index\n count','log\n analysis','crawler','word\ncount'),fontsize=15,fontweight='bold')
	ax.set_yticklabels((0,10,20,30,40,50),fontsize=16,fontweight='bold')
	ax.legend((rects1[0],rects2[0],rects3[0]), ('Yosemite','Varys','TCP'),loc=0,fontsize=15)
	ax.set_ylabel('Average CCT(Normalized)',fontsize=16,fontweight='bold')
	ax.set_ylim([0,50])
	ax.set_xlabel('Application',fontsize=16,fontweight='bold')
	#plt.figure(figsize=(12,3))
	#plt.show()
	fig.savefig("evaluation_motivation4.eps")





