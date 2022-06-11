#include "vector.h"
#include <stdio.h>

void MaxOccurances(char ch);

void ZeroAllVectors(vector_t *vector)
{
	size_t i = 0;
	size_t size = VectorCapacity(vector);
	
	for (i = 0; i < size ; i++)
	{
		*(int *)VectorAccessElement(vector, i) = 0;
	}
}

void CallMaxOccurances(const char ch, size_t times)
{
	size_t i = 0;
	
	for (i = 0 ; i < times ; i++)
	{
		MaxOccurances(ch);
	}
}

void TestMaxOccurances(void)
{
	CallMaxOccurances('a', 29999);
	CallMaxOccurances('b', 70000);
	CallMaxOccurances('c', 200000);
	CallMaxOccurances(0, 1);
	
	CallMaxOccurances('m', 399999);
	CallMaxOccurances('t', 300000);
	CallMaxOccurances(0, 1);
}

int main()
{
	TestMaxOccurances();

	return 0;
}

void MaxOccurances(char ch)
{
	static vector_t *vector = NULL;
	static char max_index = 0;
	static int counter = -1;
	
	counter++;
	
	if (0 == counter)
	{
		vector = VectorCreate(256, sizeof(int));
		ZeroAllVectors(vector);
		MaxOccurances(ch);
	}
	else
	{
		int max_occurances = *(int *)VectorAccessElement(vector, max_index);
		
		if (0 == ch)
		{
			printf("max char occurances ==> '%c' (%d times)\n", max_index, max_occurances);
			ZeroAllVectors(vector);
			max_index = 0;
		}
		else if (++(*(int *)VectorAccessElement(vector, ch)) > max_occurances)
		{
			max_index = ch;
		}
	}
	
	if (1000000 == counter)
	{
		VectorDestroy(vector);
	}
}

