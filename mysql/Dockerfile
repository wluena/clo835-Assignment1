# Use the official MySQL image
FROM mysql:5.7

# Set environment variables for the database
# These can also be passed at runtime using 'docker run -e'
ENV MYSQL_ROOT_PASSWORD=pw
ENV MYSQL_DATABASE=webapp_db

# (Optional) Copy a .sql script to initialize the database
# COPY init.sql /docker-entrypoint-initdb.d/