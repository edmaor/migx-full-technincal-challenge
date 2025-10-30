mongoimport --host localhost --port 27017 \
  -u admin -p example --authenticationDatabase admin123 \
  --db participants_db --collection participants \
  --file /docker-entrypoint-initdb.d/participants.json --jsonArray