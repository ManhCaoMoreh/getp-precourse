import numpy as np
import matplotlib.pyplot as plt


def load_image(file_path):
    image = np.load(file_path)
    return image


def apply_convolution(images, kernel, stride=1, padding=0):
    """
    Implement 2D Convolution Using Numpy
    =================================================================================================
    Arguments:
        + images: np.array of shape (B, input_H, input_W)
        + kernel: np.array of shape (kernel_h, kernel_w)
        + stride: integer
        + padding: integer
    Outputs:
        + output_images: np.array of shape (B, input_H, input_W)
    """

    n, image_h, image_w = images.shape
    kernel_h, kernel_w = kernel.shape

    image_pad_h = (stride * (image_h - 1) + kernel_h - image_h) // 2
    image_pad_w = (stride * (image_w - 1) + kernel_w - image_w) // 2

    output_h = (image_h + 2 * image_pad_h - kernel_h) // stride + 1
    output_w = (image_w + 2 * image_pad_w - kernel_w) // stride + 1

    output_images = np.zeros((n, output_h, output_w))

    for index, image in enumerate(images):
        padded_image = np.pad(
            image,
            ((image_pad_h, image_pad_h), (image_pad_w, image_pad_w)),
            mode="constant",
            constant_values=0,
        )
        output_image = np.zeros((output_h, output_w))
        for i in range(0, output_h * stride, stride):
            for j in range(0, output_w * stride, stride):
                output_image[i // stride, j // stride] = np.mean(
                    np.multiply(
                        padded_image[i : i + kernel_h, j : j + kernel_w], kernel
                    )
                )

        output_images[index] = output_image

    return output_images


if __name__ == "__main__":
    input_file_path = "input_image.npy"

    input_images = load_image(input_file_path)
    num_images = input_images.shape[0]

    # Sobel filter
    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

    result_x = apply_convolution(input_images, sobel_x, stride=1, padding=1)
    result_y = apply_convolution(input_images, sobel_y, stride=1, padding=1)

    result = np.sqrt(result_x**2 + result_y**2)

    plt.figure(figsize=(10, 8))

    plt.subplot(2, 2, 1)
    plt.imshow(result[3], cmap="gray")
    plt.title("Image 1")

    plt.subplot(2, 2, 2)
    plt.imshow(result[4], cmap="gray")
    plt.title("Image 2")

    plt.subplot(2, 2, 3)
    plt.imshow(result[5], cmap="gray")
    plt.title("Image 3")

    plt.subplot(2, 2, 4)
    plt.imshow(result[6], cmap="gray")
    plt.title("Image 4")

    plt.tight_layout()

    plt.show()

    """ 
    =================================================================================================
    Save and submit a portion of the processed 32 images. 
    You are free to choose any number of images (recommend 4~8)"
    """
