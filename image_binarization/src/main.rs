use image::{GrayImage, ImageBuffer};
use imageproc::contrast::threshold;

fn main() {
    // Load the image and convert to grayscale
    let img = image::open("/home/scrad/Pictures/saif.jpg").unwrap().into_luma8();

    // Threshold the image
    let thresholded_img: GrayImage = threshold(&img, 128);

    // Save the thresholded image
    thresholded_img.save("output.png").unwrap();
}
