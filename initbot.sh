echo("Hello, i build a bot for you")
echo("Please run this script in the directory where you want to build the bot with the sudo comand")
echo("                       ")

echo("Now we build the bot with the dockefile")
sudo docker build -t tecfanbot .
echo("                       ")
echo("CryptoBot build complete")


echo("Now we run the bot with the docker run command")
sudo docker run -it tecfanbot 
echo("                       ")
echo("CryptoBot it's running check telegram and write something") 