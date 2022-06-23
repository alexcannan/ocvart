from pathlib import Path

import cv2


def convert_to_cr(image_path: Path, output: Path):
    im = cv2.imread(str(image_path))
    tc = cv2.cvtColor(im, cv2.COLOR_BGR2YCR_CB)
    tc[:,:,1] = 0
    tc[:,:,2] = 0
    cv2.imwrite(str(output), tc)
    # TODO: this is just outputing RGB channels?


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='converts image color')
    parser.add_argument('image_path', type=Path, help='path to input image')
    parser.add_argument('-o', '--output', type=Path, help='output path')
    args = parser.parse_args()

    convert_to_cr(args.image_path, Path(f"{args.image_path.stem}_y").with_suffix(args.image_path.suffix))