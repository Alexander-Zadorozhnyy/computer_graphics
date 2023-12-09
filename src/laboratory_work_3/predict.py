import argparse

from ultralytics import YOLO


def get_parser_args():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "--model_path",
        "-m",
        type=str,
        default="model_path_root",
        help="root path to model",
    )
    parser.add_argument(
        "--img_path", "-i", type=str, default="img_path", help="path to image"
    )
    return vars(parser.parse_args())


def main(model_path, img_path):
    # Load a model
    model = YOLO(model_path)  # load a custom model

    # Predict with the model
    print(model.predict(img_path)[0].probs)  # predict on an image


if __name__ == "__main__":
    args = get_parser_args()
    main(model_path=args["model_path"], img_path=args["img_path"])
