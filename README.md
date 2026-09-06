A very primitive version of the 'Kuch Kuch Hota Hai' air piano player (for context: https://youtu.be/6-XxLVTMr30?si=b_AxLOiF_NRdYa-E). To play the exact tune, put down your index finger, then middle, again index, then ring, and finally index.

Commands to run the program:

	python3.11 -m venv ~/mp-env
    source ~/mp-env/bin/activate
    pip install mediapipe==0.10.14 opencv-python
    pip install mediapipe
	pip install pygame
    python3 path/to/piano.py
