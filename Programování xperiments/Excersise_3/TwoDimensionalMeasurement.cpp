#include <cmath>

class TwoDimensionalMeasurement {
public:
    TwoDimensionalMeasurement(double x, double y, double var_x, double cov_xy, double var_y) :
        x_(x), y_(y), var_x_(var_x), cov_xy_(cov_xy), var_y_(var_y) {}

    double x() const { return x_; }
    double y() const { return y_; }

    double variance_x() const { return var_x_; }
    double covariance_xy() const { return cov_xy_; }
    double variance_y() const { return var_y_; }

    double distance() const { return std::sqrt(x_ * x_ + y_ * y_); }
    double distance_error() const {
        double dx = 2 * x_ * var_x_ + 2 * y_ * cov_xy_;
        double dy = 2 * x_ * cov_xy_ + 2 * y_ * var_y_;
        return std::sqrt(dx * dx + dy * dy) / (2 * distance());
    }

    double significance() const { return distance() / distance_error(); }