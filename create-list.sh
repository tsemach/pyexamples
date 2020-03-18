#!/bin/bash

find pyexamples -name \*.py | grep -v __init__.py > pyexamples.list.all
rm -f pyexamples.list

for f in `cat pyexamples.list.all`
do
	git ls-files --error-unmatch $f > /dev/null 2>&1
	if [ $? -eq 0 ] 
	then
		echo $f >> pyexamples.list
	fi 
done

rm -f pyexamples.list.all
