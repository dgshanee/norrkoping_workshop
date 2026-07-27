#!/bin/bash

geoips run single_source $GEOIPS_TESTDATA_DIR/test_data_abi/data/goes16_20200918_1950/* \
    --reader_name abi_netcdf \
    --product_name Day-Land-Cloud \
    --output_formatter imagery_annotated \
    --filename_formatter geoips_fname \
    --logging_level info \
    --feature_annotator default \
    --gridline_annotator default \
    --resampled_read \
    --sector_list conus
