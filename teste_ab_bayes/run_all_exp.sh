#!/bin/bash

python bayes_dashboard.py \
& python ctr_dashboard.py \
& app_control.py \
& python app_treatment.py \
& python webscrap_control.py \
& python webscrap_treatment.py

 