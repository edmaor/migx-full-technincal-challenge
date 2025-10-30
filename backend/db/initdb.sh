mongoimport --host localhost --port 27017 \
  -u root -p example --authenticationDatabase admin \
  --db participants_db --collection participants \
  --file /docker-entrypoint-initdb.d/participants.json --jsonArray