#include <gsl/gsl_errno.h>
#include <gsl/gsl_matrix.h>
#include <gsl/gsl_odeiv2.h>
#include <cstdio>


// d y_i(t) / d t = f_i(t, y_1(t), y_2(t), ...)

int func (double t, const double y[], double f[], void *params) {
    // Store vector elements f_i(t, y, params)
    double G = *(double *)params;
    double m1 = 10;
    double m2 = 13;
    f[0] = y[1];
    f[1] = -G*m1*(y[0] - y[1])/pow(abs(y[0] - y[1]), 3);
    f[2] = -G*m2*(y[1] - y[0])/pow(abs(y[1] - y[0]), 3);
    return GSL_SUCCESS;
}

void setup_and_solve(void) {
  double G = 10;
  gsl_odeiv2_system sys = {func, NULL, 2, &G};

  gsl_odeiv2_driver *d = gsl_odeiv2_driver_alloc_y_new (&sys, gsl_odeiv2_step_rk4, 1e-6, 1e-6, 0.0);
  int i;
  double t = 0.0, t1 = 100.0;
  double y[2] = { 1.0, 0.0 };

  for (i = 1; i <= 100; i++)
    {
      double ti = i * t1 / 100.0;
      int status = gsl_odeiv2_driver_apply (d, &t, ti, y);

      if (status != GSL_SUCCESS)
        {
          printf ("error, return value=%d\n", status);
          break;
        }

      printf ("%.5e %.5e %.5e\n", t, y[0], y[1]);
    }

  gsl_odeiv2_driver_free(d);
}
