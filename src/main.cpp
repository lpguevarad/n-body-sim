#include <iostream>
#include "Planet.h"

using namespace std;

int main(int argc, char *argv[]) {
    Planet p = Planet(32.1, 0, 0, 0, 0, 0, 0);  

    cout << "Test Planet class:" << endl;
    cout << p.m << endl;
}
