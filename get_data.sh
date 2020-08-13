# download data
# RUN THIS to setup stuff:
# chmod +x setupstuff.sh

fp=http://files.grouplens.org/datasets/movielens/ml-25m.zip
fn=ml-25m.zip
if [ -f "$fn" ]; then
    echo "$fn exists."
else 
    echo "$fn does not exist."
	wget "$fp"
fi
unzip -a "$fn" #ml-25m.zip

