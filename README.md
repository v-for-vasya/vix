# VIX
Research into the VIX

<code>vix_calculation.xlsx</code> is a basic VIX calculation

<code>VIXVXO.xlsx</code> is the data of the VIX going back to 1990 when it was first created plus the VXO data which goes back to 1986, capturing the 1987 crash data. The VXO and VIX differ in that the VXO tracks the SP100 and the VIX tracks the SP500, but since they both quite accurately move in sync we can use the VXO data from 1986 to 1990 as VIX data.

<code>mean_shift_algorithm_vix</code> is a clustering algorithm for data that does not necessarily follow normal distributions. Perfect for time series such as the VIX. For a more detailed explanation and bandwidth parameter optimisation of the mean_shift algorithm see: https://spin.atomicobject.com/2015/05/26/mean-shift-clustering/ 
