# docker build -t mongo .
# docker run --name mongo -d mongo
# 
# docker exec -it mongo mongosh

# Use the official MongoDB image as base
FROM mongodb/mongodb-community-server:latest

# Expose port 27017 for MongoDB server
EXPOSE 27017

# Start MongoDB server when container runs
CMD ["mongod"]