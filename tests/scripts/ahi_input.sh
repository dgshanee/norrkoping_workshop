#!/bin/bash

PRODUCT_NAME=$1

geoips run single_source $GEOIPS_TESTDATA_DIR/test_data_ahi/data/20220109_2000_terminator/* \
  --reader_name ahi_hsd \
  --product_name $PRODUCT_NAME \
  --output_formatter imagery_annotated \
  --filename_formatter geoips_fname \
  --logging_level info \
  --feature_annotator default \
  --resampled_read \
  --gridline_annotator default \
  --sector_list conus
retval=$?

exit $retval
