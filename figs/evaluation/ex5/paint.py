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

	VarysResult=[3,13,4,10,12]
	YosemiteResult=[2,8,4.5,11,14]
	wfresult=[7,12,6,22,25]
	N=5
	ind = np.arange(N)  # the x locations for the groups
	width = 0.3       # the width of the bars
	#plt.xticks(fontsize=18,fontweight='bold',rotation=30,ha='center')
	fig, ax = plt.subplots()

	rects3 = ax.bar(ind+2*width, wfresult, width,hatch="-",color='white',ecolor='k')
	rects1 = ax.bar(ind, YosemiteResult, width,hatch="/",color='#AAAAAA',ecolor='k')
	rects2 = ax.bar(ind+width, VarysResult, width,hatch="+",color='#DDDDDD',ecolor='k')


	ax.set_xticks(ind+width)
	plt.setp(ax.xaxis.get_majorticklabels(), rotation=10)
	ax.set_xticklabels(('map-reduce','file\n copy','file\n distr','data\n backup','data\ndistr'),fontsize=15,fontweight='bold')
	ax.set_yticklabels((0,5,10,15,20,25,30),fontsize=16,fontweight='bold')
	ax.legend((rects1[0],rects2[0],rects3[0]), ('Yosemite','Varys','TCP'),loc=0,fontsize=15)
	ax.set_ylabel('Average CCT(s)',fontsize=16,fontweight='bold')
	ax.set_ylim([0,30])
	ax.set_xlabel('Application',fontsize=16,fontweight='bold')
	fig.savefig("real1.eps")




	VarysResult=[2.5,14,3,9,8.9]
	YosemiteResult=[1.9,8,4.5,10,12]
	wfresult=[6,11,5,24,23]
	N=5
	ind = np.arange(N)  # the x locations for the groups
	width = 0.3       # the width of the bars
	#plt.xticks(fontsize=18,fontweight='bold',rotation=30,ha='center')
	fig, ax = plt.subplots()

	rects3 = ax.bar(ind+2*width, wfresult, width,hatch="-",color='white',ecolor='k')
	rects1 = ax.bar(ind, YosemiteResult, width,hatch="/",color='#AAAAAA',ecolor='k')
	rects2 = ax.bar(ind+width, VarysResult, width,hatch="+",color='#DDDDDD',ecolor='k')


	ax.set_xticks(ind+width)
	plt.setp(ax.xaxis.get_majorticklabels(), rotation=10)
	ax.set_xticklabels(('map-reduce','file\n copy','file\n distr','data\n backup','data\ndistr'),fontsize=15,fontweight='bold')
	ax.set_yticklabels((0,5,10,15,20,25,30),fontsize=16,fontweight='bold')
	ax.legend((rects1[0],rects2[0],rects3[0]), ('Yosemite','Varys','TCP'),loc=0,fontsize=15)
	ax.set_ylabel('Average CCT(s)',fontsize=16,fontweight='bold')
	ax.set_ylim([0,30])
	ax.set_xlabel('Application',fontsize=16,fontweight='bold')
	fig.savefig("real2.eps")




	VarysResult=[12,22,18,8,8.5]
	YosemiteResult=[9,18,19,10,12]
	wfresult=[13,24,29,13,15]
	N=5
	ind = np.arange(N)  # the x locations for the groups
	width = 0.3       # the width of the bars
	#plt.xticks(fontsize=18,fontweight='bold',rotation=30,ha='center')
	fig, ax = plt.subplots()

	rects3 = ax.bar(ind+2*width, wfresult, width,hatch="-",color='white',ecolor='k')
	rects1 = ax.bar(ind, YosemiteResult, width,hatch="/",color='#AAAAAA',ecolor='k')
	rects2 = ax.bar(ind+width, VarysResult, width,hatch="+",color='#DDDDDD',ecolor='k')


	ax.set_xticks(ind+width)
	plt.setp(ax.xaxis.get_majorticklabels(), rotation=10)
	ax.set_xticklabels(('Significant','Important','Normal','UnImportant','Lax'),fontsize=15,fontweight='bold')
	ax.set_yticklabels((0,5,10,15,20,25,30),fontsize=16,fontweight='bold')
	ax.legend((rects1[0],rects2[0],rects3[0]), ('Yosemite','Varys','TCP'),loc=0,fontsize=15)
	ax.set_ylabel('Average CCT(s)',fontsize=16,fontweight='bold')
	ax.set_ylim([0,30])
	ax.set_xlabel('Application',fontsize=16,fontweight='bold')
	fig.savefig("real3.eps")




	VarysResult=[11,20,18,8,8.5]
	YosemiteResult=[7,21,18.5,11,13]
	wfresult=[12,22,25,12,16]
	N=5
	ind = np.arange(N)  # the x locations for the groups
	width = 0.3       # the width of the bars
	#plt.xticks(fontsize=18,fontweight='bold',rotation=30,ha='center')
	fig, ax = plt.subplots()

	rects3 = ax.bar(ind+2*width, wfresult, width,hatch="-",color='white',ecolor='k')
	rects1 = ax.bar(ind, YosemiteResult, width,hatch="/",color='#AAAAAA',ecolor='k')
	rects2 = ax.bar(ind+width, VarysResult, width,hatch="+",color='#DDDDDD',ecolor='k')


	ax.set_xticks(ind+width)
	plt.setp(ax.xaxis.get_majorticklabels(), rotation=10)
	ax.set_xticklabels(('Significant','Important','Normal','UnImportant','Lax'),fontsize=15,fontweight='bold')
	ax.set_yticklabels((0,5,10,15,20,25,30),fontsize=16,fontweight='bold')
	ax.legend((rects1[0],rects2[0],rects3[0]), ('Yosemite','Varys','TCP'),loc=0,fontsize=15)
	ax.set_ylabel('Average CCT(s)',fontsize=16,fontweight='bold')
	ax.set_ylim([0,30])
	ax.set_xlabel('Application',fontsize=16,fontweight='bold')
	fig.savefig("real4.eps")









	# VarysResult=[5,11,16,13,1.3,6,18,7,45,33]
	# YosemiteResult=[3,7,11,12,1.5,9,15,12,50,45]
	# wfresult=[4,8,20,18,1.7,8,22,13,70,65]


	# rcParams.update({'font.size': 16,'font.weight':'bold'})
	# N=10
	# ind = np.arange(N)  # the x locations for the groups
	# width = 0.3       # the width of the bars
	# #plt.xticks(fontsize=18,fontweight='bold',rotation=30,ha='center')
	# fig, ax = plt.subplots()

	# rects3 = ax.bar(ind+2*width, wfresult, width,hatch="-",color='white',ecolor='k')
	# rects1 = ax.bar(ind, YosemiteResult, width,hatch="/",color='#AAAAAA',ecolor='k')
	# rects2 = ax.bar(ind+width, VarysResult, width,hatch="+",color='#DDDDDD',ecolor='k')


	# ax.set_xticks(ind+width)
	# plt.setp(ax.xaxis.get_majorticklabels(), rotation=30)
	# ax.set_xticklabels(('event','vRouter','Druid','Hadoop','Web','VoltDB','HIVE','Redies','backup','data\ndistr'),fontsize=15,fontweight='bold')
	# ax.set_yticklabels((0,20,40,60,80,100,120,140),fontsize=16,fontweight='bold')
	# ax.legend((rects1[0],rects2[0],rects3[0]), ('Yosemite','Varys','TCP-FAIR'),loc=0,fontsize=15)
	# ax.set_ylabel('Average CCT(Normalized)',fontsize=16,fontweight='bold')
	# ax.set_ylim([0,100])
	# ax.set_xlabel('Application',fontsize=16,fontweight='bold')
	# #plt.figure(figsize=(12,3))
	# #plt.show()
	# fig.savefig("evaluation_motivation2.eps")



	# VarysResult=[12,37,16,6,12,4]
	# YosemiteResult=[10,25,14,7,15,6]
	# wfresult=[15,30,22,10,18,8]


	# rcParams.update({'font.size': 16,'font.weight':'bold'})
	# N=6
	# ind = np.arange(N)  # the x locations for the groups
	# width = 0.3       # the width of the bars
	# #plt.xticks(fontsize=18,fontweight='bold',rotation=30,ha='center')
	# fig, ax = plt.subplots()

	# rects3 = ax.bar(ind+2*width, wfresult, width,hatch="-",color='white',ecolor='k')
	# rects1 = ax.bar(ind, YosemiteResult, width,hatch="/",color='#AAAAAA',ecolor='k')
	# rects2 = ax.bar(ind+width, VarysResult, width,hatch="+",color='#DDDDDD',ecolor='k')


	# ax.set_xticks(ind+width)
	# plt.setp(ax.xaxis.get_majorticklabels(), rotation=20)
	# ax.set_xticklabels(('index\nsort','db\n analysis','index\n count','log\n analysis','crawler','word\ncount'),fontsize=15,fontweight='bold')
	# ax.set_yticklabels((0,10,20,30,40,50),fontsize=16,fontweight='bold')
	# ax.legend((rects1[0],rects2[0],rects3[0]), ('Yosemite','Varys','TCP-FAIR'),loc=0,fontsize=15)
	# ax.set_ylabel('Average CCT(Normalized)',fontsize=16,fontweight='bold')
	# ax.set_ylim([0,50])
	# ax.set_xlabel('Application',fontsize=16,fontweight='bold')
	# #plt.figure(figsize=(12,3))
	# #plt.show()
	# fig.savefig("evaluation_motivation3.eps")

	# VarysResult=[11,35,14,5,11,3]
	# YosemiteResult=[9,22,13,5,13,5]
	# wfresult=[13,26,21,8,17,7]


	# rcParams.update({'font.size': 16,'font.weight':'bold'})
	# N=6
	# ind = np.arange(N)  # the x locations for the groups
	# width = 0.3       # the width of the bars
	# #plt.xticks(fontsize=18,fontweight='bold',rotation=30,ha='center')
	# fig, ax = plt.subplots()

	# rects3 = ax.bar(ind+2*width, wfresult, width,hatch="-",color='white',ecolor='k')
	# rects1 = ax.bar(ind, YosemiteResult, width,hatch="/",color='#AAAAAA',ecolor='k')
	# rects2 = ax.bar(ind+width, VarysResult, width,hatch="+",color='#DDDDDD',ecolor='k')


	# ax.set_xticks(ind+width)
	# plt.setp(ax.xaxis.get_majorticklabels(), rotation=20)
	# ax.set_xticklabels(('index\nsort','db\n analysis','index\n count','log\n analysis','crawler','word\ncount'),fontsize=15,fontweight='bold')
	# ax.set_yticklabels((0,10,20,30,40,50),fontsize=16,fontweight='bold')
	# ax.legend((rects1[0],rects2[0],rects3[0]), ('Yosemite','Varys','TCP-FAIR'),loc=0,fontsize=15)
	# ax.set_ylabel('Average CCT(Normalized)',fontsize=16,fontweight='bold')
	# ax.set_ylim([0,50])
	# ax.set_xlabel('Application',fontsize=16,fontweight='bold')
	# #plt.figure(figsize=(12,3))
	# #plt.show()
	# fig.savefig("evaluation_motivation4.eps")





