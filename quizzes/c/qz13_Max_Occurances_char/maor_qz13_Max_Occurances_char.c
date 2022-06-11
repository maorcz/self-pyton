#include <stdio.h>
#include <string.h>

void MaxOccurences(char ch);

void CallMaxOccurences(const char ch, size_t times)
{
	size_t i = 0;
	
	for (i = 0 ; i < times ; i++)
	{
		MaxOccurences(ch);
	}
}

void TestMaxOccurences(void)
{
	CallMaxOccurences('a', 29999);
	CallMaxOccurences('b', 70000);
	CallMaxOccurences('c', 200000);
	CallMaxOccurences(0, 1);
	
	CallMaxOccurences('m', 399999);
	CallMaxOccurences('t', 300000);
	CallMaxOccurences(0, 1);
}

int main()
{
	TestMaxOccurences();

	return 0;
}

void MaxOccurences(char ch)
{
	static int occurences_arr[256];
	static char max_index = 0;
	
	int max_occurence = occurences_arr[(int)max_index];
	
	if (0 == ch)
	{
		printf("max char occurences ==> '%c' (%d times)\n", max_index, max_occurence);
		memset(occurences_arr, 0 , sizeof(int));
		max_index = 0;
	}
	else if (++occurences_arr[(int)ch] > max_occurence)
	{
		max_index = ch;
	}
}

