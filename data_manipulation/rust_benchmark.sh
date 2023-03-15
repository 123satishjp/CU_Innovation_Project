#!/bin/bash

echo "Enter the type of operation to be performed (filter/groupby/mutation/join): "
read operation

case $operation in
    filter)
        time ./terrorism_filter
        ;;
    groupby)
        time ./terrorism_groupby
        ;;
    mutation)
        time ./terrorism_mutation
        ;;
    join)
        time ./terrorism_join
        ;;
    *)
        echo "Invalid operation. Please enter filter/groupby/mutation/join."
        ;;
esac
