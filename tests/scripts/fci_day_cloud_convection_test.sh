#!/bin/bash

geoips run single_source $GEOIPS_TESTDATA_DIR/test_data_fci/data/20250623/1200/*.nc \
    --reader_name fci_netcdf \
    --product_name DayCloudConvection \
    --output_formatter imagery_annotated \
    --filename_formatter geoips_fname \
    --logging_level info \
    --feature_annotator default \
    --gridline_annotator default \
    --resampled_read \
    --sector_list africa
