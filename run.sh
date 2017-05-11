#!/bin/sh
source /web/activities/ghs/public/env/bin/activate
export FLASK_APP=/web/activities/ghs/public/app.py
export APP_SETTINGS="config.ProductionConfig"
/web/activities/ghs/public/env/bin/python app.py $PORT
