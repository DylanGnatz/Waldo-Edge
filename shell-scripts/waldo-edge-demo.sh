
./WaldoEdge_sync.sh

sudo ~/.virtualenvs/cv3/bin/python /home/pi/WaldoEdge/facial-recognition/encode_faces.py --dataset /home/pi/WaldoEdge/WaldoEdge_Photos --encodings test.pickle

sudo ~/.virtualenvs/cv3/bin/python /home/pi/WaldoEdge/facial-recognition/waldo_edge_recognition.py --cascade /home/pi/WaldoEdge/facial-recognition/haarcascade_frontalface_default.xml --encodings test.pickle