#!/usr/bin/env bash
#
# Bash completion support for m2 top level execution script.
#
# Ideas to implement : m2ls with completions based on MARTe2_CONFIGPATH

# REF : https://stackoverflow.com/questions/57426500/list-directories-at-a-specific-path-as-autocomplete-options-for-a-bash-script
# The following stackoverflow answer falls down on the underscore functions not being recognised : TO FIX

_configs()
{
	local cfgs cur
	cfgs=$(ls -1 ${MARTe2_CONFIG_DIR}/*.cfg | while read f; do echo $(basename $f); done)
	cur=${COMP_WORDS[COMP_CWORD]}
	COMPREPLY=( $(compgen -W "$cfgs" -- ${cur}) )
	return 0
}
#} && complete -o nospace -F _configs m2} && complete -o nospace -F _configs m2

complete -F _configs m2
complete -F _configs m2less
complete -F _configs m2check
