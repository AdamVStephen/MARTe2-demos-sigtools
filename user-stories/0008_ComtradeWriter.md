# ComtradeWriter Demonstrations. 

Comtrade is a standard file format for data in the energy sector.  The requirements for the ComtradeWriter data sink are to support generation of data files as follows :

1. Option to record a snapshot of values periodically with a fixed period and phase.  e.g. 5 seconds of data, every minute, on the minute.
1. Option to record a snapshot of values based on a trigger signal.
1. Option to rotate a continually recording file every N lines of output.

Goal : to provide some simple to use demonstrations of the FileWriter functionality.

## Tested Demonstrations

- TODO

## Work in Progress / Design Ideas

- Best syntax to express the capture characteristics.  Consider e.g. cron as a model ?

## Credits

The implementation of the examples added for this use case was originally made by Richard Padden.
