# MARTe2 Basics

A brief refresher.

1. `MARTeApp.ex` is the top level runtime executable.
1. Default arguments are `-l RealTimeLoader -c Application.cfg [-s State]|[-m Message]`
1. The `LD_LIBRARY_PATH` is heavily customised and defines where to find binary components.
1. `Main.sh` is the syntactic sugar to deal with much of the environment setup.
1. `m2` is a top level script to minimise the amount of typing.
1. `setenv.sh` and `m2-completion.bash` set other important PATHs for MARTe2-sigtools
1. `m2 Config.cfg [-s State]|[-m Message]` will run the main application.
1. The choice of `State` and `Message` depending on the Application configuration.
1. If the application contains a web server component, look for the Port definition.
1. If running in docker, use the relevant flags to map disk volumes and network ports.

If the application includes an EPICS server, you also need to run an IOC process.

See [EPICS Basics](EPICS_Basics.md) for details.
