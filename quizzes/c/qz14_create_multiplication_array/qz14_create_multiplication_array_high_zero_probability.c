#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>

void PrintArr(int *arr, size_t size)
{
	size_t i = 0;
	
	for (i = 0 ; i < size - 1 ; i++)
	{
		printf("%d ,", arr[i]);
	}
	
	printf("%d\n", arr[i]);
}

int *CreateMultiplicationArrForHighZeroProbability(int *A, int* B, size_t size)
{
	size_t i = 0;
	size_t count_zeros = 0;
	size_t idx_zero = 0;
	long int mult_all = 1;
	
	assert(A && B);
	
	for (i = 0; i < size ; i++)
	{
		if (A[i])
		{
			mult_all *= A[i];
		}
		else if (0 == count_zeros)
		{
			count_zeros++;
			idx_zero = i;
		}
		else
		{
			mult_all = 0;
			
			break;
		}
	}
	
	if (0 == count_zeros)
	{
		for (i = 0 ; i < size ; i++)
		{
			B[i] = mult_all / A[i];
		}
	}
	else
	{
		memset(B, 0, sizeof(B[0]));
		B[idx_zero] = mult_all;
	}
	
	return B;
}

int main()
{
	int A[4] = {100, 0, 0, 4};
	int dest[4] = {0};
	int *res = NULL;
	
	res = CreateMultiplicationArr(A, dest, 4);

	printf("testing ==> ");
	PrintArr(A, 4);
	printf("result ===> ");
	PrintArr(res, 4);
	
	return 0;
}
