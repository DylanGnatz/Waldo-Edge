
sudo aws s3 sync s3://people-finder-photos/private/us-west-2:cb5af86d-baef-4286-9bed-58d3dec67558/ /home/pi/WaldoEdge_Photos/

sudo ~/.virtualenvs/cv3/bin/python /home/pi/WaldoEdge/facial-recognition/encode_faces.py --dataset /home/pi/WaldoEdge/WaldoEdge_Photos --encodings test.pickle

sudo ~/.virtualenvs/cv3/bin/python /home/pi/WaldoEdge/facial-recognition/waldo_edge_recognition.py --cascade haarcascade_frontalface_default.xml --encodings test.pickle