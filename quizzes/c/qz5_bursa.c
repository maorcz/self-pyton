#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

int *Bursa(const int *stack_prices, int len);
void TestBursa(void);
void PrintSuccessOrFail(int is_worked);

int main()
{
	TestBursa();
	
	return 0;
}

int *Bursa(const int *stack_prices, int len)
{
	int i = 0;
	int min = 0;
	int max = 0;
	int curr_price = 0;
	int earlier_prof = 0;
	int *res_prof = NULL;
	
	assert(stack_prices);
	
	res_prof = (int *)malloc(3 * sizeof(int));
	
	if (!res_prof)
	{
		printf("Allocation Failed\n");
		return NULL;
	}
	
	res_prof[0] = 0;
	res_prof[1] = 0;
	res_prof[2] = 1;
	
	min = stack_prices[0];
	max = stack_prices[1];
	earlier_prof = max - min;
	
	for (i = 1; i < len ; i++)
	{
		/*printf("profit = %d min = %d max = %d\n", res_prof[0], res_prof[1], res_prof[2]);*/
		
		curr_price = stack_prices[i];
		
		if (curr_price > max)
		{
			res_prof[2] = i;
			max = curr_price;
			earlier_prof = max - min;
		}
		else if (curr_price < min)
		{
			res_prof[1] = i;
			max = min = curr_price;
		}
	}
	
	res_prof[0] = earlier_prof;
	
	printf("profit = %d min = %d max = %d ---------->", res_prof[0], res_prof[1], res_prof[2]);
	
	return res_prof; 
}

void TestBursa(void)
{
	int *res = NULL;
	
	int len1 = 8;
	const int stack_prices1[] = {6, 12, 3, 5, 1, 4, 9, 2};
	
	int len2 = 6;
	const int stack_prices2[] = {5, 2, 1, 4, 5, 6};
	
	int len3 = 3;
	const int stack_prices3[] = {7, 0, 46};
	
	int len4 = 9;
	const int stack_prices4[] = {100, 13, 1, 4, 5, 6, 120, 1, 13};
	
	/* check1 */
	res = Bursa(stack_prices1, len1);
	PrintSuccessOrFail(res[0] == 8 && res[1] == 4 && res[2] == 6);
	free(res);
	res = NULL;
	
	/* check2 */
	res = Bursa(stack_prices2, len2);
	PrintSuccessOrFail(res[0] == 5 && res[1] == 2 && res[2] == 5);
	free(res);
	res = NULL;
	
	/* check3 */
	res = Bursa(stack_prices3, len3);
	PrintSuccessOrFail(res[0] == 46 && res[1] == 1 && res[2] == 2);
	free(res);
	res = NULL;
	
	/* check4 */
	res = Bursa(stack_prices4, len4);
	PrintSuccessOrFail(res[0] == 119 && res[1] == 2 && res[2] == 6);
	free(res);
	res = NULL;
}

void PrintSuccessOrFail(int is_worked)
{
	printf("%s\n", is_worked ? "Succeeded" : "Failed");
	
}
