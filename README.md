# Traffix

Traffix is a YOLOv5-based traffic analysis project. The repository includes detection, segmentation, classification, training, validation, and export scripts, plus a checked-in `yolov5s.pt` model for local detection experiments.

This project is derived from Ultralytics YOLOv5 and keeps the upstream AGPL-3.0 license and citation files for attribution.

## Setup

Use Python 3.8 or newer. A virtual environment is recommended.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

If you only want to inspect script options without installing the full ML stack, the Python files can still be syntax-checked with `python3 -m py_compile`.

## Run detection

Run object detection on an image, video, directory, webcam, or stream:

```bash
python detect.py --weights yolov5s.pt --source path/to/image_or_video
```

Results are written under `runs/detect/` by default. Runtime outputs, experiment folders, model weights, and videos are ignored by `.gitignore`; keep new generated artifacts out of commits unless they are intentionally documented fixtures.

## Run segmentation

The root-level `predict.py` runs YOLOv5 segmentation inference:

```bash
python predict.py --weights yolov5s-seg.pt --source path/to/image_or_video
```

Results are written under `runs/predict-seg/` by default.

## Training and validation

Detection training and validation entry points are available as:

```bash
python train.py --data data/coco128.yaml --weights yolov5s.pt
python val.py --data data/coco128.yaml --weights yolov5s.pt
```

Segmentation and classification variants live under `segment/` and `classify/`.
