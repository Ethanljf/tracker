printf "STARTING SCAN CONTAINER\n"

cd $TRACKER_HOME
tracker run --scan here ${TRACKER_AWS_SECRET+"--lambda --lambda-profile lambda"}
