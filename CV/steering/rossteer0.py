#!/usr/bin/env python
import keras
import numpy as np
#from keras.layers import Input, Dense, merge
#from keras.models import Model
#from keras.layers import Convolution2D, Convolution1D, MaxPooling2D, MaxPooling1D, SimpleRNN, Reshape, BatchNormalization
#from keras.layers import Activation, Dropout, Flatten, Dense
#from keras.regularizers import l2
#from keras.utils import plot_model
from keras.models import load_model
#scanDataText = ''
model = load_model('lotlayer.h5')

lidarData = eval('[2.01924991607666, 0.528249979019165, inf, 0.500249981880188, 0.4729999899864197, 0.45100000500679016, 0.429749995470047, 0.4115000069141388, inf, 0.3942500054836273, 0.3792499899864197, 0.36500000953674316, 0.35225000977516174, 0.3397499918937683, inf, 0.3292500078678131, 0.3192499876022339, 0.3095000088214874, 0.3005000054836273, 0.29124999046325684, 0.28299999237060547, 0.27549999952316284, inf, 0.2682499885559082, 0.2619999945163727, 0.2552500069141388, 0.24899999797344208, inf, 0.2434999942779541, 0.2382500022649765, 0.23350000381469727, 0.22849999368190765, 0.2240000069141388, inf, 0.2202499955892563, 0.21574999392032623, 0.2122499942779541, 0.2084999978542328, 0.20524999499320984, 0.2017499953508377, inf, inf, 0.19625000655651093, 0.19349999725818634, 0.19099999964237213, 0.1887499988079071, inf, 0.18649999797344208, 0.18424999713897705, 0.18050000071525574, inf, 0.1784999966621399, 0.1772499978542328, inf, 0.1745000034570694, 0.17550000548362732, inf, inf, 0.1717499941587448, 0.17075000703334808, inf, inf, 0.16750000417232513, inf, 0.1667499989271164, 0.16574999690055847, 0.1655000001192093, 0.1652500033378601, inf, 0.16425000131130219, 0.16374999284744263, inf, 0.16374999284744263, inf, 0.164000004529953, 0.16425000131130219, 0.16324999928474426, inf, 0.16300000250339508, 0.16324999928474426, 0.164000004529953, inf, 0.16449999809265137, 0.16500000655651093, inf, 0.16574999690055847, 0.16574999690055847, 0.16725000739097595, inf, 0.16824999451637268, inf, 0.1704999953508377, inf, 0.1720000058412552, inf, inf, 0.17475000023841858, 0.17599999904632568, inf, 0.17800000309944153, inf, 0.1822499930858612, 0.18449999392032623, inf, inf, 0.18975000083446503, inf, 0.19249999523162842, 0.19574999809265137, 0.19875000417232513, inf, inf, 0.20250000059604645, 0.20624999701976776, 0.21074999868869781, inf, 0.21975000202655792, 0.2214999943971634, 0.22300000488758087, 0.22699999809265137, inf, 0.2342499941587448, inf, 0.23849999904632568, 0.24824999272823334, inf, 0.2567499876022339, 0.2630000114440918, inf, 0.27175000309944153, inf, inf, inf, inf, inf, 3.525749921798706, 3.4857499599456787, inf, 3.453000068664551, 3.434499979019165, 3.3717501163482666, inf, 3.3389999866485596, 3.302999973297119, 3.2699999809265137, 3.236999988555908, inf, 3.233750104904175, 3.202500104904175, 3.1947500705718994, inf, 3.1665000915527344, 3.1419999599456787, 3.132999897003174, inf, 3.128999948501587, 3.103250026702881, 3.078249931335449, inf, 3.0929999351501465, 3.072499990463257, 3.0712499618530273, inf, 3.0457499027252197, 3.0457499027252197, 3.046750068664551, 3.0485000610351562, inf, 3.0480000972747803, 3.0480000972747803, 3.0687499046325684, inf, 3.072499990463257, 3.0759999752044678, 3.0797500610351562, inf, 3.1075000762939453, 3.132499933242798, inf, 3.135999917984009, 3.140000104904175, 3.1675000190734863, 3.198499917984009, inf, 3.202500104904175, 3.234250068664551, 3.239500045776367, inf, 3.3002500534057617, 3.3052499294281006, 3.3712499141693115, inf, 3.3722500801086426, 3.408250093460083, 3.4477500915527344, 3.4887499809265137, inf, 3.5642499923706055, 3.6050000190734863, 3.6500000953674316, inf, 3.6967499256134033, 3.74399995803833, 3.8340001106262207, inf, 3.8802499771118164, 3.97475004196167, 4.0320000648498535, inf, 4.142749786376953, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 1.096250057220459, 1.0892499685287476, 1.0859999656677246, inf, 1.096250057220459, 1.0842499732971191, 1.0789999961853027, 1.0800000429153442, inf, 1.0787500143051147, 1.0792499780654907, 1.0762499570846558, inf, 1.0777499675750732, 1.0817500352859497, 1.0800000429153442, inf, 1.0829999446868896, 1.0852500200271606, 1.0835000276565552, inf, 1.090749979019165, 1.094499945640564, 1.0994999408721924, inf, 1.1042499542236328, 1.1109999418258667, 1.1169999837875366, inf, 1.125249981880188, 1.131250023841858, 1.1399999856948853, 1.152999997138977, inf, 1.1632499694824219, 1.1729999780654907, 1.184999942779541, inf, 1.1959999799728394, 1.2087500095367432, 1.221250057220459, inf, 1.2374999523162842, inf, 3.530250072479248, 3.60575008392334, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 1.1239999532699585, inf, 1.1109999418258667, 1.1239999532699585, inf, 2.448499917984009, inf, 1.0149999856948853, 0.9927499890327454, inf, 0.996749997138977, inf, 3.847249984741211, inf, inf, inf, 4.894000053405762, 4.300250053405762, 4.7507500648498535, inf, 4.684999942779541, 4.679749965667725, 4.61299991607666, inf, 4.547999858856201, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 2.2174999713897705, inf, 2.20674991607666, 2.2039999961853027, 2.1752500534057617, inf, inf, 1.9945000410079956, 1.9917500019073486, inf, 2.006999969482422, 2.0185000896453857]'.replace('inf', 'None'))

print(lidarData)
count1 = 0
for y in lidarData:
    lidarData[count1] = [count1+1, y]
    count1 = count1 + 1

lidarData = [lidarData]
#print(lidarData)

o = model.predict(np.array(lidarData), batch_size=32, verbose=2)
output = o[0]

print (o)

jstk = output[0]
print(jstk)
