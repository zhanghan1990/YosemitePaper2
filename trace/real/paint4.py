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


VarysResult=[5,10,21,20,2,10,24,15,77,70]
YosemiteResult=[5,10,21,20,2,10,24,15,77,70]
if __name__=='__main__':


	rcParams.update({'font.size': 16,'font.weight':'bold'})
	N=10
	ind = np.arange(N)  # the x locations for the groups
	width = 0.5       # the width of the bars
	fig, ax = plt.subplots()
	rects1 = ax.bar(ind, VarysResult, width,hatch="/",color='#AAAAAA',ecolor='k')
	rects2 = ax.bar(ind+width, YosemiteResult, width,hatch="+",color='#DDDDDD',ecolor='k')



	ax.set_xticks(ind+width,rotation=30,ha='center')
	ax.set_xticklabels(('event','vRouter','Druid','Hadoop','Web','VoltDB','HIVE','Redies','data\nbackup','data\ndistr'),fontsize=16,fontweight='bold')
	ax.set_yticklabels((0,1,2,3,4,5),fontsize=16,fontweight='bold')
	ax.legend((rects1[0],rects2[0]), ('Varys','Yosemite'),loc=0,fontsize=15)
	ax.set_ylabel('Average CCT(Normalized)',fontsize=16,fontweight='bold')
	ax.set_ylim([0,150])
	ax.set_xlabel('Application',fontsize=16,fontweight='bold')
	#plt.figure(figsize=(12,3))
	#plt.show()
	fig.savefig("evaluation_motivation.eps")
