import osgeo.ogr as ogr, csv, sys

shpfile = r"shp2\cb_2018_us_county_500k.shp"
csvfile = r"us_boundaries.csv"

# Open files
csvfile = open(csvfile, "w")
ds = ogr.Open(shpfile)
lyr = ds.GetLayer()

# Get field names
dfn = lyr.GetLayerDefn()
nfields = dfn.GetFieldCount()
fields = []
for i in range(nfields):
    fields.append(dfn.GetFieldDefn(i).GetName())
fields.append("kmlgeometry")
csvwriter = csv.DictWriter(csvfile, fields)
try:
    csvwriter.writeheader()  # python 2.7+
except:
    csvfile.write(",".join(fields) + "\n")

# Write attributes and kml out to csv
for feat in lyr:
    attributes = feat.items()
    geom = feat.GetGeometryRef()
    attributes["kmlgeometry"] = geom.ExportToKML()
    csvwriter.writerow(attributes)

# clean up
del csvwriter, lyr, ds
csvfile.close()
