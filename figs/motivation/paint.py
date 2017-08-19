# encoding: utf-8
import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy import stats

from matplotlib import rcParams
rcParams.update({'font.size': 18,'font.weight':'bold'})

patterns = ('/','//','-', '+', 'x', '\\', '\\\\', '*', 'o', 'O', '.')

WIDTH=20


wfresult=[70,20,10,40,10,5,2,15,25,80,40]
wfresult2=[25,10,20,50,20,15]
if __name__=='__main__':


	xticklabel=('file\ndistribute','Druid','Hadoop','HIVE','vRouter','Web','event','Redies','VoltDB','file\nbackup','sql')
	xlabel='Application'
	N=11
	ind = np.arange(N)  # the x locations for the 
	width = 1      # the width of the bars
	fig, ax = plt.subplots(dpi=1000)
	rects1 = ax.bar(ind, wfresult, width, hatch="//",color='#DDDDDD',ecolor='k')
	ax.set_xticks(ind+width)
	ax.set_xticklabels(xticklabel,fontsize=12,fontweight='bold',rotation=20,ha='right')
	ax.set_ylabel('Average Completion Time(Normalized)',fontsize=18,fontweight='bold')
	#ax.set_xlabel(xlabel,fontsize=12,fontweight='bold')
	ax.set_ylim([0,100])
	fig.savefig("motivation1.eps")


	xticklabel=('index\nsort','log\n analysis','crawler','db\n analysis','index\n count','word\ncount')
	xlabel='Application'
	N=6
	ind = np.arange(N)  # the x locations for the 
	width = 1      # the width of the bars
	fig, ax = plt.subplots(dpi=1000)
	rects1 = ax.bar(ind, wfresult2, width, hatch="//",color='#DDDDDD',ecolor='k')
	ax.set_xticks(ind+width)
	ax.set_xticklabels(xticklabel,fontsize=12,fontweight='bold',rotation=20,ha='right')
	ax.set_ylabel('Average Completion Time(Normalized)',fontsize=18,fontweight='bold')
	#ax.set_xlabel(xlabel,fontsize=12,fontweight='bold')
	ax.set_ylim([0,100])

	fig.show()
	fig.savefig("motivation2.eps")



