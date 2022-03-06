# MARTe Demo : Visualisation-1

This demonstration shows how to generate a continually growing CSV file and plot live updates in gnuplot.

This is a teaching demo and the techniques used here are not intended for a slick production situation.

## Interactive Instructions

Start the docker and set up the environment to launch MARTe.

```
docker run -it -net host -p 8084:8084 avstephen/marte2-demos-sigtools-centos7:v1.0.0
root@abcedf:/opt/MARTe/Projects/MARTe2-utils/bin# source setenv.sh
root@abcedf:/opt/MARTe/Projects/MARTe2-utils/bin# source m2-completion.bash
root@abcedf:/opt/MARTe/Projects/MARTe2-utils/bin# ./m2 STapp-0009-Visualisation-1.cfg -s Run
```
