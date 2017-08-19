# encoding: utf-8
import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy import stats

from matplotlib import rcParams
rcParams.update({'font.size': 18,'font.weight':'bold'})

patterns = ('/','//','-', '+', 'x', '\\', '\\\\', '*', 'o', 'O', '.')

WIDTH=20


#wfresult2=[15,10,18,30,22,3]
wfresult2=[15,30,22,10,18,3]
if __name__=='__main__':

	#xticklabel=('index\nsort','log\n analysis','crawler','db\n analysis','index\n count','word\ncount')
	xticklabel=('index\nsort','db\n analysis','index\n count','log\n analysis','crawler','word\ncount')
	width = 1      # the width of the bars
	plt.bar(range(len(wfresult2)), wfresult2, tick_label=xticklabel,hatch="//",color='#DDDDDD',ecolor='k')
	plt.subplots_adjust(bottom = 0.2)
	plt.ylabel('Average CCT(Normalized)',fontsize=18,fontweight='bold')
	plt.xticks(fontsize=18,fontweight='bold',rotation=30,ha='center')
	plt.ylim(0,50)
	#plt.show()
	plt.savefig("motivation2.eps",dpi=1000)

