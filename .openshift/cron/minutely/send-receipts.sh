#!/bin/bash
if [ ! -f $OPENSHIFT_DATA_DIR/last_run ]; then
  touch $OPENSHIFT_DATA_DIR/last_run
fi
if [[ $(find $OPENSHIFT_DATA_DIR/last_run -mmin +1) ]]; then #run every 2 mins
  rm -f $OPENSHIFT_DATA_DIR/last_run
  touch $OPENSHIFT_DATA_DIR/last_run
  date > $OPENSHIFT_PYTHON_LOG_DIR/last_date_cron_ran
fi
