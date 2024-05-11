#include<stdio.h>
#include<math.h>

#define MAX 100

int n; // size of the matrix
double a[MAX][MAX], x[MAX]; // matrix and solution vector

// Gaussian elimination function
void gaussian_elimination() {
    int i, j, k; // loop variables
    double factor; // factor used to eliminate lower elements
    for (i=0; i<n-1; i++) { // loop through each row
        for (j=i+1; j<n; j++) { // loop through each row below the current row
            factor = a[j][i]/a[i][i]; // calculate the factor to eliminate elements
            for (k=i; k<n; k++) { // loop through the elements of the current column
                a[j][k] = a[j][k] - factor * a[i][k]; // eliminate the lower element
            }
        }
    }
}

// back substitution function
void back_substitution() {
    int i, j; // loop variables
    double sum; // sum of products of known variables and coefficients
    for (i=n-1; i>=0; i--) { // loop through each row from bottom to top
        sum = 0;
        for (j=i+1; j<n; j++) { // loop through the elements of the current column
            sum = sum + a[i][j] * x[j]; // add up the products of known variables and coefficients
        }
        x[i] = (a[i][n] - sum) / a[i][i]; // solve for the unknown variable
    }
}

// main function
int main() {
    int i, j; // loop variables
    printf("Enter the order of the matrix: "); // prompt user to enter the size of the matrix
    scanf("%d", &n); // read the size of the matrix
    printf("Enter the elements of the matrix: \n"); // prompt user to enter the elements of the matrix
    for (i=0; i<n; i++) { // loop through each row
        for (j=0; j<=n; j++) { // loop through each element in the current row
            scanf("%lf", &a[i][j]); // read the element of the matrix
        }
    }
    gaussian_elimination(); // perform Gaussian elimination
    back_substitution(); // perform back substitution
    printf("The solution of the system is: \n"); // print the solution
    for (i=0; i<n; i++) { // loop through each unknown variable
        printf("x[%d] = %lf\n", i, x[i]); // print the solution for the current unknown variable
    }
    return 0; // return 0 to indicate successful execution
}
