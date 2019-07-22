python3 encode_faces.py --dataset waldo-edge-photos --encodings waldo-edge-encodings.pickle
pkill -f waldo_edge_recognition.py
python waldo_edge_recognition.py --cascade haarcascade_frontalface_default.xml --encodings waldo-edge-encodings.pickle