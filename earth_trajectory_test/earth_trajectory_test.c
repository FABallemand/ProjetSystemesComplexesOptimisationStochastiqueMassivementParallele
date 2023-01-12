#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// https://fr.wikipedia.org/wiki/Loi_universelle_de_la_gravitation
// https://www.futura-sciences.com/sciences/definitions/systeme-solaire-perihelie-2/
// https://planet-terre.ens-lyon.fr/ressource/orbite-Terre.xml
// https://forums.futura-sciences.com/archives/708501-calcul-orbite-soleil-terre.html
// https://evgenii.com/blog/earth-orbit-simulation
// https://evgenii.com/files/2016/09/earth_orbit_simulation/the_complete_code/

#define NB_SAMP 1024
#define DIM 2
#define R 0
#define THETA 1

int main()
{
    printf("===================================\n");
    printf("Compute Earth trajectory around Sun\n");
    // Open output file
    FILE *output_file = NULL;
    if ((output_file = fopen("earth_trajectory_output.txt", "w")) == NULL)
    {
        fprintf(stderr, "Error: Unable to open output_file\n");
        exit(1);
    }

    // Constants
    float sun_mass = 1.9884 * pow(10, 30);           //< Sun mass
    float g_const = 6.67408 * pow(10, -11);          //< Gravitational constant
    float delta_t = (365.25 * 24 * 3600) / NB_SAMP; //< Duration between two steps

    // Variables
    double trajectory[NB_SAMP][DIM]; //< Earth trajectory around Sun (polar coord.)
    double prev_speed[DIM];          //< Speed at previous step (polar coord.)
    double curr_speed[DIM];          //< Speed at current step (polar coord.)
    int n = 0;                       //< Current step

    // Initial conditions
    trajectory[n][R] = 147.1 * pow(10, 9);                                   // Initial position (perihelion)
    trajectory[n][THETA] = M_PI;                                             // Initial position (perihelion)
    curr_speed[R] = 0;                                                       // Initial speed (perihelion)
    curr_speed[THETA] = 30.2 * pow(10, 3);                                   // Initial speed (perihelion)
    curr_speed[THETA] = (2 * M_PI) / (365.5 * 24 * 3600);                    // Initial speed (average)
    fprintf(output_file, "%f,%f\n", trajectory[n][R], trajectory[n][THETA]); // Write coord. in output file
    n++;                                                                     // Next step

    // Compute trajectory
    for (; n < NB_SAMP; n++)
    {
        prev_speed[R] = curr_speed[R];
        prev_speed[THETA] = curr_speed[THETA];

        curr_speed[R] = prev_speed[R] + (trajectory[n - 1][R] * prev_speed[THETA] * prev_speed[THETA] - ((g_const * sun_mass) / (trajectory[n - 1][R] * trajectory[n - 1][R]))) * delta_t;
        curr_speed[THETA] = prev_speed[THETA] + ((-2 * prev_speed[R] * prev_speed[THETA]) / trajectory[n - 1][R]) * delta_t;

        trajectory[n][R] = trajectory[n - 1][R] + curr_speed[R] * delta_t;
        trajectory[n][THETA] = trajectory[n - 1][THETA] + curr_speed[THETA] * delta_t;

        fprintf(output_file, "%f,%f\n", trajectory[n][R], trajectory[n][THETA]); // Write coord. in output file
    }

    // Close output file
    fclose(output_file);

    printf("===================================\n");

    return 0;
}