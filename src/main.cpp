#include <iostream>
#include <gsl/gsl_errno.h>
#include <gsl/gsl_matrix.h>
#include <gsl/gsl_odeiv2.h>
#include "Planet.h"
#include "ode.h"

using namespace std;

int main(int argc, char *argv[]) {
    Planet p = Planet(32.1, 0, 0, 0, 0, 0, 0);  

    cout << "Test Planet class:" << endl;
    cout << p.m << endl;

    cout << "Test compilation and linking of gsl:" << endl;
    setup_and_solve();
}
