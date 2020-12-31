#!/usr/bin/env python3
import gpxpy, csv, glob, re

for file in sorted(glob.glob('gpx-files/*.gpx')):
    print(file)
    gpx_file = open(file, 'r')
    gpx = gpxpy.parse(gpx_file)
    count = 0
    #iterate through rows and append each gpx row to merged csv
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                fields=['{0},{1},{2}'.format(point.latitude, point.longitude, point.time)]
                #Here double whitespace is removed so QGIS accepts the time format
                re.sub(' +',' ',fields[0])
                count += 1
                if count % 2 == 0:
                    with open(r'merged.csv', 'a') as f:
                        writer = csv.writer(f, quoting=csv.QUOTE_NONE, escapechar=' ', lineterminator='\n')
                        writer.writerow(fields)
