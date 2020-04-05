#!/bin/bash


if [[ $# -ne 1 ]]; then
  echo "expected path to program"
  exit 1
fi

python3 gen.py

for test in $(find *.test); do
  echo test $test
  expected=$(cat $test | python3 test.py)
  actual=$(cat $test | $1)
  if [[ $actual != $expected ]]; then
    echo "FAILED $test"
    echo actual "$actual"
    echo expected "$expected"
  fi
done
