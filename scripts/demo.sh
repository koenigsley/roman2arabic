#!/usr/bin/env bash
ROMANS="MMIX XLIII XC CD CMXCVII"
for roman in $ROMANS
do
  echo "Roman: $roman; Arabic: $(python3 -m roman2arabic translate --roman "$roman")"
done
