#!C:\Users\antho\Documents\01-Fifth_Year\STATS\STATS4844\assignments\assignment2\venv\Scripts python

import requests
import xml.etree.ElementTree as ET
import numpy as np
import pandas as pd

def get_boundaries_from_xml(link: str) -> None:
	lats = []
	longs = []
	
	try:
		xml_content = requests.get(link).content
	except Excpetion as e:
		print(f'Error: {e}')
		return -1
	
	tree = ET.fromstring(xml_content)
	
	for child in tree:
		if child.attrib['name'] == "Maine":
			for grandchild in child:
				print(grandchild.tag, grandchild.attrib)
				lats.append(float(grandchild.attrib['lat']))
				longs.append(float(grandchild.attrib['lng']))
		else:
			continue
	final = np.array([longs, lats]).T
	# print(final)
	
	pd.DataFrame(final, columns = ['lng','lat']).to_csv('data/maine_boundaries.csv', index=False)
	
	return(1)
	
	
if __name__ == "__main__":
	get_boundaries_from_xml('http://econym.org.uk/gmap/states.xml')