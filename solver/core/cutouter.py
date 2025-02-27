from pathlib import Path

import cv2

from .reshaper import Reshaper


class CutOuter:
    def __init__(self, image_path: str, size: int = 28) -> None:
        self.image_path = Path(image_path)
        self.temp = self.image_path.parent / self.image_path.stem
        self.reshaper = Reshaper(self.image_path.as_posix(), size)
        self.img = self.reshaper.reshape()

    def cutout(self, eps=0) -> None:
        self.temp.mkdir(exist_ok=True)
        height = self.img.shape[0]
        cru = height // 9

        for y in range(9):
            for x in range(9):
                temp = self.img[
                    cru * x + eps : cru * (x + 1) - eps,
                    cru * y + eps : cru * (y + 1) - eps,
                ]
                cv2.imwrite(str(self.temp / f"{x}{y}.jpg"), temp)
