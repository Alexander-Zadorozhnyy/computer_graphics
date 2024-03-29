import argparse
import os

from ultralytics import YOLO, checks

os.environ["CUDA_LAUNCH_BLOCKING"] = "1"
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


def get_parser_args():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "--model",
        type=str,
        default="yolov8n.pt",
        help="root path to " "saved model or standard yolo model",
    )
    parser.add_argument(
        "--data", type=str, default="dataset/", help="root path to dataset"
    )
    parser.add_argument("--epoch", type=int, default=1, help="number of epoch")
    parser.add_argument("--imgsz", type=int, default=128, help="image size")
    parser.add_argument(
        "--batch", type=int, default=1, help="number of sample in batch"
    )
    parser.add_argument(
        "--augment", type=bool, default=False, help="enable data augmentation or not"
    )

    return vars(parser.parse_args())


def train(model_name, data, epoch, imgsz, batch, augment):
    checks()
    model = YOLO(model_name)

    # Training
    model.train(
        data=data,
        imgsz=imgsz,
        epochs=epoch,
        batch=batch,
        pretrained=True,
        augment=True,
        name=f'rpc_{model_name}_{epoch}e_{batch}b_{"aug" if augment else ""}',
    )

    # Validation
    model.val(split="test")


if __name__ == "__main__":
    args = get_parser_args()
    train(
        model_name=args["model"],
        data=args["data"],
        epoch=args["epoch"],
        imgsz=args["imgsz"],
        batch=args["batch"],
        augment=args["augment"],
    )

# python train.py --model E:\Semester5\computer_graphics\src\laboratory_work_3\runs\classify\rpc_yolov8x-cls.pt_10e_10b_aug2\weights\best.pt --imgsz 224 --epoch 10 --batch 10 --augment True
