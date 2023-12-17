import numpy as np
import matplotlib.pyplot as plt
import cv2
import pickle


def load_image(file_path):
    image = np.load(file_path)
    return image


def apply_convolution(images, kernel, stride=1, padding=0):
    '''
    Implement 2D Convolution Using Numpy
    =================================================================================================
    Arguments:
        + images: np.array of shape (B, input_H, input_W)
        + kernel: np.array of shape (kernel_H, kernel_W)
        + stride: integer
        + padding: integer
    Outputs:
        + output_images: np.array of shape (B, input_H, input_W)
    '''
    ### TODO: fill in here ###

    N, image_H, image_W = images.shape
    kernel_H, kernel_W = kernel.shape

    image_pad_H = (stride * (image_H - 1) + kernel_H - image_H) // 2
    image_pad_W = (stride * (image_W - 1) + kernel_W - image_W) // 2

    output_H = (image_H + 2 * image_pad_H - kernel_H) // stride + 1
    output_W = (image_W + 2 * image_pad_W - kernel_W) // stride + 1

    output_images = np.zeros((N, output_H, output_W))

    for index, image in enumerate(images):
        padded_image = np.pad(image, ((image_pad_H, image_pad_H), (image_pad_W, image_pad_W)), mode='constant', constant_values=0)
        output_image = np.zeros((output_H, output_W))
        for i in range(0, output_H * stride, stride):
            for j in range(0, output_W * stride, stride):
                output_image[i // stride, j // stride] = np.mean(np.multiply(padded_image[i:i + kernel_H, j:j + kernel_W], kernel))

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

    result = np.sqrt(result_x ** 2 + result_y ** 2)

    plt.figure(figsize=(10, 8))

    plt.subplot(2, 2, 1)
    plt.imshow(result[3], cmap='gray')
    plt.title('Image 1')

    plt.subplot(2, 2, 2)
    plt.imshow(result[4], cmap='gray')
    plt.title('Image 2')

    plt.subplot(2, 2, 3)
    plt.imshow(result[5], cmap='gray')
    plt.title('Image 3')

    plt.subplot(2, 2, 4)
    plt.imshow(result[6], cmap='gray')
    plt.title('Image 4')

    plt.tight_layout()

    plt.show()

    '''
    =================================================================================================
    Save and submit a portion of the processed 32 images. 
    You are free to choose any number of images (recommend 4~8)."
    '''
