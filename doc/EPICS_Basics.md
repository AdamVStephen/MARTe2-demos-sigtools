# EPICS Basics

A brief refresher.

1. `softIoc` is the top level runtime executable.
1. An EPICS database (.db) file is to softIoc as a `cfg` file is to `MARTeApp.ex`
1. A MARTe application file and EPICS database file have to be designed to work in a complementary way.
1. The database defines process variable names (PVs)
1. If the bash ENV is set correctly, the command line `caget` and `caput` commands to read/write PVs will be available.
1. Other ENV variables can be important in a real network (not Docker) context.
1. IOC processes cannot run in the *background* - they must have a controlling tty attached.
1. `tmux` is your friend and allows the IOC process to be run *as though in the background*
1. `tmux` can be used to connect to the console linked to the IOC process
1. The EPICS shell thus accessible has a lot of useful commands.   But EPICS training is a big topic (and £7500 per day).

If the IOC is a co-process for a MARTe2 application, you must start this separately.

See [MARTe2_Basics](MARTe2_Basics.md) for details.
