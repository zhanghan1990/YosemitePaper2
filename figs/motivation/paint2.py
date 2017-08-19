# encoding: utf-8
import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy import stats

from matplotlib import rcParams
rcParams.update({'font.size': 18,'font.weight':'bold'})

patterns = ('/','//','-', '+', 'x', '\\', '\\\\', '*', 'o', 'O', '.')

WIDTH=20


wfresult=[5,10,21,20,2,10,24,15,77,70]
if __name__=='__main__':


	#xticklabel=('data\ndistr','Druid','Hadoop','HIVE','vRouter','Web','event','Redies','VoltDB','data\nbackup')
	xticklabel=('event','vRouter','Druid','Hadoop','Web','VoltDB','HIVE','Redies','data\nbackup','data\ndistr')
	xlabel='Application'
	N=10
	ind = np.arange(N)  # the x locations for the 
	width = 1      # the width of the bars
	plt.bar(range(len(wfresult)), wfresult, tick_label=xticklabel,hatch="//",color='#DDDDDD',ecolor='k')
	plt.subplots_adjust(bottom = 0.2)
	plt.ylabel('Average CCT(Normalized)',fontsize=18,fontweight='bold')
	plt.xticks(fontsize=18,fontweight='bold',rotation=30,ha='center')
	#plt.show()
	plt.ylim(0,100)
	plt.savefig("motivation1.eps",dpi=1000)

