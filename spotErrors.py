import json
fileNames = ['LJ902A170913AT00010_IRRADIANCE', 'LJ902A180124AT00080_IRRADIANCE', 'LJ902A180124AT00087_IRRADIANCE', 'LJ902A180124AT00099_IRRADIANCE', 'LJ902A180301AT00011_IRRADIANCE']


for name in fileNames:
	fp = open(name + '.json')
	irradDict = json.load(fp)
	postMask = irradDict['IRRADIANCE']['map_irradiance_test']['map_data']
	postMaskSortedByIrradiance = sorted(postMask.values(), key = lambda y: y['irrad'])
	maxIrrad = postMaskSortedByIrradiance[int(.99*len(postMaskSortedByIrradiance))]
	minIrrad = postMaskSortedByIrradiance[int(.01*len(postMaskSortedByIrradiance))]
	print('---------')
	print(name)
	print(maxIrrad)
	print(minIrrad)
	fp.close()
	# 123076 - 123076 * (100/1920) = 116665.791667
	# 73896 - 73896 * (100/1080) = 67053.7777778

	#https://plot.ly/~KianKa/1/
