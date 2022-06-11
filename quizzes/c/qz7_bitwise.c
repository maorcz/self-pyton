#include <stdio.h>

unsigned int CountCouplesBitSet(unsigned char num);
void Test(void);
void PrintSuccessOrFail(int is_worked);

int main()
{
	Test();
	
	return 0;
}

unsigned int CountCouplesBitSet(unsigned char num)
{
	unsigned char couple_set = 3;
	unsigned int counter = 0;
	unsigned int i = 0;
	
	for ( i = 0 ; i < 7; i++)
	{
		if ((num & couple_set) == couple_set)
		{
			counter++;
		}
		
		num >>= 1;
	}
	
	return counter;
}

unsigned int CountSetBits(long int num)
{
	unsigned int counter = 0;
	
	while (num)
	{
		num &= ~-num;
		counter++;
	}
	
	return counter;
}

void Test(void)
{
	PrintSuccessOrFail(0 == CountCouplesBitSet(0));
	PrintSuccessOrFail(1 == CountCouplesBitSet(3));
	PrintSuccessOrFail(0 == CountCouplesBitSet(5));
	PrintSuccessOrFail(2 == CountCouplesBitSet(7));
	PrintSuccessOrFail(5 == CountCouplesBitSet(1 + 0*2 + 4 + 8 + 16 +32 +64 + 128));
	
	PrintSuccessOrFail(0 == CountSetBits(0));
	PrintSuccessOrFail(2 == CountSetBits(3));
	PrintSuccessOrFail(2 == CountSetBits(5));
	PrintSuccessOrFail(3 == CountSetBits(7));
	PrintSuccessOrFail(7 == CountSetBits(1 + 0*2 + 4 + 8 + 16 +32 +64 + 128));
	
}

void PrintSuccessOrFail(int is_worked)
{
	printf("%s\n", is_worked ? "Succeeded" : "Failed");
}
