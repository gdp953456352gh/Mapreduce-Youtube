#!/usr/bin/python

# Import relevant module
import sys

def reduce(args):
	country1video=[]
	country2video=[]
	trendnum=0
	countryname1=sys.argv[1]
	countryname2=sys.argv[2]
	key=""
	current_tag = ""
	# For every line in the data...
	for line in sys.stdin:
	    data = line.strip().split('\t')
	    if len(data) == 3:
		category,video,country = data
	    if current_tag != category:
		if current_tag != "":
		    for a in country1video:
		        if(a in country2video):
		            trendnum=trendnum+1
                    if len(country1video)!=0:
		        percentage= trendnum*100.00/len(country1video)
                    else:
                        percentage=0
		    #percentage= trendnum/(len(country2video)+1)
		    print '{0}: Total:\t{1};\t{2}% in {3}'.format(current_tag, len(country1video),round(percentage,1),countryname2)
		country1video=[]
		country2video=[]
		trendnum=0
		current_tag = category
	    if country==countryname1:
		if(video not in country1video):
		    country1video.append(video)
	    if country==countryname2:
		if(video not in country2video):
		    country2video.append(video)   
        for a in country1video:
            if(a in country2video):
		trendnum=trendnum+1
        if len(country1video)!=0:
	    percentage= trendnum*100.00/len(country1video)
        else:
            percentage=0
	print '{0}: Total:\t{1};\t{2}% in {3}'.format(current_tag, len(country1video),round(percentage,1),countryname2)
if __name__=="__main__":
	reduce(sys.argv[1:])

