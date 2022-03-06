# MARTe Demo : ComtradeWriter-1

This is the most basic test of the ComtradeWriter data sink.

In the style of the FileWriter demos, the following simple Idle/Run toggling StateMachine and EPICS PV interface
permits the user to switch between states that include or exclude the ComtradeWriter object in the real-time thread.

1. ComtradeWriter-1:STATUS
   - Read this PV to retrieve the current state readback from the StateMachine
   - 0 = Idle ; 1 = Run
1. ComtradeWriter-1:COMMAND  
   - Set to 0 for GOTOIDLE message to StateMachine
   - Set to 1 for GOTORUN message to StateMachine
1. ComtradeWriter-1:RESET  
   - Change for RESET message to StateMachine

![Run State](sta_StateRun.png)

## Interactive Instructions

Start the docker and set up the environment to launch MARTe.

```
docker run -it -p 8084:8084 avstephen/marte2-demos-sigtools-ubuntu1804:ayr
root@abcedf:/opt/MARTe/Projects/MARTe2-sigtools/bin# source setenv.sh
root@abcedf:/opt/MARTe/Projects/MARTe2-sigtools/bin# source m2-completion.bash
```
Two terminals are required to see the behaviour matches expectations.

In the first terminal, set up to watch for the changing contents of a file, which by default is
to be created in the MARTe2-demos-sigtools/temp directory.

```
root@abcedf:/opt/MARTe/Projects/MARTe2-sigtools/bin# cd ../MARTe2-demos-sigtools/temp
root@abcedf:/opt/MARTe/Projects/MARTe2-sigtools/MARTe2-demos-sigtools/temp# rm -f *.csv
root@abcedf:/opt/MARTe/Projects/MARTe2-sigtools/MARTe2-demos-sigtools/temp# watch -n 1 cat *.csv
```
In the other terminal, first start the EPICS IOC co-process using the m2ioc wrapper.
The ioc process is run within a tmux container.  Note that the tmux namespace feature is
used to keep the IOC processes from interfering with "normal" tmux sessions.  To
list the IOC tmux sessions either use `tmux -L MARTe2-sigtools list-sessions` or
alternatively the `m2ps` option.
```
root@abcedf:/opt/MARTe/Projects/MARTe2-sigtools/bin# ./m2ioc STapp-0007-FileWriter-5-IOC.db
```

In the other terminal, run the example, providing the command line message to the StateMachine to START.
This will set the run state to IDLE.
```
root@abcedf:/opt/MARTe/Projects/MARTe2-sigtools/bin# ./m2 STapp-0007-FileWriter-5.cfg -m StateMachine:START
```

Now use the `caget` and `caput` commands to exercise the state changes that will select the Run state
which in turn will cause data to be written to the CSV file.

If you get stuck, then read the [Hint-1](Hint-1.md)

