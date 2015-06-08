#
# vi.py
#
# lambda function implementations of common vegetation indicies used in 
# satellite remote sensing.
#
# Dr. Kevin Davies 03-Jun-15
# School of Geoscience, University of Sydney 2006
#

# Ratio Vegetation Index (RVI)
# Jordan
rvi = lambda r, n: n / r

# Difference Vegetation Index (DVI) or also known as Simple Vegetation Index
# ?
dvi = lambda r, n: n - r

# Normalised Difference Vegetation Index (NDVI) #
# Rouse1976
ndvi = lambda r, n: (n - r) / (n + r)

# Soil Adjusted Vegetation Index (SAVI)
# Huete1988
savi = lambda r, n: 1.5 * (n - r) / (n + r + 0.5)

# EVI Huete2002
evi = lambda r, n, b: 2.5 * (n - r) / (n + 6 * r - 7.5 * b + 1)

# EVI2 Jiang2008
evi2 = lambda r, n: 2.5 * (n - r) / (n + 2.4 * r +1)
    
