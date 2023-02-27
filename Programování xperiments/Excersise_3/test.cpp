#include "TwoDimensionalMeasurement.hpp"
#include <iostream>

int main() {
    // Create a TwoDimensionalMeasurement object with x = 1.0, y = 2.0, var_x = 0.1, var_y = 0.2, and cov_xy = 0.3
    TwoDimensionalMeasurement measurement(1.0, 2.0, 0.1, 0.2, 0.3);

    // Print the x and y coordinates of the measurement
    std::cout << "x = " << measurement.getX() << ", y = " << measurement.getY() << std::endl;

    // Print the variance and covariance of the measurement
    std::cout << "var_x = " << measurement.getVarianceX() << ", var_y = " << measurement.getVarianceY()
              << ", cov_xy = " << measurement.getCovarianceXY() << std::endl;

    // Print the distance, distance error, and significance of the measurement
    std::cout << "distance = " << measurement.getDistance() << ", distance_error = " << measurement.getDistanceError()
              << ", significance = " << measurement.getSignificance() << std::endl;

    return 0;
}