#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define NB_SAMP 1024
#define DIM 2
#define R 0
#define THETA 1

#define SUN_WEIGHT = 1.9884 * pow(10, 30) // Masse du Soleil
#define G = 6, 67408 * pow(10, -11)       // Constante gravitationnelle

int main()
{
    // Open output file
    FILE *output_file = NULL;
    if ((output_file = fopen("earth_trajectory_output.txt", "w")) == NULL)
    {
        fprintf(stderr, "Error: Unable to open output_file\n");
        exit(1);
    }

    // Constants
    float sun_weight = 1.9884 * pow(10, 30); // Sun weight
    float g_const = 6.67408 * pow(10, -11);  // Gravitational constant

    // Variables
    double trajectory[NB_SAMP][DIM];                 //< Earth trajectory around Sun (polar coord.)
    double prev_speed[DIM];                          //< Speed at previous step (polar coord.)
    double curr_speed[DIM];                          //< Speed at current step (polar coord.)
    double delta_t = (365.25 * 24 * 3600) / NB_SAMP; //< Duration between two steps
    int n = 0;                                       //< Current step

    // Initial conditions
    trajectory[n][R] = 147 * pow(10, 6);   //< Initial position (perihelion)
    trajectory[n][THETA] = M_1_PI;         //< Initial position (perihelion)
    curr_speed[R] = 0;                     //< Initial speed (perihelion)
    curr_speed[THETA] = 30.2 * pow(10, 3); //< Initial speed (perihelion)
    n++;                                   //< Next step

    // Compute trajectory
    for (; n < NB_SAMP; n++)
    {
        prev_speed[R] = curr_speed[R];
        prev_speed[THETA] = curr_speed[THETA];

        curr_speed[R] = prev_speed[R] + (2 * trajectory[n - 1][R] * prev_speed[THETA] - (g_const * sun_weight) / (trajectory[n - 1][R] * trajectory[n - 1][R])) * delta_t;
        curr_speed[THETA] = prev_speed[THETA] + ((-2 * prev_speed[R] * prev_speed[THETA]) / trajectory[n - 1][R]) * delta_t;

        trajectory[n][R] = trajectory[n - 1][R] + curr_speed[R] * delta_t;
        trajectory[n][THETA] = trajectory[n - 1][THETA] + curr_speed[THETA] * delta_t;

        fprintf(output_file, "%f,%f\n", trajectory[n][R], trajectory[n][THETA]); // Write coord. in output file
    }

    // Close output file
    fclose(output_file);

    return 0;
}