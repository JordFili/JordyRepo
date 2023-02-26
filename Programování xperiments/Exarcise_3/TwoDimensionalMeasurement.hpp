#ifndef TWO_DIMENSIONAL_MEASUREMENT_HPP
#define TWO_DIMENSIONAL_MEASUREMENT_HPP

class TwoDimensionalMeasurement {
public:
    TwoDimensionalMeasurement(double x, double y, double var_x, double var_y, double cov_xy);

    double getX() const;
    double getY() const;
    double getVarianceX() const;
    double getVarianceY() const;
    double getCovarianceXY() const;
    double getDistance() const;
    double getDistanceError() const;
    double getSignificance() const;

private:
    double x;
    double y;
    double var_x;
    double var_y;
    double cov_xy;
};

#endif // TWO_DIMENSIONAL_MEASUREMENT_HPP                                                   