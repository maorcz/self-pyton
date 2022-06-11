#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/* works for bigger numbers */
/*
long int *CreateMultiplicationArr(int *A, size_t size)
{
	size_t i = 0, j = 0;
	long int *B = malloc(size * sizeof(long int));
	
	if (!B)
	{
		printf("malloc failed\n");
		
		return NULL;
	}
	
	for (i = 0 ; i < size ; i++)
	{
		B[i] = 1;
	}
	
	for (i = 0; i < size ; i++)
	{
		for (j = (i + 1) % size ; j != i ; j = (j + 1) % size)
		{
			B[i] *= A[j];
		}
	}
	
	return B;
}
*/

void PrintArrLong(long int *arr, size_t size)
{
	size_t i = 0;
	
	for (i = 0 ; i < size - 1 ; i++)
	{
		printf("%ld ,", arr[i]);
	}
	
	printf("%ld\n", arr[i]);
}

void PrintArrInt(int *arr, size_t size)
{
	size_t i = 0;
	
	for (i = 0 ; i < size - 1 ; i++)
	{
		printf("%d ,", arr[i]);
	}
	
	printf("%d\n", arr[i]);
}

int *CreateMultiplicationArr(int *A, size_t size)
{
	size_t i = 0;
	size_t last_idx = size - 1;
	int *B = malloc(size * sizeof(int));
	int *mult_from_right = malloc(size * sizeof(int));
	
	if (!mult_from_right || !B)
	{
		free(mult_from_right);
		free(B);
		
		return NULL;
	}
	
	mult_from_right[last_idx] = 1;
	
	for (i = last_idx ; i > 0 ; i--)
	{
		mult_from_right[i - 1] = mult_from_right[i] * A[i];
	}
	
	B[0] = 1;
	
	for (i = 0 ; i < last_idx ; i++)
	{
		B[i + 1] = B[i] * A[i];
		B[i] *= mult_from_right[i];
	}
	
	B[last_idx] *= mult_from_right[last_idx];
	
	free(mult_from_right);
	mult_from_right = NULL;
	
	return B;
}

int main()
{
	int test[4] = {1000, 1000, 1000, 1000};
	int *res = NULL;
	
	res = CreateMultiplicationArr(test, 4);

	printf("testing ==> ");
	PrintArrInt(test, 4);
	printf("result ===> ");
	PrintArrInt(res, 4);
	
	free(res);
	res = NULL;
	
	return 0;
}
