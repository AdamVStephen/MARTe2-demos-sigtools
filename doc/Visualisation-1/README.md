# MARTe Demo : Visualisation-1

This demonstration shows how to generate a continually growing CSV file and plot live updates in gnuplot.

This is a teaching demo and the techniques used here are not intended for a slick production situation.

## Interactive Instructions

Start the docker and set up the environment to launch MARTe noting the special flags to allow X applications to run.
If running on Windows you also will need an X server.  I recommend MobaXterm.

```
docker run -it -net host -v/tmp/.X11-unix/:/tmp/.X11-unix -v$HOME/.Xauthority:/root/.Xauthority:rw avstephen/marte2-demos-sigtools-centos7:v1.0.2
root@abcedf:/opt/MARTe/Projects/MARTe2-utils/bin# source setenv.sh
root@abcedf:/opt/MARTe/Projects/MARTe2-utils/bin# source m2-completion.bash
root@abcedf:/opt/MARTe/Projects/MARTe2-utils/bin# ./m2 STapp-0009-Visualisation-1.cfg -s Run
```

## YouTube Instructions

[YouTube Video](https://youtu.be/C2ooPCUe-s0)
