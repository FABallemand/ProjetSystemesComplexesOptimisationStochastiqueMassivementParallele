set term png
set output "find_sun_mass.png"
set xrange[0:6000]
set xlabel "Number of Evaluations"
set ylabel "Fitness"
plot 'find_sun_mass.dat' using 3:4 t 'Best Fitness' w lines, 'find_sun_mass.dat' using 3:5 t  'Average' w lines, 'find_sun_mass.dat' using 3:6 t 'StdDev' w lines
set term png
set output "find_sun_mass.png"
set xrange[0:6000]
set xlabel "Number of Evaluations"
set ylabel "Fitness"
plot 'find_sun_mass.dat' using 3:4 t 'Best Fitness' w lines, 'find_sun_mass.dat' using 3:5 t  'Average' w lines, 'find_sun_mass.dat' using 3:6 t 'StdDev' w lines
