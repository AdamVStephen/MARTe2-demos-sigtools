
# Hint-1

- Check that an appropriate IOC process is running [See Basic EPICS refresher](../EPICS_Basics.md) 
- If not, try connecting to the IOC shell and use the `dbl` command as follows

```
Starting iocInit
############################################################################
## EPICS R7.0.6
## Rev. R7.0.6-dirty
############################################################################
iocRun: All initialization complete
epics> dbl
FileWriter-Behaviour-5:STATUS
FileWriter-Behaviour-5:COMMAND
FileWriter-Behaviour-5:FILE
FileWriter-Behaviour-5:RESET
FileWriter-Behaviour-5:TIME
FileWriter-Behaviour-5:COUNTER
FileWriter-Behaviour-5:HIST-IDLE-CT
FileWriter-Behaviour-5:HIST-RUN-CT
FileWriter-Behaviour-5:MEASUREMENT0
FileWriter-Behaviour-5:ADC0S
FileWriter-Behaviour-5:ADC1S
FileWriter-Behaviour-5:ADC2S
FileWriter-Behaviour-5:ADC3S
```


# Automated Format

Create a simple bash script as follows to do everything in one.

This script is available for the moment [here](https://github.com/AdamVStephen/MARTe2-sigtools/blob/ayr/bin/md-fw-5).
	
```
#!/usr/bin/env bash
rm -f ../MARTe2-demos-sigtools/temp/*.csv
start_time=$(date --rfc-3339='ns')
./m2 STapp-0007-FileWriter-3.cfg -m StateMachine:START > /tmp/log 2>&1 &
watch -n 1 cat ../MARTe2-demos-sigtools/temp/*.csv
sleep 5
caget
sleep 5
caput
caget
```

Since this is a continuous demo, the script then has to be exited and you need to cleanup with `pkill MARTe`.

## Suggested Exercises

TBA
