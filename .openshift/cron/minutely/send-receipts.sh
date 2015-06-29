#!/bin/bash
if [ ! -f $OPENSHIFT_DATA_DIR/last_run ]; then
  touch $OPENSHIFT_DATA_DIR/last_run
fi
if [[ $(find $OPENSHIFT_DATA_DIR/last_run -mmin +2) ]]; then #run every 3 mins
  rm -f $OPENSHIFT_DATA_DIR/last_run
  touch $OPENSHIFT_DATA_DIR/last_run
  python "$OPENSHIFT_REPO_DIR/send-receipts.py" 2> /dev/null 1>> "$OPENSHIFT_PYTHON_LOG_DIR/send-receipts.log"
fi
