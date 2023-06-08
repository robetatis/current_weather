### Use openweather.org to get current weather for a user-given city 

1. Build docker image: `docker build -t weather .`
2. Create and run container in interactive detached mode: `docker run -itd weather`
3. Use `docker ps -a` to find `container_id`
4. Start interactive shell session in the running container: `docker exec -it <container_id> sh`
5. Create the `.env` file and add your API key: `echo API_KEY=xxxxxxxxx > .env`, where `xxxx...` = your API key
6. Call `python main.py` to run the program



