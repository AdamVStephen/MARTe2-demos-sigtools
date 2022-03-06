set datafile separator ','
set title "GnuPlot : Mains Visualisation Demo 001"
set xlabel "Time (us)"
set ylabel "Mains (V)"

system "../transform/csv2livedat.py 50 1 0"

plot "/var/tmp/tmp.dat" \
	using 1:2 with lines, \
	'' using 1:3 with lines, \
	'' using 1:4 with lines, \
	'' using 1:5 with lines

while (1) {
	pause 0.5
	system "../transform/csv2livedat.py 50 1 0 > /dev/null 2>&1"
	replot
}

pause
	

