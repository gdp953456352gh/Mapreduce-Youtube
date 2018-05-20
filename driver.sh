#!/bin/bash
if [ $# -ne 2 ]; then
    echo "Invalid number of parameters!"
    echo "Usage: ./tag_driver_combiner.sh [input_location] [output_location]"
    exit 1
fi

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.9.0.jar \
-file /home/hadoop/Documents/mapper.py \
-mapper  /home/hadoop/Documents/mapper.py \
-file /home/hadoop/Documents/reducer.py \
-reducer  "python /home/hadoop/Documents/reducer.py $1 $2" \
-input /user/hadoop/videos.csv \
-output /user/hadoop/output
