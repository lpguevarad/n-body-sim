#include <cmath>
#include <array>

using namespace std;

class Planet{
public:

    double m;
    array <double, 3> x;
    array <double, 3> v;
    array <double, 3> a;
    double energy;
    double omega;
    
    Planet (double mass, double x_position, double y_position, double z_position, double x_velocity, double y_velocity, double z_velocity) {
        m = mass;
		x[0] = x_position;
		x[1] = y_position;
        x[2] = z_position;
		v[0] = x_velocity;
        v[1] = y_velocity;
        v[2] = z_velocity;
    };
    void computeKineticEnergy(){
        energy = 0.5 * m * (pow(v[0],2)+pow(v[1],2)+pow(v[2],2));
    }
};
