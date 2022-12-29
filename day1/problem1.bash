#!/bin/bash

ELFNEXT="\n"
FOODSUM=0
MAXFOOD=0

while read LINE; do
    size=${#LINE}
    if [ "$size" != 0 ]; then
        FOODSUM=$(expr "$FOODSUM" + "$((LINE))")
    else
        if [[ $MAXFOOD -lt $FOODSUM ]]; then
            MAXFOOD=$FOODSUM
        fi
        FOODSUM=0
    fi
done < data_input

echo $MAXFOOD
