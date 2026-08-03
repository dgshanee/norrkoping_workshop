#!/bin/bash

geoips run single_source $GEOIPS_TESTDATA_DIR/test_data_seviri/data/20250624/1200/* \
    --reader_name seviri_hrit \
    --product_name DayMicrophysicswithNIR16Legacy \
    --output_formatter imagery_annotated \
    --filename_formatter geoips_fname \
    --logging_level info \
    --feature_annotator default \
    --gridline_annotator default \
    --resampled_read \
    --sector_list africa
